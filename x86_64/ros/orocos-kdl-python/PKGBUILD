# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Sven Schneider <archlinux.sandmann@googlemail.com>

pkgname=orocos-kdl-python
_dir=orocos_kinematics_dynamics
_pkgname=python_orocos_kdl
pkgver=1.5.1
pkgrel=1
pkgdesc="The Kinematics and Dynamics Library is a framework for modelling and computation of kinematic chains (Python binding)"
arch=('i686' 'x86_64')
url="https://www.orocos.org/kdl"
license=('GPL')
depends=('orocos-kdl' 'python-sip4')
makedepends=('cmake' 'sip4')

# Git commit has for version-specific submodules
pkgver_pybind11='787d2c88cafa4d07fb38c9519c485a86323cfcf4' # {_pkgname}/pybind11

source=("https://github.com/orocos/${_dir}/archive/v${pkgver}.tar.gz"
        "pybind11.tar.gz::https://github.com/pybind/pybind11/archive/${pkgver_pybind11}.tar.gz"
)
sha512sums=('9774b76b755ea81168390643813789783f60d0b1cdb46cd250e3e0d27f75a6cf2fd3bfd2081c04e30a14ff4fc70d0080c9b43b82ee181c2dda82f23f052b338d'
            'e878a81924670b1e125804311c1c04552e8bd37ff1b67b73e6091cdcf5a874b5d6b8244478aef4aaa8a07862f1f865beb244e85016626724b5768d73c5c99337')

prepare() {
  pybinddir="pybind11-${pkgver_pybind11}"

  # Copy in the pybind11 source
  rm -rf "${srcdir}/${_dir}-${pkgver}/${_pkgname}/pybind11"
  cp -R "${srcdir}/${pybinddir}" "${srcdir}/${_dir}-${pkgver}/${_pkgname}/pybind11"
}

build() {
  cd "${srcdir}/${_dir}-${pkgver}/${_pkgname}"
  mkdir -p build && cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
        -DPYTHON_VERSION=3 \
        ..
  make
}

package() {
  cd "${srcdir}/${_dir}-${pkgver}/${_pkgname}/build"
  make DESTDIR="${pkgdir}" install
  find ${pkgdir}/usr -maxdepth 1 -type f -exec rm {} \;
}
