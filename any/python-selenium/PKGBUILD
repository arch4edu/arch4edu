# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pyname=selenium
_suffix='-python'
pkgname=python-$_pyname
pkgver=4.11.2
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(any)
url="https://www.selenium.dev"
license=(Apache)
depends=(python-urllib3 python-certifi python-debugpy python-multidict
         python-importlib-metadata python-trio-websocket
         python-inflection python-typing_extensions geckodriver)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=(https://github.com/SeleniumHQ/${_pyname}/archive/refs/tags/${_pyname}-${pkgver}${_suffix}.tar.gz
        test_ie_options.patch)
sha256sums=('6a4ba80c986e01a3586a10c7b687ac9f5bd16100044e6975a18dea5cb313db9c'
            '51ff4f8fc0292cda16b4ed8fd62f8c2d60226d76b35c84ed026790a95d91c757')
options=(!makeflags)

prepare() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${_suffix}/py"
  patch -p2 < "$srcdir/test_ie_options.patch"
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

  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl

  test-env/bin/python -m pytest -v
}

package() {
  cd "${srcdir}/${_pyname}-${_pyname}-${pkgver}${_suffix}/py"
  python -m installer \
    --destdir="$pkgdir" \
    --compile-bytecode=2 \
    dist/*.whl
}
