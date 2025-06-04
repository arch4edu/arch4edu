# Maintainer: Maks Verver <maks@verver.ch>

pkgname=pypy3-pyproject-metadata
_name="${pkgname#pypy3-}"
pkgver=0.9.1
pkgrel=1
pkgdesc='PEP 621 metadata parsing'
arch=(any)
url='https://github.com/pypa/python-pyproject-metadata'
license=(MIT)
depends=(pypy3 pypy3-packaging)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=($url/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('80afd47a8b33d6f756610ee317550435508f10b2eedac439c5e54ff0abf7bf02a36c75b60b264cc09ee21591cc10f714034c68745542df44227a8894253e8256')

build() {
  cd $_name-$pkgver

  pypy3 -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver

  pypy3 -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm 644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
