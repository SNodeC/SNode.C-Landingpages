# MQTTStore

MQTTStore is the MQTTSuite MQTT 3.1.1 persistence service. It connects to a broker as an MQTT client, subscribes to configured topic filters, writes every received MQTT publish to a raw MariaDB envelope table, and can independently project selected JSON/topic fields into typed application tables.

The default philosophy is **raw envelope first**:

```text
MQTT publish
  -> raw MQTT row
  -> optional JSON-only typed projections
```

That keeps the original topic, payload, QoS, retain/dup state, and receive context available even when projection schemas evolve.

Use [MQTTIntegrator](../mqttintegrator/README.md) before Store when device/vendor payloads should be normalized first. Use [MQTTCli](../mqttcli/README.md) to generate known test traffic. The whole-suite build and common configuration model are in the [MQTTSuite README](../README.md).

## Quick Start

### 1. Create a MariaDB database and dedicated user

Log in as a MariaDB administrator:

```bash
sudo mariadb
```

Create the database and a service user:

```sql
CREATE DATABASE mqttsuite_store
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER 'mqttstore'@'127.0.0.1'
  IDENTIFIED BY 'replace-with-a-long-random-password';

GRANT CREATE, INSERT, SELECT, INDEX
  ON mqttsuite_store.*
  TO 'mqttstore'@'127.0.0.1';

FLUSH PRIVILEGES;
```

MQTTStore can auto-create its raw table inside an existing database. It does **not** create the database or database user.

Do not run the service as MariaDB `root`.

### 2. Start MQTTStore

For a local plain MQTT/IPv4 broker:

```bash
mqttstore \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session \
      --client-id mqttstore-local \
      --qos 1 \
    sub --topic 'normalized/#' \
    db \
      --host 127.0.0.1 \
      --database mqttsuite_store \
      --username mqttstore \
      --password 'replace-with-a-long-random-password' \
      storage \
        --raw-table mqtt_messages \
        --auto-create-raw-table
```

The `storage` section is nested below `db` in the current command hierarchy. `--auto-create-raw-table` defaults to `true`; it is shown explicitly here so the permission requirement is visible in the command itself.

### 3. Publish a known message

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id store-test-publisher --qos 1 \
    pub --topic normalized/room-01/temperature \
        --message '{"value":21.7,"unit":"C"}'
```

### 4. Verify MariaDB

```bash
mariadb -h 127.0.0.1 -u mqttstore -p mqttsuite_store
```

Then:

```sql
SELECT id,
       received_at,
       source_instance,
       topic,
       qos,
       retain_flag,
       payload_format,
       payload_text
FROM mqtt_messages
ORDER BY id DESC
LIMIT 5;
```

The latest row should contain topic `normalized/room-01/temperature`, QoS 1, and `payload_format = 'json'`.

## How MQTTStore is assembled

MQTTStore uses the SNode.C MQTT client composition used elsewhere in MQTTSuite. Its `SocketContextFactory` reads the selected connection instance's:

- `session`;
- `sub`;
- `db`;
- nested `storage`

configuration, loads/validates the optional projection plan when the MQTT transport reaches context creation, and creates an MQTT context with Store-specific behavior.

The MQTT behavior owns a `MariaDbStorage` object. Each received PUBLISH is represented as an MQTT message envelope and passed to storage.

Because the transport endpoint is separate from Store behavior, the same persistence logic can sit above direct IPv4/IPv6/Unix-domain MQTT or MQTT-over-WebSocket/WSS client paths where compiled.

## Build and install result

`mqttstore` is part of the repository's top-level CMake build. The Store library requires SNode.C components:

```text
mqtt-client
db-mariadb
```

so the whole-suite build requires the MariaDB development/runtime support needed by SNode.C's database component.

A complete install places:

```text
${CMAKE_INSTALL_PREFIX}/bin/mqttstore
```

MQTTStore does not install a Web UI.

See [Build and install](../README.md#build-and-install) for the complete suite build.

## The raw envelope table

`--auto-create-raw-table` is a boolean Store option whose source default is **`true`**. With auto-create enabled, MQTTStore executes `CREATE TABLE IF NOT EXISTS` for the selected raw table.

Explicit forms are:

```text
storage --auto-create-raw-table=true
storage --auto-create-raw-table=false
```

Use the `false` form when a DBA owns the raw-table DDL and the Store service account should not need `CREATE`/`INDEX` privileges.

The source default table name is:

```text
mqtt_messages
```

Override it with:

```text
storage --raw-table <identifier>
```

Table names are restricted to letters, digits, and `_` by the current storage implementation.

The automatically managed table contains:

| Column | Type | Meaning |
| --- | --- | --- |
| `id` | `BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY` | stable row id |
| `received_at` | `TIMESTAMP(6)` | database-side receive timestamp |
| `source_instance` | `VARCHAR(255)` | MQTTSuite connection name |
| `topic` | `VARCHAR(1024)` | MQTT topic |
| `qos` | `TINYINT UNSIGNED` | received publish QoS |
| `retain_flag` | `BOOLEAN` | MQTT retain flag |
| `dup_flag` | `BOOLEAN` | MQTT DUP flag |
| `packet_identifier` | `INT UNSIGNED NULL` | packet identifier when represented |
| `payload` | `LONGBLOB` | original payload bytes |
| `payload_text` | `LONGTEXT NULL` | text representation when safe to expose as text |
| `payload_json` | `JSON NULL` | parsed JSON representation when parsing succeeds |
| `payload_format` | `ENUM('json','text','binary')` | current payload classification |

The table also creates indexes on `received_at` and the first 255 topic characters.

> **Figure placeholder — Raw-envelope-first persistence.** Show one received MQTT PUBLISH becoming a row with topic/QoS/retain/dup/packet id/raw payload plus the derived text/JSON/classification fields.

## Payload classification

MQTTStore always stores the raw payload.

It then classifies the payload:

### JSON

If `nlohmann::json` parses the payload successfully:

```text
payload_format = json
payload_text   = original payload text
payload_json   = parsed JSON document
```

### Text

If parsing as JSON fails but the payload contains no binary control content according to the current classifier:

```text
payload_format = text
payload_text   = payload text
payload_json   = NULL
```

### Binary

If parsing as JSON fails and binary control content is detected:

```text
payload_format = binary
payload_text   = NULL
payload_json   = NULL
```

The raw `LONGBLOB` remains populated in all cases.

This is a storage classification, not a content-type declaration from MQTT; MQTT 3.1.1 payloads remain arbitrary bytes.

## Database configuration

The `db` subcommand exposes:

```text
--host
--port
--socket
--database
--username
--password
--flags
```

The source default port is `3306`. The `--socket` option has a **non-empty source default**:

```text
/run/mysqld/mysqld.sock
```

and its source help text is:

> Database socket file (overrides host and port when set)

That is the configuration contract exposed by MQTTStore. The final connection behavior is still delegated to the underlying MariaDB client API, so inspect the effective configuration with `--show-config` and do not assume that supplying a remote `--host` alone has neutralized a configured socket value.

For an explicitly remote database, set the intended host and port and verify the resolved socket value/connection behavior for that deployment:

```bash
db \
  --host db.example.net \
  --port 3306 \
  --database mqttsuite_store \
  --username mqttstore \
  --password 'replace-with-a-long-random-password'
```

For a deliberately local socket deployment, set `--socket` to the actual server socket.

### Permission profiles

Use only the grants required by your operating model.

| Model | Typical service grants | Ownership / required Store setting |
| --- | --- | --- |
| raw table auto-create | `CREATE, INSERT, SELECT, INDEX` on the Store database | MQTTStore creates/ensures raw table; default `--auto-create-raw-table=true` |
| DBA-created raw table | `INSERT, SELECT` | DBA owns table DDL; start Store with `storage --auto-create-raw-table=false` |
| raw + projections | raw-table permissions plus `INSERT` on projection tables | DBA/application migrations own projection DDL |
| diagnostics user | `SELECT` only | separate observer/dashboard account |

The service source inserts data; it does not require you to share its write credentials with dashboards or analysts.

## MQTT session and subscriptions

The `session` section includes:

```text
--client-id
--qos
--retain-session
--keep-alive
--will-topic
--will-message
--will-qos
--will-retain
--username
--password
--session-store
```

`--retain-session` sets MQTT `clean_session=false` in the current Store factory.

Use `--session-store` when the local MQTT client/session state should survive Store restarts:

```bash
session \
  --client-id mqttstore-normalized \
  --retain-session \
  --session-store /var/lib/mqttsuite/mqttstore-session.json
```

The `sub --topic` option accepts multiple filters and the same `##<qos>` override syntax used by MQTTCli.

Examples:

```bash
sub \
  --topic 'normalized/+/temperature##1' \
  --topic 'alerts/###2'
```

The second string represents filter `alerts/#` at QoS 2.

Narrow subscriptions are easier to operate than a universal `#` when only a defined telemetry namespace belongs in the database.

## Optional typed projections

Raw storage works without projections.

A projection is an additional insert into an operator-managed typed table when:

1. the raw message payload is valid JSON;
2. the message topic matches the projection's MQTT filter.

The current schema is [`lib/projection-schema.json`](lib/projection-schema.json).

A projection file may be either:

```json
[
  { "...": "projection" }
]
```

or:

```json
{
  "projections": [
    { "...": "projection" }
  ]
}
```

The `storage` option is:

```text
--projection-file <file>
```

The projection file is loaded and validated in `SocketContextFactory::create()` **when an MQTT transport connection reaches Store context creation**. If loading or schema validation throws, Store logs the error and rethrows it into that connection-establishment path.

The exact process-level/retry/reconnect consequence of a malformed projection file has not been established by the landing-page runtime qualification and remains **[UNVERIFIED-RUNTIME]**. Do not rely on a claim that projection validation always happens before any connection attempt or that every malformed plan necessarily terminates the entire process at initial startup.

## A complete projection example

Assume normalized messages arrive on:

```text
normalized/<device>/temperature
```

with payload:

```json
{"value":21.7,"unit":"C"}
```

Create a typed table:

```sql
CREATE TABLE sensor_measurements (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(255) NOT NULL,
    metric VARCHAR(255) NOT NULL,
    value DOUBLE NULL,
    unit VARCHAR(64) NULL,
    received_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
);
```

Create `projections.json`:

```json
{
  "projections": [
    {
      "name": "room_temperature",
      "topic": "normalized/+/temperature",
      "table": "sensor_measurements",
      "columns": {
        "device_id": {
          "topic_level": 1,
          "required": true
        },
        "metric": {
          "literal": "temperature"
        },
        "value": {
          "json_pointer": "/value",
          "required": true
        },
        "unit": {
          "json_pointer": "/unit"
        }
      }
    }
  ]
}
```

Start Store with:

```bash
mqttstore \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id mqttstore-projection --qos 1 \
    sub --topic 'normalized/#' \
    db \
      --host 127.0.0.1 \
      --database mqttsuite_store \
      --username mqttstore \
      --password 'replace-with-a-long-random-password' \
      storage \
        --raw-table mqtt_messages \
        --auto-create-raw-table \
        --projection-file ./projections.json
```

The raw insert and projection insert are separate storage operations. A projection failure does not retroactively remove a successfully submitted raw-envelope insert.

> **Figure placeholder — JSON/topic projection extraction.** Show a JSON MQTT row branching into a typed projection where `topic_level`, `json_pointer`, and `literal` each populate a different SQL column while the raw row remains independent.

## Projection fields

Each projection requires:

```text
topic
table
columns
```

and may have a human-readable `name`.

### `topic`

MQTT topic filter:

```json
"topic": "normalized/+/temperature"
```

The current matcher supports literals, `+`, and terminal `#`.

### `table`

SQL identifier for the target table:

```json
"table": "sensor_measurements"
```

MQTTStore does **not** create projection tables. They are domain schemas and should be managed through your normal DBA/migration process.

### Column from JSON Pointer

```json
"value": {
  "json_pointer": "/value",
  "required": true
}
```

Pointers must be non-empty RFC 6901-style strings beginning with `/`.

The shorthand:

```json
"value": "/value"
```

means the same JSON Pointer source without `required`.

### Column from topic level

```json
"device_id": {
  "topic_level": 1
}
```

Topic levels are zero-based.

For:

```text
normalized/boiler/temperature
```

the levels are:

```text
0 = normalized
1 = boiler
2 = temperature
```

### Literal column

```json
"metric": {
  "literal": "temperature"
}
```

This writes the same constant string to every matching projection row.

### `required`

The current implementation's semantics are precise:

- source present → insert the value;
- source missing and `required: false` → omit that SQL column from the insert;
- source missing and `required: true` → include the column with SQL `NULL`.

Omitting an optional column lets the table's own default/nullable behavior decide the result. `required: true` does not reject the message; it forces an explicit `NULL` for a missing source.

## Verify the projection

Publish:

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id projection-pub --qos 1 \
    pub --topic normalized/boiler/temperature \
        --message '{"value":63.4,"unit":"C"}'
```

Check raw storage:

```sql
SELECT topic, qos, payload_format, payload_text
FROM mqtt_messages
ORDER BY id DESC
LIMIT 1;
```

Check typed projection:

```sql
SELECT device_id, metric, value, unit
FROM sensor_measurements
ORDER BY id DESC
LIMIT 1;
```

Expected projection:

```text
boiler | temperature | 63.4 | C
```

If the raw row exists but the projection row does not, focus on JSON validity, topic-filter matching, JSON Pointer paths, target-table existence, and `INSERT` grants.

## More storage examples

### Plain text

Publish:

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id text-pub --qos 0 \
    pub --topic devices/pump-1/status --message running
```

Expected raw classification:

```text
payload_format = text
payload_text   = running
payload_json   = NULL
```

### Retained state

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id retained-pub --qos 1 \
    pub --topic devices/pump-1/availability \
        --message online \
        --retain
```

The raw row records `retain_flag`. Store does not decide whether a retained message represents “new telemetry” or “current state”; that interpretation belongs to the consumer/data model.

### QoS 1

The raw row records the QoS of the PUBLISH delivered to Store. Use `session --qos 1` in MQTTCli or a topic-specific Store subscription override when you need to exercise that path.

### Binary

MQTTCli's normal shell examples are text-oriented. Binary publishers are still valid MQTT clients; Store preserves the raw bytes in `payload` and classifies detected binary control content as `binary` when it is not valid JSON.

## Transport examples

MQTTStore creates these client families when compiled in:

```text
in-mqtt       in-mqtts
in6-mqtt      in6-mqtts
un-mqtt       un-mqtts
in-wsmqtt     in-wsmqtts
in6-wsmqtt    in6-wsmqtts
un-wsmqtt     un-wsmqtts
```

They are created disabled; enable the one Store should use.

### TLS

```bash
mqttstore \
  in-mqtts --disabled=false \
    remote --host broker.example.net --port 8883 \
    session --client-id mqttstore-tls \
    sub --topic 'normalized/#' \
    db ... \
      storage ...
```

Configure the SNode.C TLS section for the selected instance.

### WebSocket

```bash
mqttstore \
  in-wsmqtt --disabled=false \
    remote --host 127.0.0.1 --port 8080 \
    http --target /ws \
    session --client-id mqttstore-ws \
    sub --topic 'normalized/#' \
    db ... \
      storage ...
```

The WebSocket target defaults to `/ws` and uses subprotocol `mqtt`.

### WSS

Select `in-wsmqtts`, configure the remote host/port and SNode.C TLS section, then keep the same `session`, `sub`, `db`, and `storage` behavior.

### Unix-domain MQTT

```bash
mqttstore \
  un-mqtt --disabled=false \
    remote --sun-path /run/mqttsuite/broker.sock \
    session --client-id mqttstore-unix \
    sub --topic 'normalized/#' \
    db ... \
      storage ...
```

Unix-domain MQTT is useful when Broker and Store share a host and you do not want the MQTT link bound to TCP.

## Persist the Store configuration

A Store command often contains database and MQTT credentials. After verifying it, you can write the SNode.C application configuration:

```bash
mqttstore \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session \
      --client-id mqttstore-normalized \
      --retain-session \
      --session-store /var/lib/mqttsuite/mqttstore-session.json \
    sub --topic 'normalized/#' \
    db \
      --host 127.0.0.1 \
      --database mqttsuite_store \
      --username mqttstore \
      --password 'replace-with-a-long-random-password' \
      storage \
        --raw-table mqtt_messages \
        --auto-create-raw-table \
        --projection-file /etc/mqttsuite/projections.json \
  --write-config ./mqttstore.conf
```

Then:

```bash
mqttstore --config-file ./mqttstore.conf
```

Set restrictive ownership/permissions on saved configuration and projection files.

## Operating the database

MQTTStore owns message insertion, not the entire database lifecycle.

The operator/DBA still owns:

- database/user creation;
- projection-table DDL and migrations;
- indexes beyond the raw table's built-ins;
- backup/restore;
- access controls for readers;
- data retention and deletion;
- capacity planning;
- monitoring failed inserts and table growth.

A wildcard subscription can produce a large raw table quickly. Choose filters and retention policy deliberately.

## Trust and data boundaries

- MQTTStore deliberately persists raw MQTT payloads. Assume the database may contain whatever devices/clients publish on the selected filters.
- Database credentials can appear in command lines or saved config files; protect both.
- MQTT username/password and session-store paths are likewise configuration material.
- TLS/WSS protects the broker connection when configured correctly; database access controls and MQTT authorization remain separate concerns.
- Projection tables can contain extracted sensitive fields even when dashboards never read the raw table.
- Backups replicate the raw-data exposure unless encrypted/access-controlled separately.
- Debug logs may include topic/payload/database connection diagnostics.

## Troubleshooting

### Store starts but no raw rows appear

Check:

1. the selected MQTT instance has `--disabled=false`;
2. Broker connection succeeds;
3. subscription filter matches the test topic;
4. database connection succeeds;
5. service account has `INSERT`;
6. raw table exists or auto-create has permission to create it.

### Raw table is not created

Confirm:

- database already exists;
- `storage --auto-create-raw-table=true` is effective (it is the source default);
- raw table name contains only letters/digits/underscore;
- user has `CREATE` and `INDEX` as required by the auto-create workflow.

If the raw table is intentionally DBA-managed, use `storage --auto-create-raw-table=false` and verify the table already exists.

### Projection plan fails during MQTT context creation

Check JSON syntax and [`lib/projection-schema.json`](lib/projection-schema.json). Projection loading/validation occurs from `SocketContextFactory::create()` when the MQTT transport reaches Store context creation. The exception is logged and rethrown into that connection path.

The exact whole-process/retry/reconnect consequence is **[UNVERIFIED-RUNTIME]** in the current qualification. Do not diagnose every malformed projection plan as a guaranteed process-startup exit without reproducing that behavior in the deployment being tested.

### Raw row exists but projection does not

Check:

- payload is valid JSON;
- projection `topic` filter matches;
- target table exists;
- column names are safe SQL identifiers;
- JSON Pointer exists or missing-value behavior is acceptable;
- topic level is in range;
- user has `INSERT` on the projection table.

### Text expected, binary classified

Review the raw payload bytes. The classifier treats NUL and non-text control content as binary when the payload is not valid JSON.

## Related documentation

- [MQTTSuite overview and build](../README.md)
- [MQTTBroker](../mqttbroker/README.md)
- [MQTTIntegrator](../mqttintegrator/README.md)
- [MQTTBridge](../mqttbridge/README.md)
- [MQTTCli](../mqttcli/README.md)
- [Store storage and projection reference](../docs/store-storage.md)
- [Projection schema](lib/projection-schema.json)

The older implementation-repository `docs/mqttstore-user-guide.md` is intentionally not used as a canonical publication route here because it predates the current evidence boundaries and command examples.

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```