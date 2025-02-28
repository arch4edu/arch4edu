# Maintainer: Evan Edwards <evan@ejedev.com>

pkgname=python-boltons
pkgver=25.0.0
_commit=c23dbdadb6fecdf505eb4231559561913b84c13f
pkgrel=2
pkgdesc="Functionality that should be in the standard library. Like builtins, but Boltons."
url="https://github.com/mahmoud/boltons"
license=('BSD-3-Clause')
arch=('any')
depends=('python')
makedepends=('git' 'python-flit' 'python-installer')
checkdepends=('python-pytest')
source=("git+https://github.com/mahmoud/boltons.git#commit=$_commit")
sha512sums=('SKIP')

build() {
  cd boltons
  python -m flit build
}

check() {
  cd boltons
  pytest
}

package() {
  cd boltons
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
