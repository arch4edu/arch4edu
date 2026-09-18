# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC1091,SC2034,SC2154,SC2164

_name=mapbox_earcut_python

pkgname=python-mapbox-earcut
pkgver=2.1.0
pkgrel=1
pkgdesc="Python bindings for the C++ implementation of the Mapbox Earcut library."

arch=("x86_64")
license=("ISC")
url="https://github.com/skogler/mapbox_earcut_python"

source=("$url/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('06566db5c3547a8e21763563f57e84c43bf3de669671e473b0d717ad5f8af82a1ae98c89e8b3ba8849199dde380ae6f9b90fc27c40045500cbb4b6c86945cd84')

depends=(
    "gcc-libs"
    "glibc"
    "python"
)
makedepends=(
    "nanobind"
    "python-build"
    "python-installer"
    "python-scikit-build-core"
    "python-setuptools"
    "python-wheel"
)
checkdepends=(
    "python-numpy"
    "python-pytest"
    "python-virtualenv"
)

build() {
    cd "$srcdir/$_name-$pkgver"
    python -m build --wheel
}

check() {
    cd "$srcdir/$_name-$pkgver"

    python -m venv --system-site-packages venv
    source venv/bin/activate
    pip install ./dist/*.whl

    (cd tests; python -m pytest)
    rm -rf venv
}

package() {
    cd "$srcdir/$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
