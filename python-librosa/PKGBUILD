# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-librosa
_pkgname=librosa
pkgver=0.7.2
pkgrel=1
pkgdesc="Python library for music and audio analysis"
arch=('any')
url="http://librosa.github.io/librosa"
license=('ISC')
depends=('python-numpy' 'python-scipy' 'python-six' 'python-numba' 'python-soundfile' 'python-joblib' 'python-matplotlib' 'python-audioread' 'python-decorator' 'python-scikit-learn' 'python-resampy')
makedepends=('python-setuptools')
source=("https://github.com/librosa/librosa/archive/${pkgver}.tar.gz")
md5sums=('091f2f966d902af5bf19409bdd80c418')

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
