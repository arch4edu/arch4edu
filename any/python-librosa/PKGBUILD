# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-librosa
_pkgname=librosa
pkgver=0.10.0.post2
pkgrel=1
pkgdesc="Python library for music and audio analysis"
arch=('any')
url="https://librosa.org"
license=('ISC')
depends=('python-numpy' 'python-scipy' 'python-six' 'python-numba' 'python-soundfile' 'python-joblib' 'python-matplotlib' 'python-audioread' 'python-decorator' 'python-pooch' 'python-scikit-learn' 'python-resampy')
makedepends=('python-setuptools')
source=("https://github.com/librosa/librosa/archive/${pkgver}.tar.gz")
md5sums=('003b5429b3c496ea0a394917dcc3fc9c')

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
