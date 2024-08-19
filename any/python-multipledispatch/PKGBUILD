# Maintainer: Michael Schubert <mschu.dev at gmail> github.com/mschubert/PKGBUILDs
# Contributor: Gaël Donval <gdonval+aur at google mail>
pkgname=python-multipledispatch
_name=${pkgname#python-}
pkgver=1.0.0
pkgrel=4
pkgdesc='Multiple dispatch implementation in Python'
arch=('any')
url='https://github.com/mrocklin/multipledispatch'
license=('BSD-3-Clause')
makedepends=(python-build python-installer python-wheel python-setuptools)
depends=(python)
source=(multipledispatch-$pkgver.tar.gz::https://github.com/mrocklin/multipledispatch/archive/$pkgver.tar.gz)
sha256sums=('a9eb21390e5051ce28b2ee7acd02bb21885b9e2a4ce6e5fdbb1f338b48b54203')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -D -m644 LICENSE* "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
  install -D -m644 README* "$pkgdir"/usr/share/doc/$pkgname/README
}
