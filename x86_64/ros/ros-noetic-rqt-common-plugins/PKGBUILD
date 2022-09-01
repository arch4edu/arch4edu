# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rqt_common_plugins metapackage provides ROS backend graphical tools suite that can be used on/off of robot runtime."
url='https://wiki.ros.org/rqt_common_plugins'

pkgname='ros-noetic-rqt-common-plugins'
pkgver='0.4.9'
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
	ros-noetic-rqt-bag-plugins
	ros-noetic-rqt-launch
	ros-noetic-rqt-action
	ros-noetic-rqt-msg
	ros-noetic-rqt-logger-level
	ros-noetic-rqt-top
	ros-noetic-rqt-service-caller
	ros-noetic-rqt-shell
	ros-noetic-rqt-graph
	ros-noetic-rqt-topic
	ros-noetic-rqt-web
	ros-noetic-rqt-py-common
	ros-noetic-rqt-bag
	ros-noetic-rqt-plot
	ros-noetic-rqt-publisher
	ros-noetic-rqt-console
	ros-noetic-rqt-srv
	ros-noetic-rqt-dep
	ros-noetic-rqt-image-view
	ros-noetic-rqt-py-console
	ros-noetic-rqt-reconfigure
)

depends=(
	${ros_depends[@]}
)

_dir="rqt_common_plugins-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_common_plugins/archive/${pkgver}.tar.gz")
sha256sums=('8e60424081e7e278b7f9bba214bc4cda0d86bee1a142556153946acf9437b391')

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
