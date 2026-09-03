cmake_minimum_required(VERSION 3.18)

project(SNodeCLandingpagesFigures NONE)

# -----------------------------------------------------------------------------
# Reproducible technical-figure generation
# -----------------------------------------------------------------------------
#
# Canonical technical figure sources live below:
#
#   <project>/assets/src/tikz/*.tex
#
# Figure names are intentionally not enumerated here. New TikZ figures become
# build inputs automatically when their .tex source is added. Shared visual
# system files ending in "-figure-system.tex" are excluded from the figure list
# and are treated as dependencies instead.
#
# Configure/build from the repository root, for example:
#
#   cmake -S . -B cmake-build-figures
#   cmake --build cmake-build-figures --target figures --parallel
#
# Each source
#
#   <project>/assets/src/tikz/<name>.tex
#
# produces
#
#   <project>/assets/<name>.svg
#
# SVG is the canonical generated format for technical diagrams. Runtime/UI
# evidence remains genuine raster capture and is intentionally outside this
# target.

find_program(PDFLATEX_EXECUTABLE NAMES pdflatex REQUIRED)
find_program(INKSCAPE_EXECUTABLE NAMES inkscape REQUIRED)

file(
    GLOB_RECURSE TIKZ_TEX_SOURCES
    CONFIGURE_DEPENDS
    RELATIVE "${CMAKE_SOURCE_DIR}"
    "*/assets/src/tikz/*.tex"
)

set(TIKZ_FIGURE_OUTPUTS "")
set(TIKZ_FIGURE_NAMES "")

foreach(TIKZ_SOURCE_REL IN LISTS TIKZ_TEX_SOURCES)
    get_filename_component(TIKZ_FILENAME "${TIKZ_SOURCE_REL}" NAME)

    # Shared style/system sources are included by figures but are not figures.
    if(TIKZ_FILENAME MATCHES "-figure-system\.tex$")
        continue()
    endif()

    # Extract the owning project from
    # <project>/assets/src/tikz/<possibly/nested/path>/<name>.tex.
    if(NOT TIKZ_SOURCE_REL MATCHES "^([^/]+)/assets/src/tikz/(.+)\.tex$")
        message(FATAL_ERROR
            "Unexpected TikZ figure path: ${TIKZ_SOURCE_REL}. "
            "Expected <project>/assets/src/tikz/<name>.tex"
        )
    endif()

    set(TIKZ_PROJECT "${CMAKE_MATCH_1}")
    set(TIKZ_FIGURE_SUBPATH "${CMAKE_MATCH_2}")

    get_filename_component(TIKZ_SOURCE_ABS
        "${CMAKE_SOURCE_DIR}/${TIKZ_SOURCE_REL}" ABSOLUTE)
    get_filename_component(TIKZ_SOURCE_DIR
        "${TIKZ_SOURCE_ABS}" DIRECTORY)
    get_filename_component(TIKZ_STEM
        "${TIKZ_SOURCE_ABS}" NAME_WE)

    # Publication assets are intentionally flat within each project's assets/
    # directory. Reject duplicate output names early instead of silently
    # overwriting one figure with another.
    set(TIKZ_OUTPUT
        "${CMAKE_SOURCE_DIR}/${TIKZ_PROJECT}/assets/${TIKZ_STEM}.svg")
    list(FIND TIKZ_FIGURE_OUTPUTS "${TIKZ_OUTPUT}" TIKZ_DUPLICATE_INDEX)
    if(NOT TIKZ_DUPLICATE_INDEX EQUAL -1)
        message(FATAL_ERROR
            "Duplicate TikZ publication output '${TIKZ_OUTPUT}'. "
            "Figure basenames must be unique within one project."
        )
    endif()

    # Give each source its own temporary TeX build directory so auxiliary and
    # PDF files never collide, even when figures build in parallel.
    string(MAKE_C_IDENTIFIER
        "${TIKZ_PROJECT}_${TIKZ_FIGURE_SUBPATH}" TIKZ_WORK_ID)
    set(TIKZ_WORK_DIR
        "${CMAKE_BINARY_DIR}/tikz/${TIKZ_WORK_ID}")
    set(TIKZ_PDF
        "${TIKZ_WORK_DIR}/${TIKZ_STEM}.pdf")

    # Any .tex file next to the figure can be a shared input (notably the
    # canonical *-figure-system.tex). Depending on all sibling .tex files keeps
    # style changes reproducible without hard-coding a particular system name.
    file(
        GLOB TIKZ_LOCAL_TEX_DEPENDENCIES
        CONFIGURE_DEPENDS
        "${TIKZ_SOURCE_DIR}/*.tex"
    )

    add_custom_command(
        OUTPUT "${TIKZ_OUTPUT}"
        COMMAND "${CMAKE_COMMAND}" -E make_directory "${TIKZ_WORK_DIR}"
        COMMAND
            "${PDFLATEX_EXECUTABLE}"
            -interaction=nonstopmode
            -halt-on-error
            -file-line-error
            -output-directory=${TIKZ_WORK_DIR}
            "${TIKZ_SOURCE_ABS}"
        COMMAND
            "${INKSCAPE_EXECUTABLE}"
            --pdf-font-strategy=keep
            "${TIKZ_PDF}"
            --export-type=svg
            --export-filename=${TIKZ_OUTPUT}
        DEPENDS
            "${TIKZ_SOURCE_ABS}"
            ${TIKZ_LOCAL_TEX_DEPENDENCIES}
        WORKING_DIRECTORY "${TIKZ_SOURCE_DIR}"
        COMMENT "TikZ -> SVG: ${TIKZ_SOURCE_REL}"
        VERBATIM
    )

    list(APPEND TIKZ_FIGURE_OUTPUTS "${TIKZ_OUTPUT}")
    list(APPEND TIKZ_FIGURE_NAMES "${TIKZ_PROJECT}/${TIKZ_STEM}")
endforeach()

if(TIKZ_FIGURE_OUTPUTS)
    add_custom_target(figures ALL DEPENDS ${TIKZ_FIGURE_OUTPUTS})

    list(LENGTH TIKZ_FIGURE_OUTPUTS TIKZ_FIGURE_COUNT)
    message(STATUS "Discovered ${TIKZ_FIGURE_COUNT} TikZ figure source(s)")
    foreach(TIKZ_FIGURE_NAME IN LISTS TIKZ_FIGURE_NAMES)
        message(STATUS "  figure: ${TIKZ_FIGURE_NAME}")
    endforeach()
else()
    # Keep the target available before the first concrete figure source lands.
    add_custom_target(figures)
    message(STATUS "No TikZ figure sources found yet")
endif()
