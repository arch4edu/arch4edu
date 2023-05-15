# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pyname=selenium
_suffix=''
pkgname=python-$_pyname
pkgver=4.9.1
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
sha256sums=('f6a11c5ac8e00e94e14e2232ea89d1b07d0334871cc5890df0a5fd50f511f09e')
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
    --compile-bytecode=1 \
    dist/*.whl
}
