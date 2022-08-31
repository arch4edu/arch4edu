# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - common_msgs contains messages that are widely used by other ROS packages."
url='https://wiki.ros.org/common_msgs'

pkgname='ros-noetic-common-msgs'
pkgver='1.13.1'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-diagnostic-msgs
	ros-noetic-trajectory-msgs
	ros-noetic-stereo-msgs
	ros-noetic-nav-msgs
	ros-noetic-actionlib-msgs
	ros-noetic-shape-msgs
	ros-noetic-visualization-msgs
	ros-noetic-sensor-msgs
	ros-noetic-geometry-msgs
)

depends=(
	${ros_depends[@]}
)

_dir="common_msgs-${pkgver}/common_msgs"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/common_msgs/archive/${pkgver}.tar.gz")
sha256sums=('74af8cc88bdc9c23cbc270d322e50562857e2c877359423f389d51c0735ee230')

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
