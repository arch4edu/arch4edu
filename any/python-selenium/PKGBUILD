# Maintainer:  Carl Smedstad <carl.smedstad at protonmail dot com>
# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pyname=selenium
_suffix=-python
pkgname=python-$_pyname
pkgver=4.18.1
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
sha256sums=('6e5c8903253f9541bc839e3e31f99680d8ceb202b2b6d75ebe51e95f348ee1c5')
options=(!makeflags)

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
    --no-isolation \
    --skip-dependency-check
}

check() {
  cd "${_pyname}-${_pyname}-${pkgver}/py"

  python -m pytest
}

package() {
  cd "${_pyname}-${_pyname}-${pkgver}/py"
  python -m installer \
    --destdir="$pkgdir" \
    --compile-bytecode=2 \
    dist/*.whl
}
