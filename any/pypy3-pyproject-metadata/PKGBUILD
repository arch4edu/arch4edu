# Maintainer: Maks Verver <maks@verver.ch>

pkgname=pypy3-pyproject-metadata
_name="${pkgname#pypy3-}"
pkgver=0.9.0
pkgrel=1
pkgdesc='PEP 621 metadata parsing'
arch=(any)
url='https://github.com/pypa/python-pyproject-metadata'
license=(MIT)
depends=(pypy3 pypy3-packaging)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=($url/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('ef79e6549c9aeb644a188910ecaac56bf1cf7c4326f4bb1f1e07514eef0f56966e8eaabfe791f82f488810428a4840a7970a1ddf7a80056c630d5f91e85911a1')

build() {
  cd $_name-$pkgver

  pypy3 -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver

  pypy3 -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm 644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
