# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - The package provides the environment variables ROS_VERSION, ROS_DISTRO, ROS_PACKAGE_PATH, and ROS_ETC_DIR."
url='https://wiki.ros.org/ros_environment'

pkgname='ros-noetic-ros-environment'
pkgver='1.3.2'
arch=('any')
pkgrel=1
license=('Apache License 2.0')

ros_makedepends=(
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
)

depends=(
	${ros_depends[@]}
)

_dir="ros_environment-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/ros_environment/archive/${pkgver}.tar.gz")
sha256sums=('c0bc78d606e85a5456ce669f33638d8e8872deadb08a745a8ae79874f61f58e3')

build() {
	# Use ROS environment variables.
	source /usr/share/ros-build-tools/clear-ros-env.sh
	[ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

	# Create the build directory.
	[ -d ${srcdir}/build ] || mkdir ${srcdir}/build
	cd ${srcdir}/build

	# Set python version for env hook
	ROS_PYTHON_VERSION=3

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
