# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=calculix-precice
pkgver=2.20.2
pkgrel=1
pkgdesc="preCICE-adapter for the CSM code CalculiX"
url="https://github.com/${pkgname/calculix-/}/${pkgname/precice/adapter}"
license=(GPL-3.0-or-later)
arch=(x86_64)
depends=(calculix-ccx precice yaml-cpp) # pastix
makedepends=(gcc-fortran pandoc-cli)    # mono
optdepends=('man-db: manual pages for ccx_preCICE')
source=(${pkgname/precice/adapter}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  http://dhondt.de/ccx_${pkgver::4}.src.tar.bz2)
sha512sums=('fd71030b5b1f9f4275272cc58808fd343bc578703691eff1d9b26f025d5613c4a4fb4346a040b4978200fa5e7ead068f6b5eb0be80593f37fb09ba0485e301a3'
            '3888c1411ad42c6f2483cbf7d8994e8175ffa9ad4f0c4df224e2d16a7d80973d32f6a8cf10844255586d4f8e076fee99017cee5f2b9bb6576b82edcfe4b4ffb8')

prepare() {
  # https://github.com/precice/precice.github.io/blob/master/pages/docs/adapters/calculix/adapter-calculix-get-adapter.md?plain=1#L94
  sed -i 's/^FFLAGS = -Wall -O3 -fopenmp $(INCLUDES)/FFLAGS = -Wall -O3 -fopenmp -fallow-argument-mismatch $(INCLUDES)/' ${pkgname/precice/adapter}-${pkgver}/Makefile
  sed -i 's/^CFLAGS = -Wall/CFLAGS =-std=gnu11 -Wno-implicit-function-declaration -Wno-incompatible-pointer-types/' ${pkgname/precice/adapter}-${pkgver}/Makefile
  cd ${pkgname/precice/adapter}-${pkgver}/packaging
  pandoc manpage.md -s -t man -o ccx_preCICE.1
}

build() {
  cd ${pkgname/precice/adapter}-${pkgver}
  make CCX="${srcdir}/CalculiX/ccx_${pkgver::4}/src"
}

check() {
  cd ${pkgname/precice/adapter}-${pkgver}
  ./bin/ccx_preCICE -v || true
}

package() {
  cd ${pkgname/precice/adapter}-${pkgver}
  install -Dvm755 bin/ccx_preCICE -t ${pkgdir}/usr/bin
  install -Dm 644 LICENSE -t ${pkgdir}/usr/share/licenses/${pkgname}
  install -Dm 644 packaging/ccx_preCICE.1 -t ${pkgdir}/usr/share/man/man1/
  install -Dm 644 README.md -t ${pkgdir}/usr/share/doc/${pkgname}
}
