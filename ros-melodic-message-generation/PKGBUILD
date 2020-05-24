# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Package modeling the build-time dependencies for generating language bindings of messages."
url='https://github.com/ros/message_generation'

pkgname='ros-melodic-message-generation'
pkgver='0.4.1'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
license=('BSD')

ros_makedepends=(
	ros-melodic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-melodic-geneus
	ros-melodic-gencpp
	ros-melodic-genpy
	ros-melodic-gennodejs
	ros-melodic-genlisp
	ros-melodic-genmsg
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
	[ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

	# Create the build directory.
	[ -d ${srcdir}/build ] || mkdir ${srcdir}/build
	cd ${srcdir}/build

	# Fix Python2/Python3 conflicts.
	/usr/share/ros-build-tools/fix-python-scripts.sh -v 3 ${srcdir}/${_dir}

	# Build the project.
	cmake ${srcdir}/${_dir} \
		-DCMAKE_BUILD_TYPE=Release \
		-DCATKIN_BUILD_BINARY_PACKAGE=ON \
		-DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
		-DPYTHON_EXECUTABLE=/usr/bin/python3 \
		-DSETUPTOOLS_DEB_LAYOUT=OFF
	make
}

package() {
	cd "${srcdir}/build"
	make DESTDIR="${pkgdir}/" install
}
