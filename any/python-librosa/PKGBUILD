# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-librosa
_pkgname=librosa
pkgver=0.10.2
pkgrel=1
pkgdesc="Python library for music and audio analysis"
arch=('any')
url="https://librosa.org"
license=('ISC')
depends=(
  'python-audioread'
  'python-decorator'
  'python-joblib'
  'python-lazy-loader'
  'python-matplotlib'
  'python-numba'
  'python-numpy'
  'python-pooch'
  'python-resampy'
  'python-scikit-learn'
  'python-scipy'
  'python-six'
  'python-soundfile'
  'python-soxr'
)
makedepends=('python-setuptools')
source=("https://github.com/librosa/librosa/archive/${pkgver}.tar.gz")
md5sums=('dfd6cd2aa29050c61cb73c942dee768f')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
