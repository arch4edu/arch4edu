# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Package modeling the run-time dependencies for language bindings of messages."
url='https://wiki.ros.org/message_runtime'

pkgname='ros-noetic-message-runtime'
pkgver='0.4.13'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
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
	ros-noetic-roscpp-traits
	ros-noetic-genpy
	ros-noetic-cpp-common
	ros-noetic-roscpp-serialization
	ros-noetic-rostime
)

depends=(
	${ros_depends[@]}
)

_dir="message_runtime-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/message_runtime/archive/${pkgver}.tar.gz")
sha256sums=('c5f97145b5095389d2459c0e7d879c07f5878d0b7ec84b5c388abddfd52bf448')

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
