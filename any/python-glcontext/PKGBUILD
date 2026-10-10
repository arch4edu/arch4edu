# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=glcontext

pkgname=python-glcontext
pkgver=3.1.0
pkgrel=1
pkgdesc="A library providing OpenGL implementation for ModernGL on multiple platforms."

arch=("any")
license=("MIT")
url="https://github.com/moderngl/glcontext"

source=("$url/archive/refs/tags/$pkgver.tar.gz")
sha512sums=('05a7bab7360bc2d4a0177f1a2ca11feaa0b8e820ba7b8905bbd371620c6122ea8658a2cecf46690f2359791d1f1e0ae147e611c4e3a883a7d8b045d231f4d90f')

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
    "xorg-server-xvfb"
)

build () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m build --wheel --no-isolation
}

check () {
    cd "$srcdir/$_name-$pkgver"

    python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
    PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" xvfb-run pytest
}

package () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
