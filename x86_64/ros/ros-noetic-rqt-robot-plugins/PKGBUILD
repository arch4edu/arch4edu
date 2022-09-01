# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Metapackage of rqt plugins that are particularly used with robots during its operation."
url='https://wiki.ros.org/rqt_robot_plugins'

pkgname='ros-noetic-rqt-robot-plugins'
pkgver='0.5.8'
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
	ros-noetic-rqt-tf-tree
	ros-noetic-rqt-runtime-monitor
	ros-noetic-rqt-nav-view
	ros-noetic-rqt-pose-view
	ros-noetic-rqt-robot-steering
	ros-noetic-rqt-moveit
	ros-noetic-rqt-robot-dashboard
	ros-noetic-rqt-rviz
	ros-noetic-rqt-robot-monitor
)

depends=(
	${ros_depends[@]}
)

_dir="rqt_robot_plugins-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_robot_plugins/archive/${pkgver}.tar.gz")
sha256sums=('ed5e2d9fd1a54736ffd311b7e82699abeb9058a4e205b5e0f2c7671e69c41d7a')

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
