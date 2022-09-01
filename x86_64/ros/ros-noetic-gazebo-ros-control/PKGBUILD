pkgdesc="ROS - gazebo_ros_control."
url='http://ros.org/wiki/gazebo_ros_control'

pkgname='ros-noetic-gazebo-ros-control'
pkgver='2.9.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=4
license=('BSD')

ros_makedepends=(
    ros-noetic-catkin
    ros-noetic-gazebo-dev
)

makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
)

ros_depends=(
    ros-noetic-gazebo-ros
    ros-noetic-roscpp
    ros-noetic-std-msgs
    ros-noetic-control-toolbox
    ros-noetic-controller-manager
    ros-noetic-controller-manager-msgs
    ros-noetic-controller-interface
    ros-noetic-pluginlib
    ros-noetic-hardware-interface
    ros-noetic-transmission-interface
    ros-noetic-joint-limits-interface
    ros-noetic-urdf
    ros-noetic-angles
)

depends=(
    ${ros_depends[@]}
)

_dir="gazebo_ros_pkgs-${pkgver}/gazebo_ros_control"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-simulation/gazebo_ros_pkgs/archive/${pkgver}.tar.gz")
sha256sums=('db937f15e5bf8f804de5d8dc0b67607f8b354aecde35785b6bff2d43387abff4')

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}
