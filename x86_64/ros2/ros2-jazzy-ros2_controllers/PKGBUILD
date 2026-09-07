# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-ros2_controllers
pkgname=(
    'ros2-jazzy-ackermann_steering_controller'
    'ros2-jazzy-admittance_controller'
    'ros2-jazzy-battery_state_broadcaster'
    'ros2-jazzy-bicycle_steering_controller'
    'ros2-jazzy-chained_filter_controller'
    'ros2-jazzy-diff_drive_controller'
    'ros2-jazzy-effort_controllers'
    'ros2-jazzy-force_torque_sensor_broadcaster'
    'ros2-jazzy-forward_command_controller'
    'ros2-jazzy-gpio_controllers'
    'ros2-jazzy-gps_sensor_broadcaster'
    'ros2-jazzy-gripper_controllers'
    'ros2-jazzy-imu_sensor_broadcaster'
    'ros2-jazzy-joint_state_broadcaster'
    'ros2-jazzy-joint_trajectory_controller'
    'ros2-jazzy-magnetometer_broadcaster'
    'ros2-jazzy-mecanum_drive_controller'
    'ros2-jazzy-motion_primitives_controllers'
    'ros2-jazzy-omni_wheel_drive_controller'
    'ros2-jazzy-parallel_gripper_controller'
    'ros2-jazzy-pid_controller'
    'ros2-jazzy-pose_broadcaster'
    'ros2-jazzy-position_controllers'
    'ros2-jazzy-range_sensor_broadcaster'
    'ros2-jazzy-ros2_controllers'
    'ros2-jazzy-ros2_controllers_test_nodes'
    'ros2-jazzy-rqt_joint_trajectory_controller'
    'ros2-jazzy-state_interfaces_broadcaster'
    'ros2-jazzy-steering_controllers_library'
    'ros2-jazzy-tricycle_controller'
    'ros2-jazzy-tricycle_steering_controller'
    'ros2-jazzy-velocity_controllers'
)
pkgver=4.42.1
pkgrel=1
pkgdesc="Controllers for the ROS 2 Jazzy control framework"
url="https://github.com/ros-controls/ros2_controllers"
arch=('x86_64')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=(
    'cmake'
    'python-colcon-common-extensions'
    'python-rospkg'
    'eigen'
    'tl-expected'
    'tinyxml2'
    'ros2-jazzy-ackermann_msgs'
    'ros2-jazzy-angles'
    'ros2-jazzy-backward_ros'
    'ros2-jazzy-control_msgs'
    'ros2-jazzy-control_toolbox'
    'ros2-jazzy-controller_interface'
    'ros2-jazzy-controller_manager_msgs'
    'ros2-jazzy-filters'
    'ros2-jazzy-generate_parameter_library'
    'ros2-jazzy-hardware_interface'
    'ros2-jazzy-kinematics_interface'
    'ros2-jazzy-realtime_tools'
    'ros2-jazzy-rsl'
    'ros2-jazzy-ros2_control_cmake'
)
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-controls/ros2_controllers/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('66adde7cdaea72c173e7f09f6cd1971257c6397fd750f1df936a4b55561f8fc3')

_srcname="ros2_controllers-$pkgver"

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

package_ros2-jazzy-ackermann_steering_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-steering_controllers_library'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub ackermann_steering_controller
}

package_ros2-jazzy-admittance_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-control_toolbox'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-kinematics_interface'
        'ros2-jazzy-realtime_tools'
        'tinyxml2'
    )
    _install_sub admittance_controller
}

package_ros2-jazzy-battery_state_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub battery_state_broadcaster
}

package_ros2-jazzy-bicycle_steering_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-steering_controllers_library'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub bicycle_steering_controller
}

package_ros2-jazzy-chained_filter_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-filters'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub chained_filter_controller
}

package_ros2-jazzy-diff_drive_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_toolbox'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub diff_drive_controller
}

package_ros2-jazzy-effort_controllers() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-forward_command_controller'
    )
    _install_sub effort_controllers
}

package_ros2-jazzy-force_torque_sensor_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-filters'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub force_torque_sensor_broadcaster
}

package_ros2-jazzy-forward_command_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub forward_command_controller
}

package_ros2-jazzy-gpio_controllers() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub gpio_controllers
}

package_ros2-jazzy-gps_sensor_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub gps_sensor_broadcaster
}

package_ros2-jazzy-gripper_controllers() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-control_toolbox'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub gripper_controllers
}

package_ros2-jazzy-imu_sensor_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub imu_sensor_broadcaster
}

package_ros2-jazzy-joint_state_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub joint_state_broadcaster
}

package_ros2-jazzy-joint_trajectory_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-control_toolbox'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'tl-expected'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-rsl'
    )
    _install_sub joint_trajectory_controller
}

package_ros2-jazzy-magnetometer_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'eigen'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub magnetometer_broadcaster
}

package_ros2-jazzy-mecanum_drive_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-control_toolbox'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub mecanum_drive_controller
}

package_ros2-jazzy-motion_primitives_controllers() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub motion_primitives_controllers
}

package_ros2-jazzy-omni_wheel_drive_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-controller_interface'
        'eigen'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub omni_wheel_drive_controller
}

package_ros2-jazzy-parallel_gripper_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-control_toolbox'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub parallel_gripper_controller
}

package_ros2-jazzy-pid_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-angles'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-control_toolbox'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub pid_controller
}

package_ros2-jazzy-pose_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub pose_broadcaster
}

package_ros2-jazzy-position_controllers() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-forward_command_controller'
    )
    _install_sub position_controllers
}

package_ros2-jazzy-range_sensor_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub range_sensor_broadcaster
}

package_ros2-jazzy-ros2_controllers() {
    arch=('any')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-ackermann_steering_controller'
        'ros2-jazzy-admittance_controller'
        'ros2-jazzy-battery_state_broadcaster'
        'ros2-jazzy-bicycle_steering_controller'
        'ros2-jazzy-chained_filter_controller'
        'ros2-jazzy-diff_drive_controller'
        'ros2-jazzy-effort_controllers'
        'ros2-jazzy-force_torque_sensor_broadcaster'
        'ros2-jazzy-forward_command_controller'
        'ros2-jazzy-gpio_controllers'
        'ros2-jazzy-gps_sensor_broadcaster'
        'ros2-jazzy-gripper_controllers'
        'ros2-jazzy-imu_sensor_broadcaster'
        'ros2-jazzy-joint_state_broadcaster'
        'ros2-jazzy-joint_trajectory_controller'
        'ros2-jazzy-magnetometer_broadcaster'
        'ros2-jazzy-mecanum_drive_controller'
        'ros2-jazzy-omni_wheel_drive_controller'
        'ros2-jazzy-parallel_gripper_controller'
        'ros2-jazzy-pid_controller'
        'ros2-jazzy-pose_broadcaster'
        'ros2-jazzy-position_controllers'
        'ros2-jazzy-range_sensor_broadcaster'
        'ros2-jazzy-state_interfaces_broadcaster'
        'ros2-jazzy-steering_controllers_library'
        'ros2-jazzy-tricycle_controller'
        'ros2-jazzy-tricycle_steering_controller'
        'ros2-jazzy-velocity_controllers'
    )
    _install_sub ros2_controllers
}

package_ros2-jazzy-ros2_controllers_test_nodes() {
    arch=('any')
    depends=(
        'ros2-jazzy'
    )
    _install_sub ros2_controllers_test_nodes
}

package_ros2-jazzy-rqt_joint_trajectory_controller() {
    arch=('any')
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_manager_msgs'
        'python-rospkg'
    )
    _install_sub rqt_joint_trajectory_controller
}

package_ros2-jazzy-state_interfaces_broadcaster() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub state_interfaces_broadcaster
}

package_ros2-jazzy-steering_controllers_library() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-generate_parameter_library'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
    )
    _install_sub steering_controllers_library
}

package_ros2-jazzy-tricycle_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-ackermann_msgs'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-realtime_tools'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub tricycle_controller
}

package_ros2-jazzy-tricycle_steering_controller() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-control_msgs'
        'ros2-jazzy-controller_interface'
        'ros2-jazzy-hardware_interface'
        'ros2-jazzy-steering_controllers_library'
        'ros2-jazzy-generate_parameter_library'
    )
    _install_sub tricycle_steering_controller
}

package_ros2-jazzy-velocity_controllers() {
    depends=(
        'ros2-jazzy'
        'ros2-jazzy-backward_ros'
        'ros2-jazzy-forward_command_controller'
    )
    _install_sub velocity_controllers
}
