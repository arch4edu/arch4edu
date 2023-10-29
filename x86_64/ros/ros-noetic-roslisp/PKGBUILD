# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Lisp client library for ROS, the Robot Operating System."
url='https://wiki.ros.org/roslisp'

pkgname='ros-noetic-roslisp'
pkgver='1.9.25'
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
	ros-noetic-rosgraph-msgs
	ros-noetic-roslang
	ros-noetic-std-srvs
	ros-noetic-rospack
)

depends=(
	${ros_depends[@]}
	sbcl
)

_dir="roslisp-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/roslisp/archive/${pkgver}.tar.gz")
sha256sums=('2a1b5d052ae8e08509d231353ba4b52742871594cb848d40519f741bf03f0b83')

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
