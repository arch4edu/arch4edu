# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=Pillow
pkgname=pypy3-${_base,,}
pkgdesc="Python Imaging Library (fork)"
pkgver=12.1.1
pkgrel=1
arch=(any)
url="https://github.com/python-${_base,,}/${_base}"
license=(MIT-CMU)
depends=(freetype2 glibc lcms2 libimagequant libjpeg-turbo libraqm
  libtiff libxcb openjpeg2 pypy3-packaging zlib)
makedepends=(libwebp tk git pypy3-build pypy3-installer pypy3-setuptools pypy3-pybind11)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('791c8972d913b616bd903aa4e9a468b1886faf5a477414fdd07cd37a29253f3e158988adf613969ea3f3efcef716d74b8d667efbac0d85ba12c15da2137c32a3')

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
