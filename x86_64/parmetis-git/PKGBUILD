# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ParMETIS
pkgname=${_base,,}-git
pkgver=r45.8ee6a37
pkgrel=2
arch=(x86_64)
pkgdesc="Parallel Graph Partitioning and Fill-reducing Matrix Ordering (git version)"
url="https://github.com/KarypisLab/${_base}"
license=('custom')
depends=(metis openmpi)
makedepends=(cmake git)
options=(docs)
source=(git+${url}.git#branch=main)
sha512sums=('SKIP')
provides=(${_base,,})
conflicts=(${_base,,})

pkgver() {
  cd ${_base}
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

prepare() {
  cd ${_base}
  sed -i 's|^CONFIG_FLAGS = .*|CONFIG_FLAGS = -DCMAKE_VERBOSE_MAKEFILE=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5|' Makefile
}

build() {
  cd ${_base}
  make config \
    shared=1 \
    cc=mpicc \
    prefix=/usr \
    gklib_path=/usr \
    metis_path=/usr
}

package() {
  cd ${_base}
  make install DESTDIR="${pkgdir}"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
