# Maintainer: Groctel <aur@taxorubio.com>
# Maintainer: Naveen M K <naveen521kk@gmail.com>
# shellcheck disable=SC2034,SC2154,SC2164

pkgbase=manimce
pkgname=manim
pkgver=0.21.0
pkgrel=1
pkgdesc="Animation engine for explanatory math videos (community edition)."

_name="$pkgname"

arch=("any")
license=("MIT" "custom")
url="https://github.com/ManimCommunity/manim"

source=("$url/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('4b738d95c58f5849b3929239fc37dd02f09fd7006e0609f37eed766dc21aadbbd9318b823b42d98848499532ce00b8abc8a4623764777acf092ad9efe0d712b5')

conflicts=("python-manimlib")

depends=(
    "ffmpeg"
    "python"
    "python-beautifulsoup4"
    "python-cairo"
    "python-click"
    "python-decorator"
    "python-importlib-metadata"
    "python-networkx"
    "python-numpy"
    "python-pillow"
    "python-pygments"
    "python-rich"
    "python-scipy"
    "python-tqdm"
    "python-typing_extensions"
    "python-watchdog"
    # Aur dependencies
    "python-audioop-lts"
    "python-av"
    "python-cloup"
    "python-glcontext"
    "python-isosurfaces"
    "python-manimpango"
    "python-mapbox-earcut"
    "python-moderngl"
    "python-moderngl-window"
    "python-pydub"
    "python-screeninfo"
    "python-skia-pathops"
    "python-srt"
    "python-svgelements"
)
makedepends=(
    "python-build"
    "python-hatchling"
    "python-installer"
    "python-poetry-core"
    "python-setuptools"
    "python-uv-build"
    "python-wheel"
)
optdepends=(
    "python-dearpygui: Graphical frontend"
    "jupyterlab: Jupyter integration"
    "python-grpcio-tools: WebGL renderer"
    "python-typst: Support for TypstMobjects"
    "texlive-core: LaTeX support"
)
checkdepends=(
    "dvisvgm"
    "python-pytest"
    "python-pytest-cov"
    "texlive-latex"
    "texlive-latexextra"
    "xorg-server-xvfb"
)

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

# Declare the paths here, but we need the env of check() to know the full paths
CHECK_TYPST_TESTS_PATH=""
CHECK_OPENGL_TESTS_PATH=""

check() {
    cd "$srcdir/$pkgname-$pkgver"

    CHECK_TYPST_TESTS_PATH="$PWD/tests/module/mobject/text/test_typst_mobject.py"
    CHECK_OPENGL_TESTS_PATH="$PWD/tests/test_scene_rendering/opengl/"

    pytest_cmd="$(__pytest_cmd)"
    suppressed_tests="$(__suppress_tests)"
    testdir="$(__patch_tests)"
    site_packages_path="$(__site_packages_path)"

    has_python_typst="$(pacman -Qq python-typst 2>/dev/null || true)"

    __disable_test_files \
        "$has_python_typst" \
        "$headless_failing_tests_paths" \
        "$CHECK_TYPST_TESTS_PATH"

    # pyproject.toml's [tool.pytest.ini_options] addopts pulls in pytest-cov
    # (and previously pytest-xdist); neither is useful in a package build.
    # -o overrides the ini value, so this stays correct if upstream edits it.
    PATH="$(__testdir_path "$testdir")" \
    PYTHONPATH="$testdir/$site_packages_path" \
    $pytest_cmd \
        -o addopts="" \
        -k "$suppressed_tests" #suppressed_tests may be empty, that's fine

    __restore_test_files \
        "$has_python_typst" \
        "$headless_failing_tests_paths" \
        "$CHECK_TYPST_TESTS_PATH"
}

package() {
    cd "$srcdir/$pkgname-$pkgver"

    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -D -m644 LICENSE.community "$pkgdir/usr/share/licenses/$pkgname/LICENSE.community"
}

# If the user doesn't have typst insalled, we make a backup of the typst test
# file so that we prevent the tests from failing after running it. We need to
# check if the file exists, as it's possible for the user to run makepkg after
# interruping the tests before they run __remove_typst_tests.
__disable_test_files() {
    has_python_typst="$1"
    headless_failing_tests_paths="$2"

    cd "$srcdir/$pkgname-$pkgver"

    if [ -z "$has_python_typst" ]; then
        echo "PKGBUILD NOTE: python-typst not found, disabling its tests"

        if [ -f "$CHECK_TYPST_TESTS_PATH" ]; then
            mv "$CHECK_TYPST_TESTS_PATH" "$CHECK_TYPST_TESTS_PATH.bak"
        fi
    fi

    if [ -z "$XDG_SESSION_TYPE" ]; then
        echo "PKGBUILD NOTE: Headless session found, disabling opengl tests"

        find "$CHECK_OPENGL_TESTS_PATH" -type f | while read file;
        do
            mv "$file" "$file.bak"
        done
    fi
}

# The pyproject.toml file declares some flags that pytest doesn't understand.
# Some tests read importlib.metadata, and the checkhealth test needs the manim
# executable on PATH, so we need to run the suite against the built wheel rather
# than the bare source tree
#
# ECHOES: the testdir path
__patch_tests() {
    cd "$srcdir/$pkgname-$pkgver"

    testdir="$srcdir/test_install"
    rm -rf "$testdir"
    python -m installer --destdir="$testdir" dist/*.whl

    # Remove unrecognised pytest args
    sed -i 's/-n auto --dist=loadfile//' pyproject.toml

    echo "$testdir"
}

# In headless systems, we need to use xvfb-run so most tests don't fail from
# not having access to graphical apis.
#
# ECHOES: the command to use to run pytest, use unquoted
__pytest_cmd() {
    if [ -z "$XDG_SESSION_TYPE" ]; then
        echo "xvfb-run pytest"
    else
        echo "pytest"
    fi
}

# If the user doesn't have typst insalled, we restore the typst test files to
# their original location. Since we check whether the user has python-typst
# installed once before backing up the file, there are no possible race
# conditions here, even if the user installs python-typst while the tests run.
__restore_test_files() {
    has_python_typst="$1"
    headless_failing_tests_paths="$2"

    cd "$srcdir/$pkgname-$pkgver"

    if [ -z "$has_python_typst" ]; then
        echo "PKGBUILD NOTE: Restoring typest test file"
        mv "$CHECK_TYPST_TESTS_PATH.bak" "$CHECK_TYPST_TESTS_PATH"
    fi

    if [ -z "$XDG_SESSION_TYPE" ]; then
        echo "PKGBUILD NOTE: Restoring headless-disabled tests"

        find "$CHECK_OPENGL_TESTS_PATH" -type f -name "*.bak" | while read file;
        do
            mv "$file" "$(echo "$file" | sed 's/\.bak$//')"
        done
    fi
}

# ECHOES: the path to the current python installation's site-packages directory
__site_packages_path() {
    python -c 'import sysconfig; print(sysconfig.get_path("purelib").lstrip("/"))'
}

# Suppress failing tests:
# In headless chroots, some tests fail that don't in normal environments. This
# function builds a list of tests to suppress in that case
#
# ECHOES: The list of suppressed tests to be used with `pytest -k`
__suppress_tests() {
    suppressed_tests=""

    if [ -z "$XDG_SESSION_TYPE" ]; then
        for sup_test in \
            "Circle" \
            "animate_with_changed_custom_attribute" \
            "dash_as_filename" \
            "images_are_created_when_png_format_set_for_opengl" \
            "images_are_zero_padded_when_zero_pad_set_for_opengl" \
            "s_flag_opengl_renderer" \
            "write_to_movie_disables_window";
        do
            suppressed_tests="$suppressed_tests and not test_$sup_test"
        done
    fi

    suppressed_tests="$(echo "$suppressed_tests" | sed 's/^ and //')"
    echo "$suppressed_tests"
}

# ECHOES: the user's PATH with the testdir's binary directory prepended
__testdir_path() {
    testdir="$1"
    echo "$testdir/usr/bin:$PATH"
}
