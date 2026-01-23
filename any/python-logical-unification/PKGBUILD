# Maintainer: Harriet O'Brien <harrietobrien@protonmail.com>
# Contributor: Letu Ren <fantasquex@gmail.com>

pkgname=python-logical-unification
_pkgname=logical-unification
_name=unification
pkgver=0.4.6
pkgrel=1
pkgdesc="Straightforward unification in Python; extensible via generic functions."
arch=('any')
url="https://github.com/pythological/unification/"
license=('custom')
depends=(
    'python-toolz'
)
makedepends=(
    'python-setuptools'
)

source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('dab8da68a5753232416637913af5b914e293d2187b5b4fe43a11331ffe15d776')

build() {
    cd "${_name}-${pkgver}"
    python setup.py build
}

package() {
    cd "${_name}-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

