# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_py_console is a Python GUI plugin providing an interactive Python console."
url='https://wiki.ros.org/rqt_py_console'

pkgname='ros-noetic-rqt-py-console'
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
	ros-noetic-rqt-gui-py
	ros-noetic-qt-gui-py-common
	ros-noetic-qt-gui
	ros-noetic-python-qt-binding
	ros-noetic-rqt-gui
	ros-noetic-rospy
)

depends=(
	${ros_depends[@]}
	python-rospkg
)

_dir="rqt_py_console-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_py_console/archive/${pkgver}.tar.gz")
sha256sums=('2478c0255758c5e45f0b4daf24fa447716d94dacfe05598fcc1a2192df518b95')

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
