# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_publisher provides a GUI plugin for publishing arbitrary messages with fixed or computed field values."
url='https://wiki.ros.org/rqt_publisher'

pkgname='ros-noetic-rqt-publisher'
pkgver='0.4.10'
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
	ros-noetic-rqt-py-common
	ros-noetic-rqt-gui-py
	ros-noetic-qt-gui-py-common
	ros-noetic-rosmsg
	ros-noetic-python-qt-binding
	ros-noetic-rqt-gui
	ros-noetic-roslib
)

depends=(
	${ros_depends[@]}
	python-rospkg
)

_dir="rqt_publisher-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_publisher/archive/${pkgver}.tar.gz")
sha256sums=('d2e8a127d6ca0cc5929b62bf333195c4717a49112a133bbc2d9040d242ce23c2')

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
