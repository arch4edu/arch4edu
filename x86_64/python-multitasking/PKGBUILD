# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=multitasking
pkgname=python-multitasking
pkgver=0.0.11
pkgrel=2
pkgdesc="Non-blocking Python methods using decorators"
arch=('any')
url="https://github.com/ranaroussi/multitasking"
license=('Apache')
depends=('python')
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
b2sums=('eab1376111fb5b4d9b77079842a02aeee6804ab75bbbdd2bebe7ad3bd2a9eb8e12d59701be37d26195bd61dbc6c9928599693e735c32168d95486d8ffcdc889b')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
