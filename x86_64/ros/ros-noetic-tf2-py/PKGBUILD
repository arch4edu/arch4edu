# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - The tf2_py package."
url='https://wiki.ros.org/tf2_py'

pkgname='ros-noetic-tf2-py'
pkgver='0.7.6'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-tf2
	ros-noetic-rospy
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-tf2
	ros-noetic-rospy
)

depends=(
	${ros_depends[@]}
)

_dir="geometry2-${pkgver}/tf2_py"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/geometry2/archive/${pkgver}.tar.gz")
sha256sums=('cd6014745564bc9fc926999820a22742058a3a0bafd4b71795324026d4491db3')

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
