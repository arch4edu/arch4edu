# Maintainer: Jakub Klinkovský <lahwaacz at archlinux dot org>
# Contributor: Butui Hu <hot123tea123@gmail.com>

_name=multimethod
pkgname=python-multimethod
pkgver=2.0
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
b2sums=('c9c732dab1e7fdf9c9da5d3049babbeac4b64f3b2b8a8587838d01769656bafb89852251fda3d7f4b4b6c588130b3c96efab156b5059ca7a740618273ee66318')

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
