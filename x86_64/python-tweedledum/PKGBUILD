# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=tweedledum
pkgname=python-${_pkgname}
pkgver=1.1.1
pkgrel=3
pkgdesc="A library for synthesizing and manipulating quantum circuits"
arch=('x86_64')
url="https://github.com/boschmitt/tweedledum"
license=('MIT')
depends=('gcc-libs')
makedepends=(
    'cmake'
    'ninja'
    'nlohmann-json'
    'python-scikit-build'
    'python-setuptools'
)
source=(
    "${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz"
    "fix-build.patch::https://github.com/boschmitt/tweedledum/pull/170.patch"
    "pybind11.tar.gz::https://github.com/pybind/pybind11/archive/refs/tags/v2.10.4.tar.gz"
)
b2sums=(
    '99da09829a70a316fdc582929bfe8ca5d805f0a7a6f049da3951c57c5e4bec24343a1021020e8d00791683ab5c140647d78ee0dde5dac95370b648e0eee44b04'
    '24cb2303a6d3fdac0967c6c925bb49113cc317aa03524b024e9131180bdcd7f6dd812d0e2ebfe157f0331e366b0284c972cc1b2b780960af38365c7d70fa078c'
    '7b2d86e8262581b2cc6dd720b83336206e242ef8ca99b257b01a11141ed8b127d7f35d7d573bc763dd36f2fe8c8ac91766089deb63a76e9c10029c34eec2d6d3'
)

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    # Fixes https://github.com/boschmitt/tweedledum/issues/169
    patch --forward --strip=1 --input="${srcdir}/fix-build.patch"

    # Update external/pybind11 to a recent version
    # https://github.com/boschmitt/tweedledum/issues/181
    cd external
    rm -r pybind11
    mv "${srcdir}/pybind11-2.10.4" pybind11

    # Fix for gcc 13
    cd "${srcdir}/${_pkgname}-${pkgver}"
    cd include/tweedledum/IR
    sed -i '6s/.*/#include <cstdint>/' Cbit.h
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python setup.py install --root="${pkgdir}/" --optimize=1 --skip-build
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
