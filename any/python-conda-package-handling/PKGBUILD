# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
_name=${pkgname#python-}
pkgver=1.8.1
pkgrel=1
pkgdesc="Create and extract conda package of various formats"
arch=('any')
url="https://github.com/conda/conda-package-handling"
license=('BSD')
depends=(
  'python'
  'python-six'
  'python-tqdm'
  'libarchive'
  'python-libarchive-c'
)
makedepends=(
  'python-setuptools'
  'cython'
)
options=(!emptydirs)
install=
source=($_name-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz)
sha512sums=('97e74d39ccc7dc1cd38c71c874a1fbf8ea49ac14d5628e5114748578b48d602a9a9d9af6f566857823e00767c96c66d6960c7748322645c37ef0d02e43250201')

build() {
  cd "$srcdir/${_name}-$pkgver"
  sed -i 's/archive_and_deps/archive/' setup.py
  python setup.py clean --all
  python setup.py build
}

package() {
  cd "$srcdir/${_name}-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
