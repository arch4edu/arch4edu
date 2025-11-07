# Maintainer: Jakub Klinkovský <lahwaacz at archlinux dot org>
# Contributor: Butui Hu <hot123tea123@gmail.com>

_name=multimethod
pkgname=python-multimethod
pkgver=2.0.1
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
b2sums=('21e2fca48329723d8f56e0978151e1f22760b0b4775a1c6a116017a450e5e645929cf07ebd28c58821473f5f59154d4793a161a63df21d2032aae16aad91cab1')

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
