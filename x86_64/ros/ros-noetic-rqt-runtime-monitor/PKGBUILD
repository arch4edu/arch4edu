# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_runtime_monitor provides a GUI plugin viewing DiagnosticsArray messages."
url='https://wiki.ros.org/rqt_runtime_monitor'

pkgname='ros-noetic-rqt-runtime-monitor'
pkgver='0.5.9'
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
	ros-noetic-qt-gui
	ros-noetic-python-qt-binding
	ros-noetic-rqt-gui
	ros-noetic-rospy
)

depends=(
	${ros_depends[@]}
	python-rospkg
)

_dir="rqt_runtime_monitor-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_runtime_monitor/archive/${pkgver}.tar.gz")
sha256sums=('f1535345853d5e473c64c5d8e6c480621a99ec4ed58f0ed6a80d3845a2f8ad8a')

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
