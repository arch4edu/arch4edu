pkgdesc="ROS - Generic joystick teleop for twist robots."
url='https://wiki.ros.org/teleop_twist_joy'

pkgname='ros-noetic-teleop-twist-joy'
pkgver='0.1.3'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
    ros-noetic-catkin
    ros-noetic-geometry-msgs
    ros-noetic-joy
    ros-noetic-roscpp
    ros-noetic-roslaunch
    ros-noetic-roslint
    ros-noetic-rostest
    ros-noetic-sensor-msgs
)

makedepends=(
	cmake
	ros-build-tools
	${ros_makedepends[@]}
)

ros_depends=(
    ros-noetic-geometry-msgs
    ros-noetic-joy
    ros-noetic-roscpp
    ros-noetic-sensor-msgs
)

depends=(
    eigen
	${ros_depends[@]}
)

_dir="teleop_twist_joy-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-teleop/teleop_twist_joy/archive/${pkgver}.tar.gz")
sha256sums=('4b83d6e52e9334f63182af5cf6ebbfb1c1e38f009f39542d32483479bd9c80d2')

build() {
	# Use ROS environment variables.
	source /usr/share/ros-build-tools/clear-ros-env.sh
	[ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

	# Create the build directory.
	[ -d ${srcdir}/build ] || mkdir ${srcdir}/build
	cd ${srcdir}/build

	# Build the project.
	cmake ${srcdir}/${_dir} \
		-DCMAKE_BUILD_TYPE=Release \
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
