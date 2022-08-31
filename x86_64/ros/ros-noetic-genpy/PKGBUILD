# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - Python ROS message and service generators."
url='https://wiki.ros.org/genpy'

pkgname='ros-noetic-genpy'
pkgver='0.6.15'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-genmsg
	ros-noetic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-noetic-genmsg
)

depends=(
	${ros_depends[@]}
	python-yaml
)

_dir="genpy-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/genpy/archive/${pkgver}.tar.gz")
sha256sums=('0c0b45c03523dab9d526641e13589c4221ad9dc826bba6e567af2a752350250b')

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
