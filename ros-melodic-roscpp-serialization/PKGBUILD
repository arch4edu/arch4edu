pkgdesc="ROS - roscpp_serialization contains the code for serialization as described in MessagesSerializationAndAdaptingTypes."
url='https://wiki.ros.org/roscpp_serialization'

pkgname='ros-melodic-roscpp-serialization'
pkgver='0.6.13'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
	ros-melodic-roscpp-traits
	ros-melodic-cpp-common
	ros-melodic-rostime
	ros-melodic-catkin
)

makedepends=(
	'cmake'
	'ros-build-tools'
	${ros_makedepends[@]}
)

ros_depends=(
	ros-melodic-roscpp-traits
	ros-melodic-cpp-common
	ros-melodic-rostime
)

depends=(
	${ros_depends[@]}
)

_dir="roscpp_core-${pkgver}/roscpp_serialization"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/roscpp_core/archive/${pkgver}.tar.gz")
sha256sums=('6740da6424373c8ffb075b30272f7a46804a76015649bc4f54fd1963d50a1e49')

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
