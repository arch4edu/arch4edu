# Maintainer:
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Sam L. Yes <samlukeyes123@gmail.com>

_pkgname="python-retry"
pkgname="$_pkgname"
pkgver=0.9.5
pkgrel=1
pkgdesc="Easy to use retry decorator"
url="https://github.com/eSAMTrade/retry"
license=('Apache-2.0')
arch=('any')

depends=('python')
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
checkdepends=('python-pytest')
optdepends=(
  'python-decorator: preserves function signatures'
)

_pkgsrc="retry-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"$url/archive/$pkgver.$_pkgext")
sha256sums=('1538899bb054de81782622f041aedc928c87f253db8167574d70406d913ecac9')

prepare() {
  install -Dm644 /dev/stdin "$_pkgsrc/setup.py" << END
from setuptools import find_packages, setup
setup(packages=find_packages(exclude=('tests')))
END
}

build() {
  cd "$_pkgsrc"
  python -m build --wheel --no-isolation
}

check() {
  cd "$_pkgsrc"
  PYTHONPATH="$PWD" pytest -x --disable-warnings
}

package() {
  cd "$_pkgsrc"
  python -m installer --destdir="$pkgdir/" dist/*.whl
  install -Dm644 README.rst -t "$pkgdir/usr/share/doc/$pkgname/"
}
