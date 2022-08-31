# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Python implementation of the URDF parser."
url='https://wiki.ros.org/urdfdom_py'

pkgname='ros-noetic-urdfdom-py'
pkgver='0.4.6'
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
	python
)

ros_depends=(
)

depends=(
	${ros_depends[@]}
	python-yaml
	python-lxml
	python
)

_dir="urdf_parser_py-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/urdf_parser_py/archive/${pkgver}.tar.gz")
sha256sums=('4c0c8072aca5c69cc659545914bd05e481cf73a9d5b80d6b5e50bfecf9cb1442')

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
