# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Brian Thompson <brianrobt@pm.me>
# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Guillaume Dolle  <dev at gdolle.com>
# Contributor: Blair Bonnett <blair dot bonnett at gmail dot com>
pkgname=micromamba
_pkgname=${pkgname/micro/}
pkgver=2.8.1
pkgrel=1
pkgdesc="The fast cross-platform package manager"
arch=(i686 x86_64)
url="https://github.com/${_pkgname}-org/${_pkgname}"
license=(BSD-3-Clause)
depends=(python fmt libsolv reproc yaml-cpp simdjson msgpack-c)
makedepends=(cli11 spdlog tl-expected nlohmann-json cmake pybind11 ninja
  python-build python-installer python-scikit-build-core)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz"
  etc-install.patch::https://github.com/mamba-org/mamba/commit/3dec9c0bc0e424749c649eae96de92c323e3b3d3.patch
  static-off.patch)
sha512sums=('ba2949c32506bcf355d549f01e5a309a862ca5618bc618d1a6b8e74d8413dbd8abaa4f2b9aec39faa593627b05ca1c6a2835e4800d646fd9c8d3a73a3801e89a'
            '2fcbaf269412225fdf5e3afc9e5d8c8122b24ad9e576cb9ba8fdb6050c1d4ac61aa0dbc38f482b41b9c586a3a25ad773e141e302a50e25dacda00fa85ca15212'
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
    -D BUILD_LIBMAMBA_SPDLOG=ON \
    -D BUILD_SHARED=ON \
    -D CMAKE_BUILD_WITH_INSTALL_RPATH=ON
  cmake --build build --parallel "$(nproc)"
  # temporary install for use by libmambapy’s build via `-Dlibmamba_ROOT=…`
  cmake --install build --prefix install

  cd "${_pkgname}-${pkgver}/libmambapy"
  export CMAKE_ARGS="\
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DBUILD_LIBMAMBA=ON \
    -DBUILD_LIBMAMBAPY=ON \
    -DBUILD_MICROMAMBA=OFF \
    -DBUILD_MAMBA_PACKAGE=OFF \
    -Dlibmamba-spdlog_DIR=$PWD/../../install/lib/cmake/libmamba-spdlog \
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
