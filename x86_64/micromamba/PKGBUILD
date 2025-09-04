# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Brian Thompson <brianrobt@pm.me>
# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Guillaume Dolle  <dev at gdolle.com>
pkgname=micromamba
_pkgname=${pkgname/micro/}
pkgver=2.3.2
pkgrel=3
pkgdesc="The fast cross-platform package manager"
arch=(i686 x86_64)
url="https://github.com/${_pkgname}-org/${_pkgname}"
license=(BSD-3-Clause)
depends=(python fmt libsolv reproc yaml-cpp simdjson)
makedepends=(cli11 spdlog tl-expected nlohmann-json cmake pybind11 ninja
  python-build python-installer python-scikit-build)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz"
  pybind11-3.patch::https://github.com/mamba-org/mamba/commit/2e0ac1a9efcb276faecf36606442114d9ea699ae.patch
  etc-install.patch::https://github.com/mamba-org/mamba/commit/3dec9c0bc0e424749c649eae96de92c323e3b3d3.patch
  static-off.patch)
sha512sums=('7c6eef5d634042e142dfa1595344ced37ba7fe47e1b09fbce6208949a670dfe0c7e01d684e035be156f5f7bebad15065ffa672c41f585123b7d3c87b41a4adba'
            '18ff918e9feafe94a771cdadddfa34541a99339d6b1dc1393f8d6f983dbb55e6b2d6fa53e1bd5da449abeeaae7b0ee34ba761924ab7d53708eba6009f34969f5'
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
  cat "${srcdir}/pybind11-3.patch" | sed 's|libmambapy/bindings|libmambapy/src/libmambapy/bindings|' | patch -p1
  patch -p1 -i "${srcdir}/etc-install.patch"
  patch -p0 -i "${srcdir}/static-off.patch"
}

build() {
  cmake \
    -S "${_pkgname}-${pkgver}" \
    -B build/ \
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
  export SKBUILD_CONFIGURE_OPTIONS="\
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
