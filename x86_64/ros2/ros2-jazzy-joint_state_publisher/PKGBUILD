# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-joint_state_publisher
pkgname=(
    'ros2-jazzy-joint_state_publisher'
    'ros2-jazzy-joint_state_publisher_gui'
)
pkgver=2.4.3
pkgrel=1
pkgdesc="Package for publishing sensor_msgs/JointState messages for a robot described with URDF, for ROS 2 Jazzy"
url="https://github.com/ros/joint_state_publisher"
arch=('any')
license=('BSD-3-Clause')
depends=('ros2-jazzy')
makedepends=('python-colcon-common-extensions')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros/joint_state_publisher/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('7b13108c8b619371241d47b2e96d96d33609597a8df5a8041aa50716812a3e73')

_srcname="joint_state_publisher-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    cd "$srcdir/$_srcname"
    colcon build \
        --install-base "$srcdir/install" \
        --cmake-args -DBUILD_TESTING=OFF -Wno-dev
}

_install_sub() {
    local _sub="$1"
    install -d "$pkgdir/opt/ros/jazzy"
    cp -a "$srcdir/install/$_sub/." "$pkgdir/opt/ros/jazzy/"

    # Strip colcon per-package bookkeeping; keep only the package payload.
    rm -f "$pkgdir/opt/ros/jazzy"/COLCON_IGNORE \
          "$pkgdir/opt/ros/jazzy"/.colcon_install_layout \
          "$pkgdir/opt/ros/jazzy"/setup.* \
          "$pkgdir/opt/ros/jazzy"/local_setup.* \
          "$pkgdir/opt/ros/jazzy"/_local_setup_util_*.py \
          "$pkgdir/opt/ros/jazzy"/colcon-core-package-selection* 2>/dev/null

    install -Dm644 "$srcdir/$_srcname/$_sub/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-joint_state_publisher() {
    pkgdesc="Publishes sensor_msgs/JointState messages for a robot described with URDF, for ROS 2 Jazzy"
    depends=('ros2-jazzy' 'python-packaging')
    _install_sub joint_state_publisher
}

package_ros2-jazzy-joint_state_publisher_gui() {
    pkgdesc="GUI for setting and publishing joint state values for a robot, for ROS 2 Jazzy"
    depends=('ros2-jazzy' 'ros2-jazzy-joint_state_publisher')
    _install_sub joint_state_publisher_gui
}
