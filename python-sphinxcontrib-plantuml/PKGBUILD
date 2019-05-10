pkgbase=python-sphinxcontrib-plantuml
pkgname=(python-sphinxcontrib-plantuml python2-sphinxcontrib-plantuml)
_pyname=sphinxcontrib-plantuml
pkgver=0.15
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

sha256sums=('ead8aef88db444ad034c18326b38ad6b3d07152dbe73132b1ff83ec4a332d41b')
