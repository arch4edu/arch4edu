# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
_name=${pkgname#python-}
pkgver=1.7.2
pkgrel=2
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
sha512sums=('cfa8f49c9345ba803068086ec37d21e7b7e366007e48ca79942f39bb667740ac94a8ee0d4a00a0664723090c108135d7dc5cbc84cf8dd6807461a544443eda3f')

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
