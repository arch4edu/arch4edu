# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Sven Schneider <archlinux.sandmann@googlemail.com>

pkgname=orocos-kdl
pkgver=1.5.1
pkgrel=1
pkgdesc="The Kinematics and Dynamics Library is a framework for modelling and computation of kinematic chains"
arch=('i686' 'x86_64')
url="https://www.orocos.org/kdl"
license=('GPL')
depends=(eigen)
makedepends=(cmake)
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/orocos/orocos_kinematics_dynamics/archive/v${pkgver}.tar.gz")
sha256sums=('5acb90acd82b10971717aca6c17874390762ecdaa3a8e4db04984ea1d4a2af9b')

_dir=orocos_kinematics_dynamics
_pkgname=orocos_kdl

build() {
  cd "${srcdir}/${_dir}-${pkgver}/${_pkgname}"

  cmake -DCMAKE_INSTALL_PREFIX=/usr .
  make
}

package() {
  cd "${srcdir}/${_dir}-${pkgver}/${_pkgname}"
  make DESTDIR="${pkgdir}" install
  find ${pkgdir}/usr -maxdepth 1 -type f -exec rm {} \;
}
