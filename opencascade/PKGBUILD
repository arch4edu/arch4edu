# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Florian Pritz <bluewind@xinu.at>
# Contributor: Giuseppe Borzi <gborzi@ieee.org>
# Contributor: Brice Méalier <mealier_brice@yahoo.fr>
# Contributor: Michele Mocciola <mickele>

pkgname=opencascade
pkgver=7.2.0p1
_pkgver=V${pkgver//./_}
pkgrel=1
pkgdesc="Open CASCADE Technology, 3D modeling & numerical simulation"
arch=('x86_64')
url="http://www.opencascade.org"
license=('custom')
depends=('tk' 'vtk' 'gl2ps' 'ffmpeg' 'freeimage' 'intel-tbb')
makedepends=('cmake' 'qt5-base') # VTK requires Qt5 to build
source=("opencascade-${pkgver}.tar.gz::http://git.dev.opencascade.org/gitweb/?p=occt.git;a=snapshot;h=refs/tags/${_pkgver};sf=tgz"
        'opencascade.sh' 'fix-install-dir-references.patch'
        'configuration-problem-glibc-2.26.patch' 'vtk7.patch')
sha256sums=('530f9981e6026e6cc04c462ab039b4977a568f943d6086dc502262d100a07a79'
            '2064536a85d46fee368a8f1a712b2c6c77ca79c5bffcc68cba79d70d36efa2f4'
            'afb584aa453993ae8d9e2b983594558531ede735a5892754b812be30650c9fb5'
            '2850a1551085c43f88f134466e3acad950e05e8d46ad04057ea671db0c8a8138'
            'bd230962173a80a971c8da9d3dc07238f249544bb67ee834be7d6466391d0315')

prepare() {
  cd "occt-${_pkgver}"
  patch -Np1 -i "$srcdir/fix-install-dir-references.patch"
  patch -Np1 -i "$srcdir/configuration-problem-glibc-2.26.patch"
  patch -Np1 -i "$srcdir/vtk7.patch"
}

build() {
  cd "occt-${_pkgver}"
  mkdir -p build && cd build

  cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DUSE_GL2PS=ON \
    -DUSE_FREEIMAGE=ON \
    -DUSE_FFMPEG=ON \
    -DUSE_VTK=ON \
    -DUSE_TBB=ON

  make
}

package() {
  cd "occt-${_pkgver}/build"

  make DESTDIR="$pkgdir" install

  cd ..

  install -D -m 755 "$srcdir/opencascade.sh" "$pkgdir/etc/profile.d/opencascade.sh"
  install -dm755 "$pkgdir/usr/share/licenses/$pkgname/"
  mv "$pkgdir/usr/share/doc/opencascade/"* "$pkgdir/usr/share/licenses/$pkgname"
  rm -r "$pkgdir/usr/share/doc"

  rm "$pkgdir/usr/bin/"*.sh
}

# vim:set ts=2 sw=2 et:
