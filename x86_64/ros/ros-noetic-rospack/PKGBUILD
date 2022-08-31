# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - ROS Package Tool."
url='https://wiki.ros.org/rospack'

pkgname='ros-noetic-rospack'
pkgver='2.6.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-cmake-modules
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	tinyxml2
	gtest
	pkg-config
	boost
	python
)

ros_depends=(
	ros-noetic-ros-environment
)

depends=(
	${ros_depends[@]}
	tinyxml2
	python-rosdep
	python-catkin_pkg
	pkg-config
	boost
	python
)

_dir="rospack-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/rospack/archive/${pkgver}.tar.gz")
sha256sums=('85e2cb33ada71eb67d26e84c149f8a5812f9a6e6a1329e4923b95ae74921613a')

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
