# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-nav2_minimal_turtlebot_simulation
pkgname=(
    'ros2-jazzy-nav2_minimal_tb3_sim'
    'ros2-jazzy-nav2_minimal_tb4_description'
    'ros2-jazzy-nav2_minimal_tb4_sim'
)
pkgver=1.0.1
pkgrel=1
pkgdesc="Minimal TurtleBot simulation assets for Nav2 on ROS 2 Jazzy"
url="https://github.com/ros-navigation/nav2_minimal_turtlebot_simulation"
arch=('any')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=('cmake' 'python-colcon-common-extensions' 'ros2-jazzy-xacro')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-navigation/nav2_minimal_turtlebot_simulation/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('78d97bbd8208e165cafc13016704ce8fec880ab01b4a311c7eee706b1fc82ddf')

_srcname="nav2_minimal_turtlebot_simulation-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    cd "$srcdir/$_srcname"
    colcon build \
        --install-base "$srcdir/install" \
        --cmake-args -DCMAKE_BUILD_TYPE=None -DBUILD_TESTING=OFF -Wno-dev
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

    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-nav2_minimal_tb3_sim() {
    pkgdesc="Minimal TurtleBot3 Gazebo simulation assets for Nav2 on ROS 2 Jazzy"
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-xacro'
        'ros2-jazzy-ros_gz_bridge'
        'ros2-jazzy-ros_gz_image'
        'ros2-jazzy-ros_gz_interfaces'
        'ros2-jazzy-ros_gz_sim'
    )
    _install_sub nav2_minimal_tb3_sim
}

package_ros2-jazzy-nav2_minimal_tb4_description() {
    pkgdesc="Minimal TurtleBot4 URDF description for Nav2 on ROS 2 Jazzy"
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-xacro'
        'ros2-jazzy-joint_state_publisher'
    )
    _install_sub nav2_minimal_tb4_description
}

package_ros2-jazzy-nav2_minimal_tb4_sim() {
    pkgdesc="Minimal TurtleBot4 Gazebo simulation assets for Nav2 on ROS 2 Jazzy"
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-nav2_minimal_tb4_description'
        'ros2-jazzy-xacro'
        'ros2-jazzy-ros_gz_bridge'
        'ros2-jazzy-ros_gz_image'
        'ros2-jazzy-ros_gz_interfaces'
        'ros2-jazzy-ros_gz_sim'
    )
    _install_sub nav2_minimal_tb4_sim
}
