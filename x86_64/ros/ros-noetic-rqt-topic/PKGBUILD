pkgdesc="ROS - rqt_topic provides a GUI plugin for displaying debug information about ROS topics including publishers, subscribers, publishing rate, and ROS Messages."
url='https://wiki.ros.org/rqt_topic'

pkgname='ros-noetic-rqt-topic'
pkgver='0.4.13'
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
    ros-noetic-python-qt-binding
    ros-noetic-rostopic
    ros-noetic-rqt-gui
    ros-noetic-rqt-gui-py
    ros-noetic-std-msgs
)

depends=(
    ${ros_depends[@]}
    python-rospkg
)

_dir="rqt_topic-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_topic/archive/${pkgver}.tar.gz")
sha256sums=('069b862dca74bdf5f45f767134e8c633af13d220490ca54a1add5ab9e15606b8')

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
