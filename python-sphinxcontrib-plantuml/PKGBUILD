pkgbase=python-sphinxcontrib-plantuml
pkgname=(python-sphinxcontrib-plantuml python2-sphinxcontrib-plantuml)
_pyname=sphinxcontrib-plantuml
pkgver=0.8.2
pkgrel=1
arch=(any)
pkgdesc="Sphinx 'plantuml' extension"
url='https://pypi.python.org/pypi/sphinxcontrib-plantuml'
license=('BSD')
makedepends=(python-setuptools python2-setuptools)
source=("https://files.pythonhosted.org/packages/source/s/${_pyname}/${_pyname}-${pkgver}.tar.gz")

build() {
  cp -r $_pyname-$pkgver $_pyname-$pkgver-py2

  cd $_pyname-$pkgver
  python setup.py build

  cd "$srcdir"/$_pyname-$pkgver-py2
  python2 setup.py build
}

package_python-sphinxcontrib-plantuml() {
  depends=('plantuml' 'python-sphinx')
  cd $_pyname-${pkgver}
  python setup.py install --root="$pkgdir" --optimize=1
}

package_python2-sphinxcontrib-plantuml() {
  depends=('plantuml' 'python2-sphinx')
  cd $_pyname-${pkgver}-py2
  python2 setup.py install --root="$pkgdir" --optimize=1
}

sha256sums=('88e6995521ff5a567346c60c6ce580296ab2d67029a24353bb72ab6381cb2a96')
