# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-ros2_control
pkgname=(
    'ros2-jazzy-controller_manager_msgs'
    'ros2-jazzy-hardware_interface'
    'ros2-jazzy-joint_limits'
    'ros2-jazzy-transmission_interface'
    'ros2-jazzy-controller_interface'
    'ros2-jazzy-ros2_control_test_assets'
    'ros2-jazzy-hardware_interface_testing'
    'ros2-jazzy-controller_manager'
    'ros2-jazzy-ros2controlcli'
    'ros2-jazzy-rqt_controller_manager'
    'ros2-jazzy-ros2_control'
)
pkgver=4.48.0
pkgrel=1
pkgdesc="Real-time control framework for ROS 2 Jazzy"
url="https://github.com/ros-controls/ros2_control"
arch=('x86_64')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=(
    'cmake'
    'python-colcon-common-extensions'
    'python-filelock'
    'python-yaml'
    'fmt'
    'tinyxml2'
    'ros2-jazzy-backward_ros'
    'ros2-jazzy-control_msgs'
    'ros2-jazzy-diagnostic_updater'
    'ros2-jazzy-generate_parameter_library'
    'ros2-jazzy-pal_statistics'
    'ros2-jazzy-realtime_tools'
    'ros2-jazzy-ros2_control_cmake'
    'ros2-jazzy-sdformat_urdf'
)
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-controls/ros2_control/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('8f1681ccb2cb0a24e7d1322a4e4bc6419567e3ce225df1eeadb8198f9a67325b')

_srcname="ros2_control-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    cd "$srcdir/$_srcname"
    colcon build \
        --install-base "$srcdir/install" \
        --cmake-args -DCMAKE_BUILD_TYPE=None -DBUILD_TESTING=OFF -Wno-dev
}

_install_sub() {
    local sub="$1"
    install -d "$pkgdir/opt/ros/jazzy"
    cp -a "$srcdir/install/$sub/." "$pkgdir/opt/ros/jazzy/"
    rm -f "$pkgdir/opt/ros/jazzy"/COLCON_IGNORE \
          "$pkgdir/opt/ros/jazzy"/.colcon_install_layout \
          "$pkgdir/opt/ros/jazzy"/setup.* \
          "$pkgdir/opt/ros/jazzy"/local_setup.* \
          "$pkgdir/opt/ros/jazzy"/_local_setup_util_*.py \
          "$pkgdir/opt/ros/jazzy"/colcon-core-package-selection* 2>/dev/null
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-controller_manager_msgs() {
    depends=('ros2-jazzy')
    _install_sub controller_manager_msgs
}

package_ros2-jazzy-hardware_interface() {
    depends=('ros2-jazzy' 'ros2-jazzy-backward_ros' 'ros2-jazzy-control_msgs' 'ros2-jazzy-joint_limits' 'ros2-jazzy-pal_statistics' 'ros2-jazzy-realtime_tools' 'ros2-jazzy-sdformat_urdf' 'fmt' 'tinyxml2')
    _install_sub hardware_interface
}

package_ros2-jazzy-joint_limits() {
    depends=('ros2-jazzy' 'ros2-jazzy-backward_ros' 'ros2-jazzy-realtime_tools' 'fmt')
    _install_sub joint_limits
}

package_ros2-jazzy-transmission_interface() {
    depends=('ros2-jazzy' 'ros2-jazzy-hardware_interface' 'fmt')
    _install_sub transmission_interface
}

package_ros2-jazzy-controller_interface() {
    depends=('ros2-jazzy' 'ros2-jazzy-hardware_interface' 'ros2-jazzy-pal_statistics' 'ros2-jazzy-realtime_tools' 'fmt')
    _install_sub controller_interface
}

package_ros2-jazzy-ros2_control_test_assets() {
    arch=('any')
    depends=('ros2-jazzy')
    _install_sub ros2_control_test_assets
}

package_ros2-jazzy-hardware_interface_testing() {
    depends=('ros2-jazzy' 'ros2-jazzy-control_msgs' 'ros2-jazzy-hardware_interface' 'ros2-jazzy-ros2_control_test_assets' 'fmt')
    _install_sub hardware_interface_testing
}

package_ros2-jazzy-controller_manager() {
    depends=('ros2-jazzy' 'ros2-jazzy-backward_ros' 'ros2-jazzy-controller_interface' 'ros2-jazzy-controller_manager_msgs' 'ros2-jazzy-diagnostic_updater' 'ros2-jazzy-generate_parameter_library' 'ros2-jazzy-hardware_interface' 'ros2-jazzy-realtime_tools' 'python-filelock' 'python-yaml' 'fmt')
    _install_sub controller_manager
}

package_ros2-jazzy-ros2controlcli() {
    arch=('any')
    depends=('ros2-jazzy' 'ros2-jazzy-controller_manager' 'ros2-jazzy-controller_manager_msgs' 'python-graphviz')
    _install_sub ros2controlcli
}

package_ros2-jazzy-rqt_controller_manager() {
    arch=('any')
    depends=('ros2-jazzy' 'ros2-jazzy-controller_manager' 'ros2-jazzy-controller_manager_msgs')
    _install_sub rqt_controller_manager
}

package_ros2-jazzy-ros2_control() {
    arch=('any')
    depends=(
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-controller_manager'
        'ros2-jazzy-controller_manager_msgs'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-joint_limits'
        'ros2-jazzy-ros2controlcli'
        'ros2-jazzy-ros2_control_test_assets'
        'ros2-jazzy-transmission_interface'
    )
    _install_sub ros2_control
}
