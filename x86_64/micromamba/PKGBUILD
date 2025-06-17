# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Co-Maintainer: Brian Thompson <brianrobt@pm.me>
# Contributor: Guillaume Dolle  <dev at gdolle.com>

pkgname=micromamba
_pkgname=${pkgname/micro/}
pkgver=2.3.0
pkgrel=1
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
sha512sums=('580afeddd18c7a3f41c2138d3a3ccdcd2b86faa126c7279f78036462b52fa205387d7421c197cb8ba19ad0117730be9077b07d5d62cd6cb6e55c68fa6da2261a'
            'ee549a0bff94bff386a820cb54e38b0c51f7f563c9dd99ab017bc4ba46a117a11fe8e6c016a8e6eef1ae30cde8e0f57b04d6cda685ad8f1609e1f22c38bf9258'
            '62deaeef709c6b03ed92cdf4890e4b8b8171ce72ddd83b3ff33ae8f9a2696a0ec1e1e6025b64ca654b3debb99654c9e36a404bc947b504becc452d6f39c168e6')
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
