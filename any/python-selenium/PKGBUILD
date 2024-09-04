# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

pkgname=python-selenium
pkgver=4.24.0
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(x86_64)
url="https://github.com/SeleniumHQ/selenium"
license=(Apache-2.0)
depends=(
  bzip2
  gcc-libs
  glibc
  python
  python-certifi
  python-trio
  python-trio-websocket
  python-typing_extensions
  python-urllib3
  python-websocket-client
  zlib
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-setuptools-rust
  python-wheel
)
checkdepends=(python-pytest)
options=(!lto)
source=(
  "$pkgname-$pkgver.tar.gz::$url/archive/selenium-$pkgver.tar.gz"
  "fix-selenium-manager-build.patch"
)
sha256sums=(
  '981015b21a120072c20f87f2a0bd8a677d65cf98464657cb0cf96094b1dd44a4'
  'af031d7fd32bb4b8216d8b16957e2102b4f319ae22d94460636db90947d2d6ba'
)

_archive="selenium-selenium-$pkgver"

prepare() {
  cd "$srcdir/$_archive"
  patch -Np1 -i "$srcdir/fix-selenium-manager-build.patch"

  cd "$srcdir/$_archive/rust"
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "$srcdir/$_archive/py"
  export RUSTUP_TOOLCHAIN=stable
  python -m build --wheel --no-isolation
}

check() {
  cd "$srcdir/$_archive/py"
  pytest
}

package() {
  cd "$srcdir/$_archive/py"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
