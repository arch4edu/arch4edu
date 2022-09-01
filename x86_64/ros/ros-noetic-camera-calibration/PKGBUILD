# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - camera_calibration allows easy calibration of monocular or stereo cameras using a checkerboard calibration target."
url='https://wiki.ros.org/camera_calibration'

pkgname='ros-noetic-camera-calibration'
pkgver='1.16.0'
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
	ros-noetic-std-srvs
	ros-noetic-image-geometry
	ros-noetic-cv-bridge
	ros-noetic-message-filters
	ros-noetic-sensor-msgs
	ros-noetic-rospy
)

depends=(
	${ros_depends[@]}
)

_dir="image_pipeline-${pkgver}/camera_calibration"
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
		-DSETUPTOOLS_DEB_LAYOUT=OFF
	make
}

package() {
	cd "${srcdir}/build"
	make DESTDIR="${pkgdir}/" install
}
