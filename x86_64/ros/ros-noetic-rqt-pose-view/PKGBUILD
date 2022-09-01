# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_pose_view provides a GUI plugin for visualizing 3D poses."
url='https://wiki.ros.org/rqt_pose_view'

pkgname='ros-noetic-rqt-pose-view'
pkgver='0.5.11'
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
	ros-noetic-gl-dependency
	ros-noetic-tf
	ros-noetic-rostopic
	ros-noetic-python-qt-binding
	ros-noetic-rqt-gui
	ros-noetic-rospy
	ros-noetic-geometry-msgs
)

depends=(
	${ros_depends[@]}
	python-opengl
	python-rospkg
)

_dir="rqt_pose_view-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_pose_view/archive/${pkgver}.tar.gz")
sha256sums=('44abf89dbde2c52cbe8feb11cc58e94439b31dd09be85989eee2cf38e91eab1c')

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
