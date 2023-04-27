# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pkgname=selenium
_suffix=''
pkgname=python-$_pkgname
pkgver=4.9.0
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=('any')
url="https://www.selenium.dev"
license=('Apache')
depends=('python-urllib3' 'python-certifi' 'python-debugpy' 'python-multidict'
         'python-importlib-metadata' 'python-trio-websocket'
         'python-inflection' 'geckodriver')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://github.com/SeleniumHQ/${_pkgname}/archive/refs/tags/${_pkgname}-${pkgver}${suffix}.tar.gz")
sha256sums=('a8bafe09fb0d6eb1b3bbc08d4baf0c2de230ca2f0834a17598610d59059eac66')
options=(!makeflags)

prepare() {
  cd "${srcdir}/${_pkgname}-${_pkgname}-${pkgver}${suffix}/py"
  cp ../rb/lib/$_pkgname/webdriver/atoms/* $_pkgname/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > \
    $_pkgname/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "${srcdir}/${_pkgname}-${_pkgname}-${pkgver}${suffix}/py"
  python setup.py build
}

check() {
  cd "${srcdir}/${_pkgname}-${_pkgname}-${pkgver}${suffix}/py"
  pytest
}

package() {
  cd "${srcdir}/${_pkgname}-${_pkgname}-${pkgver}${suffix}/py"
  python setup.py install \
    --prefix=/usr         \
    --root="$pkgdir"      \
    --optimize=1          \
    --skip-build
}
