# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-ros_gz
pkgname=(
    'ros2-jazzy-ros_gz_interfaces'
    'ros2-jazzy-ros_gz_bridge'
    'ros2-jazzy-ros_gz_image'
    'ros2-jazzy-ros_gz_sim'
    'ros2-jazzy-ros_gz_sim_demos'
    'ros2-jazzy-ros_gz'
)
pkgver=1.0.24
pkgrel=1
pkgdesc="ROS 2 Jazzy integration with the Gazebo (Harmonic) simulator"
url="https://index.ros.org/p/ros_gz/"
arch=('x86_64')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=(
    'cmake'
    'cli11'
    'gflags'
    'pkgconf'
    'ros2-jazzy-gz-msgs-vendor'
    'ros2-jazzy-gz-transport-vendor'
    'ros2-jazzy-gz-sim-vendor'
    'ros2-jazzy-actuator_msgs'
    'ros2-jazzy-gps_msgs'
    'ros2-jazzy-marine_acoustic_msgs'
    'ros2-jazzy-vision_msgs'
    'ros2-jazzy-simulation_interfaces'
)
source=("$pkgbase-$pkgver.tar.gz::https://github.com/gazebosim/ros_gz/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('d7596d2c9a45e4a21948eaacfd5b1161d5fba85b5bc196301e61a85765deab51')

_srcname="ros_gz-$pkgver"

_build_cmake() {
    local _sub="$1"
    shift

    source /opt/ros/jazzy/setup.bash

    # The base ros2-jazzy gz_math_vendor ships a -extras.cmake that prepends a
    # leaked build path (/build/ros2-jazzy/src/install/...) instead of the
    # installed one, so find_package(gz-math) cannot locate the versionless
    # config. Prepend the correct extra_cmake directory to recover it.
    export CMAKE_PREFIX_PATH="/opt/ros/jazzy/opt/gz_math_vendor/extra_cmake:${CMAKE_PREFIX_PATH}"

    local _prefix='' _dep
    for _dep in "$@"; do
        _prefix+="$srcdir/_staging/$_dep/opt/ros/jazzy:"
    done

    CMAKE_PREFIX_PATH="${_prefix}${CMAKE_PREFIX_PATH}" \
        cmake -B "$srcdir/build-$_sub" -S "$srcdir/$_srcname/$_sub" \
            -DCMAKE_BUILD_TYPE='None' \
            -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
            -DBUILD_TESTING=OFF \
            -Wno-dev
    cmake --build "$srcdir/build-$_sub"
    DESTDIR="$srcdir/_staging/$_sub" cmake --install "$srcdir/build-$_sub"
}

build() {
    rm -rf "$srcdir/_staging"

    # Compiled bridge/sim/image libraries embed __FILE__ build paths.
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake ros_gz_interfaces
    _build_cmake ros_gz_bridge ros_gz_interfaces
    _build_cmake ros_gz_image ros_gz_bridge ros_gz_interfaces
    _build_cmake ros_gz_sim ros_gz_interfaces
    _build_cmake ros_gz_sim_demos
    _build_cmake ros_gz
}

package_ros2-jazzy-ros_gz_interfaces() {
    pkgdesc="Message and service definitions for interacting with Gazebo from ROS 2"
    depends=('ros2-jazzy')

    cp -a "$srcdir/_staging/ros_gz_interfaces/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-ros_gz_bridge() {
    pkgdesc="Bridge that enables the exchange of messages between ROS 2 and Gazebo Transport"
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-ros_gz_interfaces'
        'ros2-jazzy-gz-msgs-vendor'
        'ros2-jazzy-gz-transport-vendor'
        'ros2-jazzy-actuator_msgs'
        'ros2-jazzy-gps_msgs'
        'ros2-jazzy-marine_acoustic_msgs'
        'ros2-jazzy-vision_msgs'
    )

    cp -a "$srcdir/_staging/ros_gz_bridge/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-ros_gz_image() {
    pkgdesc="Utilities for using Gazebo Transport image messages with ROS 2 image_transport"
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-ros_gz_bridge'
        'ros2-jazzy-gz-msgs-vendor'
        'ros2-jazzy-gz-transport-vendor'
    )

    cp -a "$srcdir/_staging/ros_gz_image/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-ros_gz_sim() {
    pkgdesc="Tools and launch files for running the Gazebo simulator from ROS 2"
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-ros_gz_interfaces'
        'ros2-jazzy-gz-msgs-vendor'
        'ros2-jazzy-gz-transport-vendor'
        'ros2-jazzy-gz-sim-vendor'
        'ros2-jazzy-simulation_interfaces'
    )

    cp -a "$srcdir/_staging/ros_gz_sim/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-ros_gz_sim_demos() {
    pkgdesc="Demos for using ROS 2 with the Gazebo simulator"
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-ros_gz_bridge'
        'ros2-jazzy-ros_gz_image'
        'ros2-jazzy-ros_gz_sim'
        'ros2-jazzy-image_transport_plugins'
        'ros2-jazzy-rqt_image_view'
        'ros2-jazzy-sdformat_urdf'
        'ros2-jazzy-xacro'
        'ros2-jazzy-marine_acoustic_msgs'
    )

    cp -a "$srcdir/_staging/ros_gz_sim_demos/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-ros_gz() {
    pkgdesc="Metapackage pulling in the full ROS 2 / Gazebo integration stack"
    depends=(
        'ros2-jazzy-ros_gz_bridge'
        'ros2-jazzy-ros_gz_image'
        'ros2-jazzy-ros_gz_sim'
        'ros2-jazzy-ros_gz_sim_demos'
    )

    cp -a "$srcdir/_staging/ros_gz/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
