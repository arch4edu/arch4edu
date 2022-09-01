# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This package allows you to publish the state of a robot to tf."
url='https://wiki.ros.org/robot_state_publisher'

pkgname='ros-noetic-robot-state-publisher'
pkgver='1.15.2'
_pkgver_patch=0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-tf2-kdl
	ros-noetic-rostime
	ros-noetic-catkin
	ros-noetic-tf
	ros-noetic-tf2-ros
	ros-noetic-rosconsole
	ros-noetic-roscpp
	ros-noetic-kdl-parser
	ros-noetic-sensor-msgs
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	eigen
	urdfdom-headers
	orocos-kdl
)

ros_depends=(
	ros-noetic-tf2-kdl
	ros-noetic-rostime
	ros-noetic-catkin
	ros-noetic-tf
	ros-noetic-tf2-ros
	ros-noetic-rosconsole
	ros-noetic-roscpp
	ros-noetic-kdl-parser
	ros-noetic-sensor-msgs
)

depends=(
	${ros_depends[@]}
	eigen
	orocos-kdl
)

_dir="robot_state_publisher-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/robot_state_publisher/archive/${pkgver}.tar.gz")
sha256sums=('15dd320a7409cd3542a9e78a18e103be54c5fa3cf467276085c804314014e521')

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
        -DCMAKE_CXX_STANDARD=17 \
		-DSETUPTOOLS_DEB_LAYOUT=OFF
	make
}

package() {
	cd "${srcdir}/build"
	make DESTDIR="${pkgdir}/" install
}
