# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_dep provides a GUI plugin for visualizing the ROS dependency graph."
url='https://wiki.ros.org/rqt_dep'

pkgname='ros-noetic-rqt-dep'
pkgver='0.4.12'
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
	ros-noetic-rqt-graph
	ros-noetic-qt-gui-py-common
	ros-noetic-qt-gui
	ros-noetic-python-qt-binding
	ros-noetic-qt-dotgraph
)

depends=(
	${ros_depends[@]}
	python-rospkg
)

_dir="rqt_dep-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_dep/archive/${pkgver}.tar.gz")
sha256sums=('9a69cda0491aa8b1239c9aa9d8b5bb9f38827d85f5d60fecfd3a2a4636e1af92')

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
