# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC1091,SC2034,SC2154,SC2164

_name=mapbox_earcut_python

pkgname=python-mapbox-earcut
pkgver=1.0.3
pkgrel=3
pkgdesc="Python bindings for the C++ implementation of the Mapbox Earcut library."

arch=("x86_64")
license=("ISC")
url="https://github.com/skogler/mapbox_earcut_python"

source=("$url/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('3700a25de44e73edd762b5cfa0c43fa73ebbf95f811694bfc8bb77f07dc9512c3fb814b409b5ea88c9e1a32cc5272f3ae33c1e4e323afe8b139cf8b96f1edc54')

depends=(
    "gcc-libs"
    "glibc"
    "python"
)
makedepends=(
    "pybind11"
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

build () {
    cd "$srcdir/$_name-$pkgver"
    python -m build --wheel --no-isolation
}

check () {
    cd "$srcdir/$_name-$pkgver"

    python -m venv --system-site-packages venv
    source venv/bin/activate
    pip install ./dist/*.whl
    python -m pytest
    rm -rf venv
}

package () {
    cd "$srcdir/$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
