# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - control_msgs contains base messages and actions useful for controlling robots."
url='https://wiki.ros.org/control_msgs'

pkgname='ros-noetic-control-msgs'
pkgver='1.5.2'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-trajectory-msgs
	ros-noetic-catkin
	ros-noetic-message-generation
	ros-noetic-std-msgs
	ros-noetic-actionlib-msgs
	ros-noetic-geometry-msgs
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-trajectory-msgs
	ros-noetic-std-msgs
	ros-noetic-actionlib-msgs
	ros-noetic-message-runtime
	ros-noetic-geometry-msgs
)

depends=(
	${ros_depends[@]}
)

_dir="control_msgs-${pkgver}/control_msgs"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-controls/control_msgs/archive/${pkgver}.tar.gz")
sha256sums=('6e74a95a91a0105196720acb0cb860724373e430480258f16c9b7661607ba36b')

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
