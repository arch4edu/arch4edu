# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

pkgname=ros2-humble-slam-toolbox
_pkgname=slam_toolbox
pkgver=2.6.10
pkgrel=1
pkgdesc="This package provides a sped up improved slam karto with updated SDK and visualization and modification toolsets"
url="https://index.ros.org/p/slam_toolbox/"
arch=('any')
depends=(
    'ros2-humble' 
    'eigen'
    'boost-libs'
    'suitesparse'
    'ceres-solver'
    'lapack'
    'tbb'
    'qt5-base'
)
makedepends=('cmake' 'boost')
source=("https://github.com/SteveMacenski/slam_toolbox/archive/refs/tags/${pkgver}.tar.gz"
        "ceres-manifold.patch")
sha256sums=('1a69a6db1473e4c2cabe34e3fd38186fcde3f5bacf00e5e9fcfa0b6b43263303'
            '43802b0d920dba1cabb2de1c89dde80088a70a472f80cc766255db5c27068343')


prepare() {
    # Boost 1.91: boost_system is header-only, no longer a compiled component
    sed -i 's/find_package(Boost REQUIRED system serialization filesystem thread)/find_package(Boost REQUIRED serialization filesystem thread)/' \
        "$_pkgname-$pkgver/CMakeLists.txt" \
        "$_pkgname-$pkgver/lib/karto_sdk/CMakeLists.txt"

    # Ceres 2.2: LocalParameterization removed, migrate to Manifold API
    patch -d "$_pkgname-$pkgver" -p1 -i ../ceres-manifold.patch
}

build() {
    source /opt/ros/humble/setup.bash

    # karto_sdk includes <Eigen/Core> but doesn't link Eigen3::Eigen
    export CXXFLAGS="$CXXFLAGS -I/usr/include/eigen3"

    cmake -B build -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/humble' \
        -DBoost_NO_BOOST_CMAKE=ON \
        -Wno-dev
    
    cmake --build build
}

package() {
    # Runtime-only dep: map_saver invokes nav2_map_server via subprocess.
    # Declared here (not global depends) so it's not required at build time.
    depends+=('ros2-humble-nav2-map-server')

    DESTDIR="$pkgdir" cmake --install build
}
