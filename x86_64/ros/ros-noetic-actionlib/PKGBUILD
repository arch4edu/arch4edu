# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - The actionlib stack provides a standardized interface for interfacing with preemptable tasks."
url='https://wiki.ros.org/actionlib'

pkgname='ros-noetic-actionlib'
pkgver='1.13.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-rostest
	ros-noetic-catkin
	ros-noetic-message-generation
	ros-noetic-actionlib-msgs
	ros-noetic-std-msgs
	ros-noetic-roscpp
	ros-noetic-rospy
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	boost
)

ros_depends=(
	ros-noetic-rostest
	ros-noetic-actionlib-msgs
	ros-noetic-rostopic
	ros-noetic-std-msgs
	ros-noetic-roscpp
	ros-noetic-message-runtime
	ros-noetic-rospy
	ros-noetic-roslib
)

depends=(
	${ros_depends[@]}
	python-wxpython
	boost
)

_dir="actionlib-${pkgver}/actionlib"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/actionlib/archive/${pkgver}.tar.gz")
sha256sums=('b741755881e30b9aea6bcdd9831e3f0932a8bbba02fa59e5c0e5970280024055')

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
