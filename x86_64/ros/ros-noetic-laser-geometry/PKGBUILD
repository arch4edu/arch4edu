# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This package contains a class for converting from a 2D laser scan as defined by sensor_msgs/LaserScan into a point cloud as defined by sensor_msgs/PointCloud or sensor_msgs/PointCloud2."
url='https://wiki.ros.org/laser_geometry'

pkgname='ros-noetic-laser-geometry'
pkgver='1.6.7'
_pkgver_patch=0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=4
license=('BSD')

ros_makedepends=(
	ros-noetic-cmake-modules
	ros-noetic-catkin
    ros-noetic-tf2-geometry-msgs
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-tf
	ros-noetic-tf2
	ros-noetic-angles
	ros-noetic-sensor-msgs
	ros-noetic-roscpp
)

depends=(
	${ros_depends[@]}
	boost
	eigen
	python-numpy
)

_dir="laser_geometry-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-perception/laser_geometry/archive/${pkgver}.tar.gz")
sha256sums=('334a1cb1e8846a80a9980f06e4ab01dedd15f85016ea9d7c6fa4f2a29b075760')

prepare(){
    sed -i '4s/11/17/' ./${_dir}/CMakeLists.txt
}

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
