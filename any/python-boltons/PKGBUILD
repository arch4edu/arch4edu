# Maintainer: Evan Edwards <evan@ejedev.com>
# Co-maintainer: stickynotememo <samk26633@gmail.com>

pkgname=python-boltons
pkgver=26.1.0
_commit=1d525271754ed7aea7f2347ed16ddbcedb1097a3
pkgrel=1
pkgdesc="Functionality that should be in the standard library. Like builtins, but Boltons."
url="https://github.com/mahmoud/boltons"
license=('BSD-3-Clause')
arch=('any')
depends=('python')
makedepends=('uv' 'git' 'python-installer')
checkdepends=('python-pytest')
source=("git+https://github.com/mahmoud/boltons.git#commit=$_commit")
sha512sums=('SKIP')

prepare() {
  cd boltons
}

build() {
  cd boltons
  uv build
}

check() {
  cd boltons
  python -m pytest
}

package() {
  cd boltons
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
