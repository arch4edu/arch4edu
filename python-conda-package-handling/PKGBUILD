# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
_name=${pkgname#python-}
pkgver=1.7.2
pkgrel=1
pkgdesc="Create and extract conda package of various formats"
arch=('any')
url="https://github.com/conda/conda-package-handling"
license=('BSD')
depends=(
  'python'
  'python-six'
  'python-tqdm'
  #'python-libarchive-c'
  'libarchive'
)
makedepends=(
  'python-setuptools'
  'cython'
)
options=(!emptydirs)
install=
source=($_name-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz)
sha512sums=('e125ead9727cf3ee2a1a0621dc77e0de11d4edc00f0a3d80ccf140c7eb40f7aa207f648b9f6c6455be8d134118be0f5cf4735eab3faf71d4ee21484d8920c734')

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
