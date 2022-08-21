# Maintainer:  Anton Kudelin <kudelin at protonmail dot com>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

_pkgname=selenium
pkgname=python-$_pkgname
pkgver=4.4.2
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
source=("https://github.com/SeleniumHQ/$_pkgname/archive/refs/tags/$_pkgname-$pkgver-python.tar.gz")
sha256sums=('bd6c54419e0f3b22cb095920123ce9992cc66ffa5fc60d7383d7c2001fda47b8')
options=(!makeflags)

prepare() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver-python/py"
  cp ../rb/lib/$_pkgname/webdriver/atoms/* $_pkgname/webdriver/remote
  echo '{"frozen":{},"mutable":{}}' > $_pkgname/webdriver/firefox/webdriver_prefs.json
}

build() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver-python/py"
  python setup.py build
}

check() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver-python/py"
  pytest
}

package() {
  cd "$srcdir/$_pkgname-$_pkgname-$pkgver-python/py"
  python setup.py install --prefix=/usr --root="$pkgdir" -O1 --skip-build
}
