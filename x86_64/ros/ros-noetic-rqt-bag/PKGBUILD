pkgdesc="ROS - rqt_bag provides a GUI plugin for displaying and replaying ROS bag files."
url='https://wiki.ros.org/rqt_bag'

pkgname='ros-noetic-rqt-bag'
pkgver='0.5.1'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
    ros-noetic-catkin
)

makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
)

ros_depends=(
    ros-noetic-rqt-gui-py
    ros-noetic-rosbag
    ros-noetic-rosnode
    ros-noetic-rosgraph-msgs
    ros-noetic-python-qt-binding
    ros-noetic-rqt-gui
    ros-noetic-rospy
    ros-noetic-roslib
)

depends=(
    ${ros_depends[@]}
    python-rospkg
)

_dir="rqt_bag-${pkgver}/rqt_bag"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_bag/archive/${pkgver}.tar.gz")
sha256sums=('52c194b9bdfc63b03b88fdb9d851715ba456a9fc016cf22c8f9cbf0c0bc9ecf9')

build() {
    # Use ROS environment variables.
    source /usr/share/ros-build-tools/clear-ros-env.sh
    [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

    # Create the build directory.
    [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
    cd ${srcdir}/build

    # Build the project.
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
