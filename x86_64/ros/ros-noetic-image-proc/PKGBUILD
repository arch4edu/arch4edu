pkgdesc="ROS - Single image rectification and color processing."
url='https://wiki.ros.org/image_proc'

pkgname='ros-noetic-image-proc'
pkgver='1.16.0'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
license=('BSD')

ros_makedepends=(
	ros-noetic-image-geometry
	ros-noetic-nodelet
	ros-noetic-dynamic-reconfigure
	ros-noetic-catkin
	ros-noetic-cv-bridge
	ros-noetic-roscpp
	ros-noetic-sensor-msgs
	ros-noetic-nodelet-topic-tools
	ros-noetic-image-transport
       ros-noetic-camera-calibration-parsers
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	boost
)

ros_depends=(
	ros-noetic-image-geometry
	ros-noetic-nodelet
	ros-noetic-dynamic-reconfigure
	ros-noetic-cv-bridge
	ros-noetic-roscpp
	ros-noetic-sensor-msgs
	ros-noetic-nodelet-topic-tools
	ros-noetic-image-transport
       ros-noetic-camera-calibration-parsers
	ros-noetic-rostest
)

depends=(
	${ros_depends[@]}
)

_dir="image_pipeline-${pkgver}/image_proc"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-perception/image_pipeline/archive/${pkgver}.tar.gz")
sha256sums=('310004d402930a059bb2c4811301e6f8aabc517143d094662de7e047e6e2b429')

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
