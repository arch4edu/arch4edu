pkgname=python-sphinxcontrib-plantuml
_pyname=sphinxcontrib-plantuml
pkgver=0.31
pkgrel=1
arch=(any)
pkgdesc="Sphinx 'plantuml' extension"
url='https://pypi.python.org/pypi/sphinxcontrib-plantuml'
license=('BSD')
makedepends=(python-build python-installer python-wheel python-setuptools)
depends=('plantuml' 'python-sphinx')
source=("https://files.pythonhosted.org/packages/source/s/${_pyname//-/_}/${_pyname//-/_}-${pkgver}.tar.gz")
sha256sums=('fd74752f8ea070e641c3f8a402fccfa1d4a4056e0967b56033d2a76282d9f956')

build() {
  cd "${_pyname//-/_}-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pyname//-/_}-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
