# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Package modeling the build-time dependencies for generating language bindings of messages."
url='https://github.com/ros/message_generation'

pkgname='ros-noetic-message-generation'
pkgver='0.4.1'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
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
	ros-noetic-geneus
	ros-noetic-gencpp
	ros-noetic-genpy
	ros-noetic-gennodejs
	ros-noetic-genlisp
	ros-noetic-genmsg
)

depends=(
	${ros_depends[@]}
)

_dir="message_generation-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/message_generation/archive/${pkgver}.tar.gz")
sha256sums=('90ab9649f594d5d007d735bd056f777e5f72bfb4f11f2b891fa5c5139f0a5e2f')

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
