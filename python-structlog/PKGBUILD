# Maintainer: 71e6fd52 <DAStudio.71e6fd52@gmail.com>
pkgbase=('python-structlog')
pkgname=('python-structlog')
_module='structlog'
pkgver='18.1.0'
pkgrel=1
pkgdesc="Structured Logging for Python"
url="http://www.structlog.org/"
depends=('python')
makedepends=('python-setuptools')
license=('Apache' 'MIT')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/s/structlog/structlog-${pkgver}.tar.gz")
md5sums=('9a6cbd3dc2f1ccd5519d876eddaf692a')

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
    install -Dm644 LICENSE.apache2 "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.apache2
    install -Dm644 LICENSE.mit "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.mit
}
