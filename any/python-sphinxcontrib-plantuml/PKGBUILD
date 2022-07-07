pkgname=python-sphinxcontrib-plantuml
_pyname=sphinxcontrib-plantuml
pkgver=0.24
pkgrel=1
arch=(any)
pkgdesc="Sphinx 'plantuml' extension"
url='https://pypi.python.org/pypi/sphinxcontrib-plantuml'
license=('BSD')
makedepends=(python-setuptools)
depends=('plantuml' 'python-sphinx')
source=("https://files.pythonhosted.org/packages/source/s/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('cf65db7358f785a6498ee03e7198b6680c625d28e55b33475fc3f6c94351451d')

build() {
  cd $_pyname-$pkgver
  python setup.py build
}

package() {
  cd $_pyname-${pkgver}
  python setup.py install --root="$pkgdir" --optimize=1
}
