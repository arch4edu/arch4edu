# Maintainer:  Carl Smedstad <carl.smedstad at protonmail dot com>
# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pyname=selenium
_suffix=-python
pkgname=python-$_pyname
pkgver=4.17.2
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(any)
url="https://www.selenium.dev"
license=(Apache)
depends=(python python-urllib3 python-certifi python-trio
         python-trio-websocket)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=("https://github.com/SeleniumHQ/${_pyname}/archive/refs/tags/${_pyname}-${pkgver}${_suffix}.tar.gz")
sha256sums=('ba9222c983fa34eb03b8847515bf0c170bf12e89ad291e859e0bf05f183e540a')
options=(!makeflags)

prepare() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${_suffix}/py"
  cp ../rb/lib/$_pyname/webdriver/atoms/* $_pyname/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > \
    $_pyname/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${_suffix}/py"
  python -m build \
    --wheel \
    --no-isolation \
    --skip-dependency-check
}

check() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${_suffix}/py"

  python -m pytest
}

package() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${_suffix}/py"
  python -m installer \
    --destdir="$pkgdir" \
    --compile-bytecode=2 \
    dist/*.whl
}
