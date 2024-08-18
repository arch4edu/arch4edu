# Maintainer: Evan Edwards <evan@ejedev.com>

pkgname=python-boltons
pkgver=24.0.0
_commit=992a58c1036fcf4d52cbf3313b6217b7c07b11d9
pkgrel=1
pkgdesc="Functionality that should be in the standard library. Like builtins, but Boltons."
url="https://github.com/mahmoud/boltons"
license=('BSD')
arch=('any')
depends=('python')
makedepends=('git' 'python-setuptools')
checkdepends=('python-pytest')
source=("git+https://github.com/mahmoud/boltons.git#commit=$_commit")
sha512sums=('SKIP')

build() {
  cd boltons
  python setup.py build
}

check() {
  cd boltons
  pytest
}

package() {
  cd boltons
  python setup.py install --root="$pkgdir" --optimize=1

  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
