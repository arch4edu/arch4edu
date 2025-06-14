# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Co-Maintainer: Brian Thompson <brianrobt@pm.me>
# Contributor: Guillaume Dolle  <dev at gdolle.com>

pkgname=micromamba
_pkgname=${pkgname/micro/}
pkgver=2.2.0
pkgrel=2
pkgdesc="The fast cross-platform package manager"
arch=(i686 x86_64)
url="https://github.com/${_pkgname}-org/${_pkgname}"
license=(BSD-3-Clause)
depends=(
  python
  fmt
  libsolv
  reproc
  yaml-cpp
  simdjson
)
makedepends=(
  cli11
  spdlog
  tl-expected
  nlohmann-json
  cmake
  pybind11
  ninja
)
source=(
  ${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz
  static-off.patch
  utils.cpp.patch
)
sha512sums=(
  'e17f22ad0025fb802cf29830a3449e6b35bbca5bd319196904557993a825868007247fbf1651517864439de5224ebdb76d532bd1340a3021360ac93530526102'
  'SKIP'
  'SKIP'
)
provides=(
  "libmamba=${pkgver}"
  "libmambapy=${pkgver}"
)
conflicts=(
  'micromamba-bin'
)

prepare() {
  cd ${_pkgname}-${pkgver}
  patch -p0 -i "${srcdir}/static-off.patch"
  patch -p0 -i "${srcdir}/utils.cpp.patch"
}

build() {
  cmake \
    -S ${_pkgname}-${pkgver} \
    -B build/ \
    -G Ninja \
    -D CMAKE_INSTALL_PREFIX="/usr" \
    -D CMAKE_BUILD_TYPE=Release \
    -D BUILD_LIBMAMBA=ON \
    -D BUILD_LIBMAMBAPY=ON \
    -D BUILD_MICROMAMBA=ON \
    -D BUILD_SHARED=ON \
    -D CMAKE_BUILD_WITH_INSTALL_RPATH=ON
  cmake --build build --parallel $(nproc)
}

check() {
  ctest --test-dir build
}

package() {
    # Install main components (C++ library, executables, headers)
    DESTDIR="${pkgdir}" cmake --build build --target install

    # Manually install Python bindings
    local python_version=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    local site_packages="$pkgdir/usr/lib/python$python_version/site-packages"

    # Create site-packages directory
    mkdir -p "$site_packages"

    # Copy the built Python module
    cp -r build/libmambapy/libmambapy "$site_packages/"

    # Set proper permissions
    find "$site_packages/libmambapy" -type f -exec chmod 644 {} \;
    find "$site_packages/libmambapy" -type d -exec chmod 755 {} \;
    chmod 755 "$site_packages/libmambapy"/*.so
}