# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=Pillow
pkgname=pypy3-${_base,,}
pkgdesc="Python Imaging Library (fork)"
pkgver=12.2.0
pkgrel=1
arch=(any)
url="https://github.com/python-${_base,,}/${_base}"
license=(MIT-CMU)
depends=(freetype2 glibc lcms2 libimagequant libjpeg-turbo libraqm
  libtiff libxcb openjpeg2 pypy3-packaging zlib)
makedepends=(libwebp tk git pypy3-build pypy3-installer pypy3-setuptools pypy3-pybind11)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('cd66b5b033f82127934624c474aed55c014d10d5e7cc9455ea6a3470d1b7e9f0b94ad2c0a5f1559e01ce003fc179b01fee89aa1b51d78dff3f04927d8252a41e')

build() {
  cd ${_base}-${pkgver}
  PKG_CONFIG_PATH=$(/opt/pypy3/bin/pybind11-config --pkgconfigdir) \
	pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
