# Maintainer: Luis Sarmiento < lgsarmientop-ala-unal.edu.co >
# Contributor: Sebastian Voecking <voeck-ala-web.de>

pkgname=clhep
_pkgname=CLHEP
pkgver=2.4.7.1
pkgrel=1
pkgdesc='A Class library for High Energy Physics'
url="http://proj-clhep.web.cern.ch/"
arch=('x86_64')
license=('GPL3')
depends=('bash')
options=('!emptydirs' 'staticlibs')
makedepends=('cmake'                # for building the package
	     'texlive-core'         # for the documentation
             'texlive-formatsextra' # for the documentation
             'doxygen'              # for the documentation
            )
source=("http://proj-clhep.web.cern.ch/proj-clhep/dist1/${pkgname}-${pkgver}.tgz")
sha256sums=('1c8304a7772ac6b99195f1300378c6e3ddf4ad07c85d64a04505652abb8a55f9')

build() {
  msg 'Compiling the package'
  cmake \
      -S ${pkgver}/${_pkgname} \
      -B build \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCLHEP_BUILD_DOCS=ON \
      ${srcdir}/${pkgver}/${_pkgname}
  cmake --build build --target all
}

check() {
  msg 'Running the tests'
  ctest --test-dir build
}

package() {
    msg 'Creating the package'
    DESTDIR="${pkgdir}" cmake --build build --target install
    install -Dm644 ${srcdir}/${pkgver}/${_pkgname}/COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
