# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rosgraph contains the rosgraph command-line tool, which prints information about the ROS Computation Graph."
url='https://wiki.ros.org/rosgraph'

pkgname='ros-noetic-rosgraph'
pkgver='1.16.0'
arch=('any')
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
)

depends=(
	${ros_depends[@]}
	python-yaml
	python-netifaces
	python-rospkg
)

_dir="ros_comm-${pkgver}/tools/rosgraph"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/ros_comm/archive/${pkgver}.tar.gz"
        "frame.patch"::"https://github.com/ros/ros_comm/pull/2331.patch")
sha256sums=('0a51857a50cf646db4af85469cb0e4877b1484f7aa0c00ec65a8be7ff574a886'
            'SKIP')

prepare() {
  cd "${srcdir}/ros_comm-${pkgver}"
  patch -Np1 -i "${srcdir}/frame.patch"
}


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
