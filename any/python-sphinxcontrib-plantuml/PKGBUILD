pkgname=python-sphinxcontrib-plantuml
_pyname=sphinxcontrib-plantuml
pkgver=0.29
pkgrel=1
arch=(any)
pkgdesc="Sphinx 'plantuml' extension"
url='https://pypi.python.org/pypi/sphinxcontrib-plantuml'
license=('BSD')
makedepends=(python-setuptools)
depends=('plantuml' 'python-sphinx')
source=("https://files.pythonhosted.org/packages/source/s/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('97a4f2a26af91db88770ccf8a3b2e03305bcda7ec41a7f969fc8cb27b84a3c44')

build() {
  cd $_pyname-$pkgver
  python setup.py build
}

package() {
  cd $_pyname-${pkgver}
  python setup.py install --root="$pkgdir" --optimize=1
}
