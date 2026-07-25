# Maintainer: robertfoster

_name=timeout-decorator
pkgname=python-${_name}
pkgver=0.5.0
pkgrel=2
pkgdesc="Timeout decorator for Python"
arch=('any')
depends=('python')
makedepends=(python-build python-installer python-setuptools python-wheel)
url="https://github.com/pnpnpn/timeout-decorator"
license=('MIT')
options=(!emptydirs)
source=("https://files.pythonhosted.org/packages/source/t/${_name}/${_name}-$pkgver.tar.gz")

build() {
  cd "$srcdir/${pkgname#python-}-$pkgver"

  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/${pkgname#python-}-$pkgver"

  python -m installer --destdir="$pkgdir" dist/*.whl
}

sha256sums=('6a2f2f58db1c5b24a2cc79de6345760377ad8bdc13813f5265f6c3e63d16b3d7')
