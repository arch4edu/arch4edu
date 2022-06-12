# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
_name=${pkgname#python-}
pkgver=1.7.3
pkgrel=2
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
sha512sums=('f3c3bd07ba2b725594447913029c2323c498960678888615d452abbe1e779ba3cfb9a2cbe7ea2c93aa4f0356258a3ff2be24034963aae74c348b7ad01aaa403d')

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
