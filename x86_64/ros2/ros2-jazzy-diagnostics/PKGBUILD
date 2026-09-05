# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-diagnostics
pkgname=(
    'ros2-jazzy-diagnostic_updater'
    'ros2-jazzy-diagnostic_aggregator'
    'ros2-jazzy-diagnostic_common_diagnostics'
    'ros2-jazzy-diagnostic_remote_logging'
    'ros2-jazzy-self_test'
    'ros2-jazzy-diagnostics'
)
pkgver=4.2.7
pkgrel=1
pkgdesc="Diagnostics packages for ROS 2 Jazzy"
url="https://github.com/ros/diagnostics"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy')
makedepends=('cmake')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros/diagnostics/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('d8ae00740db5eb3a23a7fa5f3cfa7e3c0d1082edcad5209ab84900d0368908fd')

_srcname="diagnostics-$pkgver"

_build_cmake() {
    local _sub="$1"
    shift

    source /opt/ros/jazzy/setup.bash

    local _prefix='' _dep
    for _dep in "$@"; do
        _prefix+="$srcdir/_staging/$_dep/opt/ros/jazzy:"
    done

    CMAKE_PREFIX_PATH="${_prefix}${CMAKE_PREFIX_PATH}" \
        cmake -B "$srcdir/build-$_sub" -S "$srcdir/$_srcname/$_sub" \
            -DCMAKE_BUILD_TYPE='None' \
            -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
            -DBUILD_TESTING=OFF \
            -Wno-dev
    cmake --build "$srcdir/build-$_sub"
    DESTDIR="$srcdir/_staging/$_sub" cmake --install "$srcdir/build-$_sub"
}

build() {
    rm -rf "$srcdir/_staging"

    # Compiled nodes embed __FILE__ build paths.
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake diagnostic_updater
    _build_cmake diagnostic_aggregator
    _build_cmake diagnostic_common_diagnostics diagnostic_updater
    _build_cmake diagnostic_remote_logging
    _build_cmake self_test diagnostic_updater
    _build_cmake diagnostics
}

package_ros2-jazzy-diagnostic_updater() {
    pkgdesc="Tools for easily updating ROS 2 diagnostics"
    depends=('ros2-jazzy')

    cp -a "$srcdir/_staging/diagnostic_updater/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-diagnostic_aggregator() {
    pkgdesc="Aggregates and categorizes ROS 2 diagnostic messages"
    depends=('ros2-jazzy')

    cp -a "$srcdir/_staging/diagnostic_aggregator/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-diagnostic_common_diagnostics() {
    pkgdesc="Predefined diagnostic nodes for monitoring Linux and ROS 2 systems"
    arch=('any')
    depends=('ros2-jazzy' 'ros2-jazzy-diagnostic_updater' 'lm_sensors' 'python-psutil' 'python-ntplib')

    cp -a "$srcdir/_staging/diagnostic_common_diagnostics/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-diagnostic_remote_logging() {
    pkgdesc="Remote logging for ROS 2 diagnostics (InfluxDB)"
    depends=('ros2-jazzy' 'curl')

    cp -a "$srcdir/_staging/diagnostic_remote_logging/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-self_test() {
    pkgdesc="Self-test tools for ROS 2 diagnostics"
    depends=('ros2-jazzy' 'ros2-jazzy-diagnostic_updater')

    cp -a "$srcdir/_staging/self_test/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-diagnostics() {
    pkgdesc="Metapackage for the ROS 2 diagnostics suite"
    arch=('any')
    depends=(
        'ros2-jazzy-diagnostic_updater'
        'ros2-jazzy-diagnostic_aggregator'
        'ros2-jazzy-diagnostic_common_diagnostics'
        'ros2-jazzy-diagnostic_remote_logging'
        'ros2-jazzy-self_test'
    )

    cp -a "$srcdir/_staging/diagnostics/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
