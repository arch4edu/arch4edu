# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Sven-Hendrik Haase <svenstaro@gmail.com>
# Contributor: bartus <arch-user-repoᘓbartus.33mail.com>
# Contributor: pingplug <pingplug@foxmail.com>
# Contributor: cornholio <vigo.the.unholy.carpathian@gmail.com>

pkgname=hipmagma
pkgver=2.6.2
pkgrel=3
pkgdesc="Matrix Algebra on GPU and Multicore Architectures"
arch=('x86_64')
url="https://icl.cs.utk.edu/magma/"
license=('custom')
depends=('blas' 'lapack' 'rocm-hip-sdk')
makedepends=('gcc11-fortran' 'cmake' 'ninja')
optdepends=('python: for examples and tests'
            'gcc11-fortran: Fortran interface')
_pkgname="magma"
source=("${_pkgname}-${pkgver}.tar.gz::http://icl.cs.utk.edu/projectsfiles/${_pkgname}/downloads/${_pkgname}-${pkgver}.tar.gz"
        "find-hip.patch::https://bitbucket.org/avcxz/magma/commits/489c8b6a4ae180da65630edbfcc92728f665db6c/raw")
sha256sums=('75b554dab00903e2d10b972c913e50e7f88cbc62f3ae432b5a086c7e4eda0a71'
            'SKIP')
options=(!lto)

prepare() {
  cd ${_pkgname}-${pkgver}
  patch -Np1 < "$srcdir/find-hip.patch"
}

build() {
  cd ${_pkgname}-${pkgver}

  CC=/usr/bin/gcc-11 \
  CXX=/opt/rocm/g++-11 \
  FC=/usr/bin/gfortran-11 \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Bbuild \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DMAGMA_ENABLE_HIP=ON \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc
  ninja -C build
}

package() {
  cd "${_pkgname}-${pkgver}"
  DESTDIR="${pkgdir}" ninja -Cbuild install

  install -d "${pkgdir}"/usr/share/magma/example
  cp -r "${srcdir}"/magma-${pkgver}/example/* "${pkgdir}"/usr/share/magma/example/
  install -d "${pkgdir}"/usr/share/magma/testing
  cp -r "${srcdir}"/magma-${pkgver}/testing/* "${pkgdir}"/usr/share/magma/testing/
  install -Dm644 "${srcdir}"/magma-${pkgver}/COPYRIGHT "${pkgdir}"/usr/share/licenses/magma/LICENSE
}

# vim:set ts=2 sw=2 et:
