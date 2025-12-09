# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=glcontext

pkgname=python-glcontext
pkgver=3.0.0
pkgrel=1
pkgdesc="A library providing OpenGL implementation for ModernGL on multiple platforms."

arch=("any")
license=("MIT")
url="https://github.com/moderngl/glcontext"

source=("$url/archive/refs/tags/$pkgver.tar.gz")
sha512sums=('dc38b4f019d939c619d0981468f84fae72d8958a3e139901ba0866a6c0e6ffa35f566fcd0061cd9ad89dd20881ab9b84da8e9913c1944f70565457775e90bc26')

depends=(
    "python"
    "libx11" # Required to build, even on a Wayland session
    "libglvnd"
)
optdepends=(
    "egl-wayland: Run on Wayland session"
)
makedepends=(
    "python-build"
    "python-installer"
    "python-setuptools"
    "python-wheel"
)
checkdepends=(
    "python-pytest"
    "python-psutil"
)

build () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m build --wheel --no-isolation
}

check () {
    cd "$srcdir/$_name-$pkgver"

    if [ -z "$XDG_SESSION_TYPE" ]; then
        echo "Tests don't work on headless sessions. Skipping..."
        return
    fi

    cd "$srcdir/$_name-$pkgver"
    python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
    PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" pytest
}

package () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
