# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=Pillow
pkgname=pypy3-${_base,,}
pkgdesc="Python Imaging Library (fork)"
pkgver=12.1.0
pkgrel=1
arch=(any)
url="https://github.com/python-${_base,,}/${_base}"
license=(MIT-CMU)
depends=(freetype2 glibc lcms2 libimagequant libjpeg-turbo libraqm
  libtiff libxcb openjpeg2 pypy3-packaging zlib)
makedepends=(libwebp tk git pypy3-build pypy3-installer pypy3-setuptools pypy3-pybind11)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('f542780a7894ca4eade3ee2c806f2bb0866cd93967ce45228ffaff9d0c9fb09eb3193a5afc9aa08caff1ed7f495031414fbd4a1addb3c373f8fa76a373a0be8d')

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
