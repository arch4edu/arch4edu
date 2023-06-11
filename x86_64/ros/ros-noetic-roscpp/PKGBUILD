pkgdesc="ROS - roscpp is a C++ implementation of ROS."
url='https://github.com/ros/ros_comm'

pkgname='ros-noetic-roscpp'
pkgver='1.16.0'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
    ros-noetic-xmlrpcpp
    ros-noetic-roscpp-traits
    ros-noetic-catkin
    ros-noetic-rosgraph-msgs
    ros-noetic-message-generation
    ros-noetic-cpp-common
    ros-noetic-std-msgs
    ros-noetic-rosconsole
    ros-noetic-roscpp-serialization
    ros-noetic-rostime
    ros-noetic-roslang
)

makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
    pkg-config
    google-glog
)

ros_depends=(
    ros-noetic-rostime
    ros-noetic-xmlrpcpp
    ros-noetic-roscpp-traits
    ros-noetic-rosgraph-msgs
    ros-noetic-cpp-common
    ros-noetic-std-msgs
    ros-noetic-rosconsole
    ros-noetic-roscpp-serialization
    ros-noetic-message-runtime
)

depends=(
    ${ros_depends[@]}
)

_dir="ros_comm-${pkgver}/clients/roscpp"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/ros_comm/archive/${pkgver}.tar.gz")
sha256sums=('0a51857a50cf646db4af85469cb0e4877b1484f7aa0c00ec65a8be7ff574a886')

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
