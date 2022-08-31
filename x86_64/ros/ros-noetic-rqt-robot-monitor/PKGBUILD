# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_robot_monitor displays diagnostics_agg topics messages that are published by diagnostic_aggregator."
url='https://wiki.ros.org/rqt_robot_monitor'

pkgname='ros-noetic-rqt-robot-monitor'
pkgver='0.5.14'
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
	ros-noetic-rqt-gui-py
	ros-noetic-diagnostic-msgs
	ros-noetic-qt-gui-py-common
	ros-noetic-rqt-gui
	ros-noetic-qt-gui
	ros-noetic-rqt-bag
	ros-noetic-python-qt-binding
	ros-noetic-rqt-py-common
	ros-noetic-rospy
)

depends=(
	${ros_depends[@]}
	python-rospkg
)

_dir="rqt_robot_monitor-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_robot_monitor/archive/${pkgver}.tar.gz")
sha256sums=('898cc073a4eb2cf9d90e3af536ed68cc097a3fd69708df93e7746fa8430f971d')

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
