# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Compressed_depth_image_transport provides a plugin to image_transport for transparently sending depth images (raw, floating-point) using PNG compression."
url='https://wiki.ros.org/image_transport_plugins'

pkgname='ros-noetic-compressed-depth-image-transport'
pkgver='1.14.0'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-catkin
	ros-noetic-cv-bridge
	ros-noetic-dynamic-reconfigure
	ros-noetic-image-transport
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-cv-bridge
	ros-noetic-dynamic-reconfigure
	ros-noetic-image-transport
)

depends=(
	${ros_depends[@]}
)

_dir="image_transport_plugins-${pkgver}/compressed_depth_image_transport"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-perception/image_transport_plugins/archive/${pkgver}.tar.gz")
sha256sums=('eed856edeb26c66c1e1730a8c8b26ea6dec03d2f9a3c6db0462767106f9e73d8')

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
