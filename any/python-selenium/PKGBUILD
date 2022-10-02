# Maintainer:  Anton Kudelin <kudelin at protonmail dot com>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pkgname=selenium
pkgname=python-$_pkgname
pkgver=4.5.0
pkgrel=1
pkgdesc="Python language bindings for Selenium WebDriver"
arch=('any')
url="https://www.selenium.dev"
license=('Apache')
depends=('python-urllib3' 'python-certifi' 'python-debugpy' 'python-inflection'
         'python-multidict' 'python-importlib-metadata' 'python-trio-websocket'
         'geckodriver')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://github.com/SeleniumHQ/$_pkgname/archive/refs/tags/$_pkgname-$pkgver.tar.gz")
sha256sums=('26a0e2b042de2fe066a1bfea17166eb18ff705735d90d2b0ab971a9343cacd83')
options=(!makeflags)

prepare() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver/py"
  cp ../rb/lib/$_pkgname/webdriver/atoms/* $_pkgname/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > $_pkgname/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver/py"
  python setup.py build
}

check() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver/py"
  pytest
}

package() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver/py"
  python setup.py install --prefix=/usr --root="$pkgdir" -O1 --skip-build
}
