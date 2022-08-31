pkgdesc="ROS - Underlying data libraries for roscpp messages."
url='https://wiki.ros.org/roscpp_core'

pkgname='ros-noetic-roscpp-core'
pkgver='0.7.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
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
	ros-noetic-roscpp-traits
	ros-noetic-cpp-common
	ros-noetic-rostime
	ros-noetic-roscpp-serialization
)

depends=(
	${ros_depends[@]}
)

_dir="roscpp_core-${pkgver}/roscpp_core"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/roscpp_core/archive/${pkgver}.tar.gz")
sha256sums=('a2aa77814ed97b48995c872a405c51f6b0f1ab9d40e38ece483852bbd273ad7b')

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
