# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This is a set of tools for recording from and playing back ROS message without relying on the ROS client library."
url='https://wiki.ros.org/rosbag_storage'

pkgname='ros-noetic-rosbag-storage'
pkgver='1.15.14'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-rostest
	ros-noetic-roscpp-traits
	ros-noetic-catkin
	ros-noetic-roslz4
	ros-noetic-cpp-common
	ros-noetic-roscpp-serialization
	ros-noetic-rostime
	ros-noetic-pluginlib
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	console-bridge
	gpgme
	openssl
	boost
	bzip2
)

ros_depends=(
	ros-noetic-roscpp-traits
	ros-noetic-roslz4
	ros-noetic-cpp-common
	ros-noetic-roscpp-serialization
	ros-noetic-rostime
	ros-noetic-pluginlib
)

depends=(
	${ros_depends[@]}
	console-bridge
	gpgme
	openssl
	boost
	bzip2
)

_dir="ros_comm-${pkgver}/tools/rosbag_storage"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/ros_comm/archive/${pkgver}.tar.gz")
sha256sums=('1083b58470a81323bc3a13aa9ae7c813e9fbc27b18f0e95a76b53e4076f3d872')

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
