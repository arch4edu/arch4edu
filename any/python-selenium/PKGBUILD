# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

pkgname=python-selenium
pkgver=4.26.1
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
  "${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/selenium-${pkgver}-python.tar.gz"
  "0001-fix-selenium-manager-build.patch"
)
sha256sums=('0e1ee5e523825a19e440b8bf91509139586767c1723af37b89685c121656fedb'
            'af031d7fd32bb4b8216d8b16957e2102b4f319ae22d94460636db90947d2d6ba')

_archive="selenium-selenium-${pkgver}-python"

prepare() {
  cd "${_archive}"
  patch -Np1 -i "${srcdir}/0001-fix-selenium-manager-build.patch"

  cd "../${_archive}/rust"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "${_archive}/py"
  export RUSTUP_TOOLCHAIN=stable
  python -m build --wheel --no-isolation
}

check() {
  cd "${_archive}/py"
  pytest
}

package() {
  cd "${_archive}/py"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
