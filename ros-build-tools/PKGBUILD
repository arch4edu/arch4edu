# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Sean Greenslade <zootboysean@gmail.com>
# Contributor: Benjamin Chretien <chretien+aur at lirmm dot fr>
# Contributor: Oskar Roesler <oskar@oskar-roesler.de>

pkgdesc='Utilities for building Arch packages for ROS stacks.'
url="https://github.com/acxz/pkgbuilds/tree/master/ros-build-tools"

pkgname='ros-build-tools'
pkgver='0.3.1'
arch=('any')
pkgrel=3
license=('BSD')
makedepends=()
optdepends=('python' 'python-argparse' 'python-yaml' 'python-termcolor' 'python-certifi')
depends=('bash')

pkg_destination_dir="/usr/share/ros-build-tools"

source=('fix-python-scripts.sh'
        'clear-ros-env.sh'
        'create_pkgbuild.py')

sha256sums=('5528486d640d91136276edda2075aefc06f360e6297e556051bae57b9479aeda'
            '9626b8e5f3865f5640660f4a7f6a00afc4db8448b95329b4d5a64bd691677a88'
            '6171500f4e807e170f3705277032107b3902502a7fcccf8ab5b300a35580ebf7')
build() {
  return 0
}

package() {
  mkdir -p ${pkgdir}${pkg_destination_dir}
  for file in "${source[@]}"; do
    cp $file ${pkgdir}${pkg_destination_dir}/$file
  done
}
