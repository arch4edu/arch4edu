# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rosconsole_bridge is a package used in conjunction with console_bridge and rosconsole for connecting console_bridge-based logging to rosconsole-based logging."
url='https://wiki.ros.org/rosconsole_bridge'

pkgname='ros-noetic-rosconsole-bridge'
pkgver='0.5.4'
arch=('any')
pkgrel=2
license=('BSD')

ros_makedepends=(
	ros-noetic-rosconsole
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	console-bridge
)

ros_depends=(
	ros-noetic-rosconsole
)

depends=(
	${ros_depends[@]}
	console-bridge
)

_dir="rosconsole_bridge-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/rosconsole_bridge/archive/${pkgver}.tar.gz")
sha256sums=('d74931186eff823a2cf5af7122c6ed88e4c2bc5286055816517e6310d24a0730')

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
