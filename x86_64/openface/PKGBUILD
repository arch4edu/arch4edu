# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=openface
_pkgname=OpenFace
pkgver=2.2.0
pkgrel=1
pkgdesc="A state-of-the art tool intended for facial landmark detection, head pose estimation, facial action unit recognition, and eye-gaze estimation"
arch=('x86_64')
url="https://github.com/TadasBaltrusaitis/${_pkgname}"
license=('custom')
depends=('dlib' 'openblas' 'opencv')
makedepends=('cmake' 'qt5-base' 'tbb' 'wget')
source=("${url}/archive/refs/tags/${_pkgname}_${pkgver}.tar.gz")
sha256sums=('928e6346bcff41393393a364df99bf09c3410fab85b569f2023e3224d2a1981a')

build() {
  cd "${srcdir}/${_pkgname}-${_pkgname}_${pkgver}"

  bash download_models.sh

  cmake -B build \
    -DCMAKE_BUILD_TYPE=RELEASE \
    -DCMAKE_INSTALL_PREFIX=/opt/${pkgname}
#    -DBUILD_SHARED_LIBS=ON \
#    -S "$srcdir/$pkgname-$pkgver" \
#    -DMARCH_NATIVE=ON \
#    -Wno-dev
  make -C build
}

package() {
  cd "${srcdir}/${_pkgname}-${_pkgname}_${pkgver}"

  make -C build DESTDIR="${pkgdir}" install

  install -Dm644 Copyright.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
