# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - The class_loader package is a ROS-independent package for loading plugins during runtime and the foundation of the higher level ROS pluginlib library."
url='https://wiki.ros.org/class_loader'

pkgname='ros-noetic-class-loader'
pkgver='0.5.0'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
license=('BSD')

ros_makedepends=(
	ros-noetic-cmake-modules
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	boost
	console-bridge
	poco
)

ros_depends=(
)

depends=(
	${ros_depends[@]}
	boost
	console-bridge
	poco
)

_dir="class_loader-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/class_loader/archive/${pkgver}.tar.gz")
sha256sums=('134ef1ecfb20a7a59b89af716d209f915c8a5e0a6c1067b420fd2f38e84ba663')

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
