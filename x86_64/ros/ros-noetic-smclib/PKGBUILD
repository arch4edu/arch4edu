# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - The State Machine Compiler (SMC) from https://smc.sourceforge.net/ converts a language-independent description of a state machine into the source code to support that state machine."
url='http://smc.sourceforge.net/'

pkgname='ros-noetic-smclib'
pkgver='1.8.6'
arch=('any')
pkgrel=2
license=('Mozilla Public License Version 1.1')

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

_dir="bond_core-${pkgver}/smclib"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/bond_core/archive/${pkgver}.tar.gz")
sha256sums=('33ec23816b57630c449b4a629504bd0112eeef5cee15652b3759ab11088a1e81')

prepare() {
    perl -0777 -pi -e 's/(?<!>)\n+ {4}//g' ${srcdir}/${_dir}/package.xml
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
