pkgdesc="ROS - image_geometry contains C++ and Python libraries for interpreting images geometrically."
url='https://wiki.ros.org/image_geometry'

pkgname='ros-noetic-image-geometry'
pkgver='1.16.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-catkin
	ros-noetic-sensor-msgs
)

makedepends=(
	'cmake'
	'ros-build-tools'
	"${ros_makedepends[@]}"
	opencv
)

ros_depends=(
)

depends=(
	"${ros_depends[@]}"
	opencv
)

_dir="vision_opencv-${pkgver}/image_geometry"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-perception/vision_opencv/archive/${pkgver}.tar.gz")
sha256sums=('046f3bac5dcdaea5678bf5e6be10d895bbd670cc16c7b97ba4c1a6b661f8557e')

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
