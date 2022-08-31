# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Javascript ROS message and service generators."
url='https://wiki.ros.org/gennodejs'

pkgname='ros-noetic-gennodejs'
pkgver='2.0.1'
_pkgver_patch=0
arch=('any')
pkgrel=1
license=('Apache 2.0')

ros_makedepends=(
	ros-noetic-genmsg
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-genmsg
)

depends=(
	${ros_depends[@]}
)

_dir="gennodejs-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RethinkRobotics-opensource/gennodejs/archive/${pkgver}.tar.gz")
sha256sums=('6380efc25d0c80e0372d1f57dea5e3bd3ab05b537f0477a702fd472965035478')

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
