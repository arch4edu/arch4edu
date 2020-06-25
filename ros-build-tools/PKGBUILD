# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Sean Greenslade <zootboysean@gmail.com>
# Contributor: Benjamin Chretien <chretien+aur at lirmm dot fr>
# Contributor: Oskar Roesler <oskar@oskar-roesler.de>

pkgdesc='Utilities for building Arch packages for ROS stacks.'
url="https://github.com/acxz/pkgbuilds/tree/master/ros-build-tools"

pkgname='ros-build-tools'
pkgver='0.3.2'
arch=('any')
pkgrel=1
license=('BSD')
makedepends=()
depends=('bash')

pkg_destination_dir="/usr/share/ros-build-tools"

source=('clear-ros-env.sh')

sha256sums=('9626b8e5f3865f5640660f4a7f6a00afc4db8448b95329b4d5a64bd691677a88')

package() {
  mkdir -p ${pkgdir}${pkg_destination_dir}
  for file in "${source[@]}"; do
    cp $file ${pkgdir}${pkg_destination_dir}/$file
  done
}
