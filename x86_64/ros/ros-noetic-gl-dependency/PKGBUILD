# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This encapsulates the GL dependency for a specific ROS distribution and its Qt version."
url='https://wiki.ros.org/gl_dependency'

pkgname='ros-noetic-gl-dependency'
pkgver='1.1.2'
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
)

ros_depends=(
)

depends=(
	${ros_depends[@]}
	python-pyqt5
)

_dir="gl_dependency-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/gl_dependency/archive/${pkgver}.tar.gz")
sha256sums=('c0502c7cc5841e03bdc59f57c0461665a45ec03d7bd9cdda3cd147f87ca67b8c')

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
