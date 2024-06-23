# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

pkgname=python-selenium
_pkgname=${pkgname#python-}
pkgver=4.22.0
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(any)
url="https://github.com/SeleniumHQ/selenium"
license=(Apache-2.0)
depends=(
  python
  python-certifi
  python-trio
  python-trio-websocket
  python-typing_extensions
  python-urllib3
  python-websocket-client
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(python-pytest)
source=("$pkgname-$pkgver.tar.gz::$url/archive/selenium-$pkgver.tar.gz")
sha256sums=('196c7080449c48a46fab64dce0fb0085f7c2276d359d49ef1fad51203c853152')

_archive="$_pkgname-selenium-$pkgver/py"

prepare() {
  cd "$_archive"

  cp ../rb/lib/selenium/webdriver/atoms/* selenium/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > \
    selenium/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "$_archive"

  python -m build --wheel --no-isolation
}

check() {
  cd "$_archive"

  pytest
}

package() {
  cd "$_archive"

  python -m installer --destdir="$pkgdir" dist/*.whl
}
