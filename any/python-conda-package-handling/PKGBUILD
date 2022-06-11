# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
_name=${pkgname#python-}
pkgver=1.7.3
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
sha512sums=('86ce78b1a3bcaacc59d751cec09a55fa3b539a7adad3edfc6aa10665c868d14977fb045f858590f04f2f54ee9d255556494e294d23c3f61b50af34c902f7aa0c')

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
