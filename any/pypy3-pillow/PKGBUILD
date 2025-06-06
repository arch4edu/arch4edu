# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=Pillow
pkgname=pypy3-${_base,,}
pkgdesc="Python Imaging Library (Fork)"
pkgver=11.2.1
pkgrel=1
arch=(any)
url="https://github.com/python-${_base,,}/${_base}"
license=(MIT-CMU)
depends=(freetype2 glibc lcms2 libimagequant libjpeg-turbo libraqm
  libtiff libxcb openjpeg2 pypy3-packaging zlib)
makedepends=(libwebp tk git pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('4b5eee712b6cedf175e251ca29bb6e6dda27491585d343ef71ed416819e91510c4add6be50fe1151ab5f178f4686968de111beff4143a978b7a32519293a5725')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
