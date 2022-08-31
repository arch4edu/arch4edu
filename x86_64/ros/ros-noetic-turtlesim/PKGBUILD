# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - turtlesim is a tool made for teaching ROS and ROS packages."
url='https://wiki.ros.org/turtlesim'

pkgname='ros-noetic-turtlesim'
pkgver='0.10.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-std-srvs
	ros-noetic-roslib
	ros-noetic-catkin
	ros-noetic-message-generation
	ros-noetic-std-msgs
	ros-noetic-rosconsole
	ros-noetic-roscpp
	ros-noetic-roscpp-serialization
	ros-noetic-rostime
	ros-noetic-geometry-msgs
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	qt5-base
)

ros_depends=(
	ros-noetic-std-srvs
	ros-noetic-rostime
	ros-noetic-roslib
	ros-noetic-std-msgs
	ros-noetic-rosconsole
	ros-noetic-roscpp
	ros-noetic-roscpp-serialization
	ros-noetic-message-runtime
	ros-noetic-geometry-msgs
)

depends=(
	${ros_depends[@]}
	qt5-base
)

_dir="ros_tutorials-${pkgver}/turtlesim"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/ros_tutorials/archive/${pkgver}.tar.gz")
sha256sums=('c191f004ffaae3d8723798ed808767190576ef49308140dcfc7ab1adb3b4dcd0')

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
