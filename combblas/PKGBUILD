# Maintainer: Christian Pfeiffer <cpfeiffer at live de>
# Contributor: Michael Straube <straubem gmx de>
# Contributor: xantares <xantares09 at hotmail dot com>

pkgname=combblas
pkgver=1.6.2
pkgrel=2
pkgdesc="Combinatorial BLAS Library"
arch=('x86_64')
url="http://gauss.cs.ucsb.edu/~aydin/CombBLAS/html/"
license=("MIT")
depends=('openmpi')
makedepends=('cmake')
_filename="CombBLAS_beta_16_2"
source=("http://gauss.cs.ucsb.edu/~aydin/CombBLAS_FILES/${_filename}.tgz")

sha512sums=('de63b6da77563cd1e074f44d6892c8d1dcb7aa9475f617b2de60239485e6dbd5965a305471f933fe175778a12fc6bb987a75f3631487b6461a382c5419b267aa')

prepare() {
  mkdir build
}

build() {
  cd build

  # Some tests are computationally heavy MPI stuff, so avoid them
  cmake "${srcdir}/${_filename}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING=OFF

  make
}

package() {
  cd build

  make DESTDIR="${pkgdir}" install

  # Remove OS X leftover files
  find "${pkgdir}" -name "*.DS_Store" -delete
  find "${pkgdir}" -name "._*" -delete

  install -Dm644 "${srcdir}/${_filename}/LICENSE" -t "${pkgdir}"/usr/share/licenses/$pkgname/

  # Add extra headers
  install -Dm644 "${srcdir}/${_filename}"/Applications/*.h -t "${pkgdir}"/usr/include/CombBLAS/Applications/
  install -Dm644 "${srcdir}/${_filename}"/BipartiteMatchings/*.h -t "${pkgdir}"/usr/include/CombBLAS/BipartiteMatchings/
}
