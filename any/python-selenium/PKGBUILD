# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pyname=selenium
_suffix=''
pkgname=python-$_pyname
pkgver=4.10.0
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(any)
url="https://www.selenium.dev"
license=(Apache)
depends=(python-urllib3 python-certifi python-debugpy python-multidict
         python-importlib-metadata python-trio-websocket
         python-inflection geckodriver)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=(https://github.com/SeleniumHQ/${_pyname}/archive/refs/tags/${_pyname}-${pkgver}${suffix}.tar.gz)
sha256sums=('873f8071df2dd0c175216721e39072f8a9821119ac21b1ddb52a21f6a0ad442e')
options=(!makeflags)

prepare() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${suffix}/py"
  cp ../rb/lib/$_pyname/webdriver/atoms/* $_pyname/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > \
    $_pyname/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${suffix}/py"
  python -m build \
    --wheel \
    --no-isolation \
    --skip-dependency-check
}

check() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${suffix}/py"

  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl

  test-env/bin/python -m pytest -v
}

package() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${suffix}/py"
  python -m installer \
    --destdir="$pkgdir" \
    --compile-bytecode=2 \
    dist/*.whl
}
