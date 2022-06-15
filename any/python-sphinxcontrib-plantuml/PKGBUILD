pkgname=python-sphinxcontrib-plantuml
_pyname=sphinxcontrib-plantuml
pkgver=0.23
pkgrel=1
arch=(any)
pkgdesc="Sphinx 'plantuml' extension"
url='https://pypi.python.org/pypi/sphinxcontrib-plantuml'
license=('BSD')
makedepends=(python-setuptools)
depends=('plantuml' 'python-sphinx')
source=("https://files.pythonhosted.org/packages/source/s/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('1d55518f0a86ecd6c96ba8ff8c884adca05bac3e58e76a692a3cd19aa7f42acf')

build() {
  cd $_pyname-$pkgver
  python setup.py build
}

package() {
  cd $_pyname-${pkgver}
  python setup.py install --root="$pkgdir" --optimize=1
}
