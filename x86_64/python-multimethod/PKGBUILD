# Maintainer: Jakub Klinkovský <lahwaacz at archlinux dot org>
# Contributor: Butui Hu <hot123tea123@gmail.com>

_name=multimethod
pkgname=python-multimethod
pkgver=2.0.2
pkgrel=1
epoch=1
pkgdesc='Multiple argument dispatching'
arch=(any)
url='https://github.com/coady/multimethod'
license=(Apache-2.0)
depends=(
  python
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(
  python-pytest
)
source=($_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('57f804f0bc2171b20b9e5840e5f7da5f72dd3b476a38b1cb84dc7bbd2914bfe1e7265ef76a1429338c4e55e0479edb2720f3c813acb22c930469a86076065f2b')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd $_name-$pkgver
  pytest -vv
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
