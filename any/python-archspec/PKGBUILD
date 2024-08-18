# Maintainer: arielzn <arielzn at riseup.net>

pkgbase='python-archspec'
pkgname=('python-archspec')
_module='archspec'
pkgver='0.2.4'
pkgrel=1
pkgdesc="A library for detecting, labeling, and reasoning about microarchitectures"
url="https://github.com/archspec/archspec"
depends=('python')
makedepends=('python-poetry')
license=('MIT')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-$pkgver.tar.gz")
sha256sums=('eabbae22f315d24cc2ce786a092478ec8e245208c9877fb213c2172a6ecb9302')


build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python -m build -wn
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python -m installer -d "$pkgdir" dist/*.whl
}
