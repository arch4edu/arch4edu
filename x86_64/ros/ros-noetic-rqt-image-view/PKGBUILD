pkgdesc="ROS - rqt_image_view provides a GUI plugin for displaying images using image_transport."
url='https://wiki.ros.org/rqt_image_view'

pkgname='ros-noetic-rqt-image-view'
pkgver='0.4.16'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=3
license=('BSD')

ros_makedepends=(
	ros-noetic-rqt-gui-cpp
	ros-noetic-geometry-msgs
	ros-noetic-catkin
	ros-noetic-cv-bridge
	ros-noetic-rqt-gui
	ros-noetic-sensor-msgs
	ros-noetic-image-transport
)

makedepends=(
	'cmake'
	'ros-build-tools'
    'boost'
	${ros_makedepends[@]}
	qt5-base
)

ros_depends=(
	ros-noetic-rqt-gui-cpp
	ros-noetic-geometry-msgs
	ros-noetic-cv-bridge
	ros-noetic-rqt-gui
	ros-noetic-sensor-msgs
	ros-noetic-image-transport
)

depends=(
	${ros_depends[@]}
)

_dir="rqt_image_view-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/rqt_image_view/archive/${pkgver}.tar.gz")
sha256sums=('8fc609aefd0faf9d2b7df62add6e11310f43e5f5499ba203e2e81899ac2b8d30')

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
        -DCMAKE_CXX_STANDARD=17 \
		-DSETUPTOOLS_DEB_LAYOUT=OFF
	make
}

package() {
	cd "${srcdir}/build"
	make DESTDIR="${pkgdir}/" install
}
