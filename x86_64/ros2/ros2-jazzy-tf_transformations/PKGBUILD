# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=tf_transformations
pkgname=ros2-jazzy-tf_transformations
pkgver=1.1.1
pkgrel=1
pkgdesc="Reimplementation of the tf/transformations.py library for common Python spatial operations"
url="https://index.ros.org/p/tf_transformations/"
arch=('any')
license=('BSD-3-Clause')
makedepends=('python-colcon-common-extensions' 'python-setuptools')
depends=('ros2-jazzy' 'python-transforms3d' 'python-numpy')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/DLu/tf_transformations/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('1965cc33941e78a8f5469e8f243960d95264ca7e31ac4dd26577db7cfda3c427')

build() {
    source /opt/ros/jazzy/setup.bash

    mkdir -p "$srcdir/ws/src"
    ln -sfn "$srcdir/$_pkgname-$pkgver" "$srcdir/ws/src/$_pkgname"

    cd "$srcdir/ws"
    colcon build --merge-install \
        --install-base "$srcdir/install" \
        --cmake-args -DBUILD_TESTING=OFF
}

package() {
    install -d "$pkgdir/opt/ros/jazzy"
    cp -a "$srcdir/install/." "$pkgdir/opt/ros/jazzy/"

    # Strip colcon workspace bookkeeping; keep only the package payload.
    rm -f "$pkgdir/opt/ros/jazzy"/COLCON_IGNORE \
          "$pkgdir/opt/ros/jazzy"/.colcon_install_layout \
          "$pkgdir/opt/ros/jazzy"/setup.* \
          "$pkgdir/opt/ros/jazzy"/local_setup.* \
          "$pkgdir/opt/ros/jazzy"/_local_setup_util_*.py

    install -Dm644 "$srcdir/$_pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
