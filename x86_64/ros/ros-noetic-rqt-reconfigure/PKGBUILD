# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This rqt plugin succeeds former dynamic_reconfigures GUI (reconfigure_gui), and provides the way to view and edit the parameters that are accessible via dynamic_reconfigure."
url='https://wiki.ros.org/rqt_reconfigure'

pkgname='ros-noetic-rqt-reconfigure'
pkgver='0.5.5'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-catkin
	ros-noetic-roslint
)

makedepends=(
	cmake
	ros-build-tools
	${ros_makedepends[@]}
	python-setuptools
)

ros_depends=(
	ros-noetic-dynamic-reconfigure
	ros-noetic-python-qt-binding
	ros-noetic-rospy
	ros-noetic-rqt-console
	ros-noetic-rqt-gui
	ros-noetic-rqt-gui-py
	ros-noetic-rqt-py-common
)

depends=(
	${ros_depends[@]}
	python-pyaml
)

_dir="rqt_reconfigure-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_reconfigure/archive/${pkgver}.tar.gz")
sha256sums=('325c1e1c2367a5d5a654df38317b51d1aa3e951921f6457b4de4411775e954df')

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
