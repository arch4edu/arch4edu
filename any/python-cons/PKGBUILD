# Maintainer: Harriet O'Brien <harrietobrien@protonmail.com>
# Contributor: Letu Ren <fantasquex@gmail.com>

pkgname=python-cons
_pkgname=cons
pkgver=0.4.6
pkgrel=1
pkgdesc="An implementation of Lisp/Scheme-like cons in Python"
arch=('any')
url="https://github.com/pythological/python-cons/"
license=('LGPL3')
depends=(
    'python-logical-unification'
)
makedepends=(
    'python-setuptools'
)
source=("https://github.com/pythological/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('86f7729f8c9eb47392b94799d94da6f036847702956c26abc85d070f7dd54cc8')

build() {
    cd "${pkgname}-${pkgver}"
    python setup.py build
}

package() {
    cd "${pkgname}-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}

