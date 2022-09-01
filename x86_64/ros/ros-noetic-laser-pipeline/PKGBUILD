# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Meta-package of libraries for processing laser data, including converting laser data into 3D representations."
url='https://wiki.ros.org/laser_pipeline'

pkgname='ros-noetic-laser-pipeline'
pkgver='1.6.4'
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
	ros-noetic-laser-geometry
	ros-noetic-laser-assembler
	ros-noetic-laser-filters
)

depends=(
	${ros_depends[@]}
)

_dir="laser_pipeline-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-perception/laser_pipeline/archive/${pkgver}.tar.gz")
sha256sums=('4016fac551a4e60166aa152412212e0091937cd8b34f39e1696c405a8a2c11bd')

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
