# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Sven Schneider <archlinux.sandmann@googlemail.com>

pkgname=orocos-kdl-git
pkgver=1.5.3.r2.gfb840b0
pkgrel=1
pkgdesc="The Kinematics and Dynamics Library is a framework for modelling and computation of kinematic chains"
arch=('i686' 'x86_64')
url="https://www.orocos.org/kdl"
license=('GPL')
depends=(eigen cppunit)
makedepends=(cmake git)
provides=(orocos-kdl)
conflicts=(orocos-kdl)
source=(git+https://github.com/orocos/orocos_kinematics_dynamics)
sha256sums=('SKIP')

_dir=orocos_kinematics_dynamics
_pkgname=orocos_kdl

pkgver() {
  cd "${srcdir}/${_dir}"
  git describe --long --tags --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd "${srcdir}/${_dir}/${_pkgname}"

  mkdir -p build && cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr ..
  make
}

package() {
  cd "${srcdir}/${_dir}/${_pkgname}/build"
  make DESTDIR="${pkgdir}" install
}
