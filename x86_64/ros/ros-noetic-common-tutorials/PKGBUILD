# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Metapackage that contains common tutorials."
url='https://wiki.ros.org/common_tutorials'

pkgname='ros-noetic-common-tutorials'
pkgver='0.2.0'
_pkgver_patch=0
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
	ros-noetic-pluginlib-tutorials
	ros-noetic-turtle-actionlib
	ros-noetic-nodelet-tutorial-math
	ros-noetic-actionlib-tutorials
)

depends=(
	${ros_depends[@]}
)

_dir="common_tutorials-${pkgver}/common_tutorials"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/common_tutorials/archive/${pkgver}.tar.gz")
sha256sums=('61b4f75a846264debe4f8eb4c7090f21079c5cd368f85124cf13eca6340570f3')

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
