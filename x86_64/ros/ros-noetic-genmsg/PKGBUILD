# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Standalone Python library for generating ROS message and service data structures for various languages."
url='https://wiki.ros.org/genmsg'

pkgname='ros-noetic-genmsg'
pkgver='0.5.16'
arch=('any')
pkgrel=2
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
	ros-noetic-catkin
)

depends=(
	${ros_depends[@]}
)

_dir="genmsg-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/genmsg/archive/${pkgver}.tar.gz")
sha256sums=('0e414846823a2aaa7781f81268251c7c9a45ff96cef8e6a78bbbbcf7e4c28d56')

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
