# Maintainer: Harriet O'Brien <harrietobrien@protonmail.com>
# Maintainer: Letu Ren <fantasquex@gmail.com>

pkgname=python-etuples
_pkgname=etuples
pkgver=0.3.9
pkgrel=1
pkgdesc="Python S-expression emulation using tuple-like objects."
arch=('any')
url="https://github.com/pythological/${_pkgname}/"
license=('APACHE')
depends=(
    'python-cons'
    'python-multipledispatch'
)
makedepends=(
    'python-setuptools'
)
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('5295b9a6089e3dd25b1773a8f9e1220873dbc9eb9b7232ac7a96511d6c44a128')

build() {
    cd "${_pkgname}-${pkgver}"
    python setup.py build
}

package() {
    cd "${_pkgname}-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}

