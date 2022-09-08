# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Simon Legner <Simon.Legner@gmail.com>
_base=pydub
pkgname=python-${_base}
pkgver=0.25.1
pkgrel=3
pkgdesc="Manipulate audio with a simple and easy high level interface"
url="https://${_base}.com"
license=(MIT)
arch=('any')
depends=(python ffmpeg)
makedepends=(python-setuptools)
optdepends=('python-pyaudio: for playback'
  'python-simpleaudio: for playback') # 'python-scipy' 'opus'
source=(https://github.com/jiaaro/${_base}/archive/v${pkgver}.tar.gz)
sha512sums=('8c3fb3714c4b0aed37ba7ab6727776bf4cd7568c1f5060cf43c30ede8da2ce4b498fb83326daa19ef44635250d552295407289c3945681e028eedde1b2b418e0')

build() {
  cd "${_base}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_base}-${pkgver}"
  python test/test.py
}

package() {
  cd "${_base}-${pkgver}"
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
