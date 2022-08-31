pkgdesc="ROS - rqt_graph provides a GUI plugin for visualizing the ROS computation graph."
url='https://wiki.ros.org/rqt_graph'

pkgname='ros-noetic-rqt-graph'
pkgver='0.4.14'
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
    ros-noetic-rosservice
    ros-noetic-rqt-gui
    ros-noetic-rosnode
    ros-noetic-rosgraph-msgs
    ros-noetic-rostopic
    ros-noetic-rosgraph
    ros-noetic-python-qt-binding
    ros-noetic-qt-dotgraph
    ros-noetic-rospy
    ros-noetic-roslib
)

depends=(
    ${ros_depends[@]}
    python-rospkg
)

_dir="rqt_graph-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_graph/archive/${pkgver}.tar.gz")
sha256sums=('2b5f6440cb826362043a35ac561151033688560bfe1b84fb2dd2533424b017bc')

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
