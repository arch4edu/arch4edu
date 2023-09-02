# Maintainer:  Carl Smedstad <carl.smedstad at protonmail dot com>
# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pyname=selenium
pkgname=python-$_pyname
pkgver=4.12.0
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(any)
url="https://www.selenium.dev"
license=(Apache)
depends=(python python-urllib3 python-certifi python-trio
         python-trio-websocket)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=("https://github.com/SeleniumHQ/${_pyname}/archive/refs/tags/${_pyname}-${pkgver}.tar.gz")
sha256sums=('b69cd3e99682d2030db53ed8274e746a30a4689609ca92b4d49098fb4c612f71')
options=(!makeflags)

prepare() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}/py"
  cp ../rb/lib/$_pyname/webdriver/atoms/* $_pyname/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > \
    $_pyname/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}/py"
  python -m build \
    --wheel \
    --no-isolation \
    --skip-dependency-check
}

check() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}/py"

  python -m pytest
}

package() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}/py"
  python -m installer \
    --destdir="$pkgdir" \
    --compile-bytecode=2 \
    dist/*.whl
}
