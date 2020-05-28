# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Javascript ROS message and service generators."
url='https://wiki.ros.org/gennodejs'

pkgname='ros-melodic-gennodejs'
pkgver='2.0.1'
_pkgver_patch=0
arch=('any')
pkgrel=2
license=('Apache 2.0')

ros_makedepends=(
	ros-melodic-genmsg
	ros-melodic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-melodic-genmsg
)

depends=(
	${ros_depends[@]}
)

_dir="gennodejs-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RethinkRobotics-opensource/gennodejs/archive/${pkgver}.tar.gz")
sha256sums=('6380efc25d0c80e0372d1f57dea5e3bd3ab05b537f0477a702fd472965035478')

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
		-DPYTHON_INCLUDE_DIR=/usr/include/python3.7m \
		-DPYTHON_LIBRARY=/usr/lib/libpython3.7m.so \
		-DPYTHON_BASENAME=.cpython-37m \
		-DSETUPTOOLS_DEB_LAYOUT=OFF
	make
}

package() {
	cd "${srcdir}/build"
	make DESTDIR="${pkgdir}/" install
}
