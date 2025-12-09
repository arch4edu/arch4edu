# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=isosurfaces

pkgname=python-isosurfaces
pkgver=0.1.2
pkgrel=1
pkgdesc="Construct isolines/isosurfaces of a 2D/3D scalar field defined by a function."

arch=("any")
license=("MIT")
url="https://github.com/jared-hughes/isosurfaces"

source=("$url/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('b7c1f7c33d443ff45f15d552dc36e47de762e0c09755f378285126f9acd9fdc5fe55cef9a2218f3966a83046a8646faaa97590f9bd2c79e6c31a0712b61c905c')

depends=(
    "python"
    "python-numpy"
)
makedepends=(
    "python-build"
    "python-installer"
    "python-setuptools"
    "python-wheel"
)

build () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m build --wheel --no-isolation
}

package () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
