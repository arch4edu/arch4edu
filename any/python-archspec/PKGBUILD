# Maintainer: arielzn <arielzn at riseup dot net>

pkgbase='python-archspec'
pkgname=('python-archspec')
_module='archspec'
pkgver='0.2.5'
pkgrel=4
pkgdesc="A library for detecting, labeling, and reasoning about microarchitectures"
url="https://github.com/archspec/archspec"
depends=('python')
makedepends=(
  'python-build'
  'python-installer'
  'python-poetry-core'
)
license=('MIT')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-$pkgver.tar.gz")
sha256sums=('5bec8dfc5366ff299071200466dc9572d56db4e43abca3c66bdd62bc2b731a2a')


build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python -m build -wn
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python -m installer -d "$pkgdir" dist/*.whl

    install -Dm644  LICENSE-MIT "$pkgdir/usr/share/licenses/$pkgname/LICENSE-MIT"
    install -Dm644  LICENSE-APACHE "$pkgdir/usr/share/licenses/$pkgname/LICENSE-APACHE"
}

