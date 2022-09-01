# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - A metapackage to aggregate several packages."
url='https://github.com/ros/metapackages'

pkgname='ros-noetic-desktop'
pkgver='1.5.0'
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
	ros-noetic-angles
	ros-noetic-common-tutorials
	ros-noetic-urdf-tutorial
	ros-noetic-geometry-tutorials
	ros-noetic-visualization-tutorials
	ros-noetic-viz
	ros-noetic-roslint
	ros-noetic-robot
	ros-noetic-ros-tutorials
)

depends=(
	${ros_depends[@]}
)

_dir="metapackages-${pkgver}/desktop"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/metapackages/archive/${pkgver}.tar.gz")
sha256sums=('5e055b7528d088cf62035d88c78cfd5aefcac2a96d0ce2ac62242f6d6f76d3b0')

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
