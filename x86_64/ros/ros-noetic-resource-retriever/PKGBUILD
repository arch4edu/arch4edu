# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This package retrieves data from url-format files such as http://, ftp://, package:// file://, etc., and loads the data into memory."
url='https://wiki.ros.org/resource_retriever'

pkgname='ros-noetic-resource-retriever'
pkgver='1.12.7'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-noetic-rosconsole
	ros-noetic-catkin
	ros-noetic-roslib
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
	boost
	curl
)

ros_depends=(
	ros-noetic-rosconsole
	ros-noetic-roslib
)

depends=(
	${ros_depends[@]}
	boost
	python-rospkg
	curl
)

_dir="resource_retriever-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/resource_retriever/archive/${pkgver}.tar.gz")
sha256sums=('5e01da1e97915ef73b169955f4ec311ee292e3f01a3b465f6220bd8662f8e056')

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
        -DCMAKE_CXX_STANDARD=17 \
		-DSETUPTOOLS_DEB_LAYOUT=OFF
	make
}

package() {
	cd "${srcdir}/build"
	make DESTDIR="${pkgdir}/" install
}
