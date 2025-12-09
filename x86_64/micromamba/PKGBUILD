# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Brian Thompson <brianrobt@pm.me>
# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Guillaume Dolle  <dev at gdolle.com>
pkgname=micromamba
_pkgname=${pkgname/micro/}
pkgver=2.4.0
pkgrel=1
pkgdesc="The fast cross-platform package manager"
arch=(i686 x86_64)
url="https://github.com/${_pkgname}-org/${_pkgname}"
license=(BSD-3-Clause)
depends=(python fmt libsolv reproc yaml-cpp simdjson)
makedepends=(cli11 spdlog tl-expected nlohmann-json cmake pybind11 ninja
  python-build python-installer python-scikit-build-core)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz"
  etc-install.patch::https://github.com/mamba-org/mamba/commit/3dec9c0bc0e424749c649eae96de92c323e3b3d3.patch
  static-off.patch)
sha512sums=('ac0db60d1775929741c9908242bd846194b0a94f2e59677c85b022851a420b070cb209b4c80d315f7fc006dd32c53636f438b9cf9428b217a516a62795b193f3'
            '4e9230098bc1409e771d06811267c44d4ce95ce71ba9e5a2b63605e21302c94359d531a8f528944f09c76382468efda62daf51de171364c9198b2297111dff0e'
            '36c1ff684597251aba0de64cfee372212cdfe51890e584c15798b37bd41c02ed929596368b2c743934cfab89ce31bf9ac6ba9ee7f17ab038feb87fdecbadf1d8')
provides=(
  "libmamba=${pkgver}"
  "python-libmambapy=${pkgver}"
)
conflicts=(
  'micromamba-bin'
)

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/etc-install.patch"
  patch -p0 -i "${srcdir}/static-off.patch"
}

build() {
  cmake \
    -S "${_pkgname}-${pkgver}" \
    -B build \
    -G Ninja \
    -D CMAKE_INSTALL_PREFIX="/usr" \
    -D CMAKE_BUILD_TYPE=Release \
    -D BUILD_LIBMAMBA=ON \
    -D BUILD_LIBMAMBAPY=ON \
    -D BUILD_MICROMAMBA=ON \
    -D BUILD_SHARED=ON \
    -D CMAKE_BUILD_WITH_INSTALL_RPATH=ON
  cmake --build build --parallel "$(nproc)"
  cmake --install build --prefix install

  cd "${_pkgname}-${pkgver}/libmambapy"
  export CMAKE_ARGS="\
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DBUILD_LIBMAMBA=ON \
    -DBUILD_LIBMAMBAPY=ON \
    -DBUILD_MICROMAMBA=OFF \
    -DBUILD_MAMBA_PACKAGE=OFF \
    -Dlibmamba_ROOT=$PWD/../../install"
  python -m build --wheel --no-isolation --skip-dependency-check
}

check() {
  ctest --test-dir build
}

package() {
  # Install main components (C++ library, executables, headers)
  DESTDIR="${pkgdir}" cmake --build build --target install

  cd "${_pkgname}-${pkgver}"
  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"

  cd libmambapy
  python -m installer --destdir="$pkgdir" dist/*.whl
}
