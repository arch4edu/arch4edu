# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Provides nodes to assemble point clouds from either LaserScan or PointCloud messages."
url='https://wiki.ros.org/laser_assembler'

pkgname='ros-noetic-laser-assembler'
pkgver='1.7.8'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-filters
	ros-noetic-laser-geometry
	ros-noetic-rostest
	ros-noetic-catkin
	ros-noetic-tf
	ros-noetic-message-generation
	ros-noetic-roscpp
	ros-noetic-message-filters
	ros-noetic-sensor-msgs
	ros-noetic-pluginlib
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-filters
	ros-noetic-laser-geometry
	ros-noetic-message-filters
	ros-noetic-tf
	ros-noetic-roscpp
	ros-noetic-message-runtime
	ros-noetic-sensor-msgs
	ros-noetic-pluginlib
)

depends=(
	${ros_depends[@]}
)

_dir="laser_assembler-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-perception/laser_assembler/archive/${pkgver}.tar.gz")
sha256sums=('cf2e8649f6df73d63c5ff0a65dea8cf21ce3f644ce47c7955a165a94d3a1ded9')

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
