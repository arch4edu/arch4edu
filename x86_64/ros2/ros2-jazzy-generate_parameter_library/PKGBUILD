# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-generate_parameter_library
pkgname=(
    'ros2-jazzy-parameter_traits'
    'ros2-jazzy-generate_parameter_library_py'
    'ros2-jazzy-generate_parameter_library'
    'ros2-jazzy-generate_parameter_library_example'
    'ros2-jazzy-generate_parameter_module_example'
    'ros2-jazzy-cmake_generate_parameter_module_example'
    'ros2-jazzy-generate_parameter_library_example_external'
)
pkgver=0.7.6
pkgrel=1
pkgdesc="Generate C++ and Python parameter libraries for ROS 2 Jazzy"
url="https://github.com/PickNikRobotics/generate_parameter_library"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy')
makedepends=(
    'cmake'
    'python-colcon-common-extensions'
    'python-jinja'
    'python-typeguard'
    'python-yaml'
    'ros2-jazzy-rsl'
    'ros2-jazzy-tcb_span'
    'ros2-jazzy-tl_expected'
    'ros2-jazzy-ros2_control_cmake'
    'tl-expected'
    'eigen'
    'fmt'
)
source=("$pkgbase-$pkgver.tar.gz::https://github.com/PickNikRobotics/generate_parameter_library/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('2fed256eb49c3e01df8becfe6eb064ea9352ea6681b52bf120546cdf3665369e')

_srcname="generate_parameter_library-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    cd "$srcdir/$_srcname"
    colcon build \
        --install-base "$srcdir/install" \
        --cmake-args -DCMAKE_BUILD_TYPE=None -DBUILD_TESTING=OFF -Wno-dev
}

_install_sub() {
    local sub="$1"
    install -d "$pkgdir/opt/ros/jazzy"
    cp -a "$srcdir/install/$sub/." "$pkgdir/opt/ros/jazzy/"
    rm -f "$pkgdir/opt/ros/jazzy"/COLCON_IGNORE \
          "$pkgdir/opt/ros/jazzy"/.colcon_install_layout \
          "$pkgdir/opt/ros/jazzy"/setup.* \
          "$pkgdir/opt/ros/jazzy"/local_setup.* \
          "$pkgdir/opt/ros/jazzy"/_local_setup_util_*.py \
          "$pkgdir/opt/ros/jazzy"/colcon-core-package-selection* 2>/dev/null
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-parameter_traits() {
    arch=('any')
    depends=('ros2-jazzy' 'ros2-jazzy-rsl' 'ros2-jazzy-tcb_span' 'ros2-jazzy-tl_expected' 'fmt')
    _install_sub parameter_traits
}

package_ros2-jazzy-generate_parameter_library_py() {
    arch=('any')
    depends=('python-jinja' 'python-typeguard' 'python-yaml')
    _install_sub generate_parameter_library_py
}

package_ros2-jazzy-generate_parameter_library() {
    arch=('any')
    depends=('ros2-jazzy' 'ros2-jazzy-generate_parameter_library_py' 'ros2-jazzy-parameter_traits' 'ros2-jazzy-rsl' 'ros2-jazzy-tcb_span' 'ros2-jazzy-tl_expected' 'tl-expected' 'fmt')
    _install_sub generate_parameter_library
}

package_ros2-jazzy-generate_parameter_library_example() {
    depends=('ros2-jazzy' 'ros2-jazzy-generate_parameter_library' 'ros2-jazzy-ros2_control_cmake')
    _install_sub generate_parameter_library_example
}

package_ros2-jazzy-generate_parameter_module_example() {
    arch=('any')
    depends=('ros2-jazzy' 'ros2-jazzy-generate_parameter_library' 'ros2-jazzy-generate_parameter_library_py')
    _install_sub generate_parameter_module_example
}

package_ros2-jazzy-cmake_generate_parameter_module_example() {
    arch=('any')
    depends=('ros2-jazzy' 'ros2-jazzy-generate_parameter_library')
    _install_sub cmake_generate_parameter_module_example
}

package_ros2-jazzy-generate_parameter_library_example_external() {
    depends=('ros2-jazzy' 'ros2-jazzy-generate_parameter_library_example' 'ros2-jazzy-ros2_control_cmake')
    _install_sub generate_parameter_library_example_external
}
