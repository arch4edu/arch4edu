# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Metapackage of geometry tutorials ROS."
url='https://wiki.ros.org/geometry_tutorials'

pkgname='ros-noetic-geometry-tutorials'
pkgver='0.2.3'
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
	ros-noetic-turtle-tf
	ros-noetic-turtle-tf2
)

depends=(
	${ros_depends[@]}
)

_dir="geometry_tutorials-${pkgver}/geometry_tutorials"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/geometry_tutorials/archive/${pkgver}.tar.gz")
sha256sums=('7346c3a2d595cbac3d4d2f2e5aa01ff2c7fbafe1c21374efb09244629303ea2f')

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
