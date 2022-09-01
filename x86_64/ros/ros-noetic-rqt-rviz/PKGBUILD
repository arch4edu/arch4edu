# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_rviz provides a GUI plugin embedding RViz."
url='https://wiki.ros.org/rqt_rviz'

pkgname='ros-noetic-rqt-rviz'
pkgver='0.7.0'
_pkgver_patch=0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-rviz
	ros-noetic-rqt-gui-cpp
	ros-noetic-catkin
	ros-noetic-rqt-gui
	ros-noetic-pluginlib
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	boost
	qt5-base
)

ros_depends=(
	ros-noetic-rqt-gui
	ros-noetic-rqt-gui-cpp
	ros-noetic-rviz
	ros-noetic-pluginlib
)

depends=(
	${ros_depends[@]}
	boost
)

_dir="rqt_rviz-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_rviz/archive/${pkgver}.tar.gz")
sha256sums=('3b3970c40d01a48a6f30f729cd4447d932268602cd603797927d51c8dadc0175')

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
