# Maintainer: Letu Ren <fantasquex@gmail.com>

pkgname=python-minikanren
_pkgname=miniKanren
pkgver=1.0.3
pkgrel=1
pkgdesc="An extensible, lightweight relational/logic programming DSL written in pure Python"
arch=('any')
url="https://github.com/pythological/kanren/"
license=('custom')
depends=(
    'python-toolz'
    'python-cons'
    'python-multipledispatch'
    'python-etuples'
    'python-logical-unification'
)
makedepends=(
    'python-setuptools'
)
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('1ec8bdb01144ad5e8752c7c297fb8a122db920f859276d25a72d164e998d7f6e')

build() {
    cd "${_pkgname}-${pkgver}"
    python setup.py build
}

package() {
    cd "${_pkgname}-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

