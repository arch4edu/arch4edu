# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - tf is a package that lets the user keep track of multiple coordinate frames over time."
url='https://wiki.ros.org/tf'

pkgname='ros-noetic-tf'
pkgver='1.13.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
license=('BSD')

ros_makedepends=(
	ros-noetic-angles
	ros-noetic-rostime
	ros-noetic-catkin
	ros-noetic-message-generation
	ros-noetic-std-msgs
	ros-noetic-tf2-ros
	ros-noetic-rosconsole
	ros-noetic-roscpp
	ros-noetic-message-filters
	ros-noetic-sensor-msgs
	ros-noetic-geometry-msgs
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-roswtf
	ros-noetic-message-runtime
	ros-noetic-std-msgs
	ros-noetic-tf2-ros
	ros-noetic-rosconsole
	ros-noetic-roscpp
	ros-noetic-message-filters
	ros-noetic-sensor-msgs
	ros-noetic-geometry-msgs
)

depends=(
	${ros_depends[@]}
	graphviz
)

_dir="geometry-${pkgver}/tf"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/geometry/archive/${pkgver}.tar.gz")
sha256sums=('6b653d4e10503d3da56bc4000e39ce58d6a85547a37837da576edccecc0c6ae2')

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
		-DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCMAKE_CXX_STANDARD=17
	make
}

package() {
	cd "${srcdir}/build"
	make DESTDIR="${pkgdir}/" install
}
