# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=GKlib
pkgname=${_base,,}
pkgver=5.1.1
pkgrel=3
pkgdesc="A library of various helper routines and frameworks used by many of the lab's software"
arch=(x86_64)
url="https://github.com/KarypisLab/${_base}"
license=(Apache)
depends=(pcre) # openmp
makedepends=(cmake)
source=(${url}/archive/METIS-v${pkgver}-DistDGL-0.5.tar.gz
  gk_GetProcVmPeak.patch::${url}/commit/33b8c8bb8dada74b824badff961532f11d0d5e1c.patch
  gk_creadfilebin.patch::${url}/commit/1403a04bc40a306d09adfccced7d903d69de040a.patch)
sha512sums=('248db76a51c66ae9b94ac759e19f6e5504dd75d6e1b3a1c0f8a1f2db899099ec7b62328213bfdefef8c70b6be40f122a27d427c016cbf4419fd1e032a52567ca'
  '10840132076a59acb24228d4caf46a1db19bd37f6e85e43b990ca85d2dd6f5173f97532d1d9305bed6895d6328536edc7c47c518e035e19bd40fa79b62861cf9'
  '9bf8920c17760198047c6afdd65ac0cc12557a0caf975cf2ed93a2f0b966955ddb7a68e10cbb890570bf8b55dd29193438e166fedba04d629dd3ea8ba28427a7')

prepare() {
  cd ${_base}-METIS-v${pkgver}-DistDGL-0.5
  # https://github.com/KarypisLab/METIS/issues/54
  patch -p1 -i ../gk_GetProcVmPeak.patch
  patch -p1 -i ../gk_creadfilebin.patch
}

build() {
  cmake \
    -S ${_base}-METIS-v${pkgver}-DistDGL-0.5 \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_C_COMPILER=gcc \
    -DGDB=ON \
    -DGKRAND=ON \
    -DGKREGEX=OFF \
    -DGPROF=ON \
    -DOPENMP=ON \
    -DPCRE=ON \
    -Wno-dev
  cmake --build build --target all
}
package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${_base}-METIS-v${pkgver}-DistDGL-0.5/LICENSE.txt -t ${pkgdir}/usr/share/licenses/${_base}
}
