# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=Pillow
pkgname=pypy3-${_base,,}
pkgdesc="Python Imaging Library (Fork)"
pkgver=11.3.0
pkgrel=1
arch=(any)
url="https://github.com/python-${_base,,}/${_base}"
license=(MIT-CMU)
depends=(freetype2 glibc lcms2 libimagequant libjpeg-turbo libraqm
  libtiff libxcb openjpeg2 pypy3-packaging zlib)
makedepends=(libwebp tk git pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('7d97e623bd41da94dd89a66dc600cea016d0a4f33fbf036175768ea96b2031c1968acf4fc3d9b2835ce93f9533838a9ce68a6579a7397f4aeccafb6032adb3db')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
