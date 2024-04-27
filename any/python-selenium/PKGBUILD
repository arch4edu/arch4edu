# Maintainer:  Carl Smedstad <carl.smedstad at protonmail dot com>
# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pyname=selenium
_suffix=-python
pkgname=python-$_pyname
pkgver=4.20.0
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(any)
url="https://github.com/SeleniumHQ/selenium"
license=(Apache-2.0)
depends=(python python-urllib3 python-certifi python-trio
         python-trio-websocket python-typing_extensions)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=("$url/archive/${_pyname}-${pkgver}.tar.gz")
sha256sums=('8e06c1dc0de53cbd13edd613579542ae8d66d907befcda8b8025421dc914212e')

prepare() {
  cd "${_pyname}-${_pyname}-${pkgver}/py"
  cp ../rb/lib/$_pyname/webdriver/atoms/* $_pyname/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > \
    $_pyname/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "${_pyname}-${_pyname}-${pkgver}/py"
  python -m build \
    --wheel \
    --no-isolation
}

check() {
  cd "${_pyname}-${_pyname}-${pkgver}/py"

  pytest
}

package() {
  cd "${_pyname}-${_pyname}-${pkgver}/py"
  python -m installer \
    --destdir="$pkgdir" \
    dist/*.whl
}
