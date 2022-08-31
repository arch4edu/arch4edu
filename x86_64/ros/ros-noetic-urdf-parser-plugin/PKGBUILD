# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This package contains a C++ base class for URDF parsers."
url='https://wiki.ros.org/urdf'

pkgname='ros-noetic-urdf-parser-plugin'
pkgver='1.13.2'
_pkgver_patch=0
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
	urdfdom-headers
)

ros_depends=(
)

depends=(
	${ros_depends[@]}
	urdfdom-headers
)

_dir="urdf-${pkgver}/urdf_parser_plugin"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/urdf/archive/${pkgver}.tar.gz")
sha256sums=('6643846ea63504463ec0f2c5ba4c73d965455b5ecc7aed81b860b8b4c8fa7133')

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
