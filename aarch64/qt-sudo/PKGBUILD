# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: MatMoul <matmoul at the google email domain which is .com>

pkgname=qt-sudo
pkgver=2.4.1
pkgrel=1
pkgdesc='A clone of LXQt sudo tool, without LXQt libs'
arch=('x86_64')
url='https://github.com/aarnt/qt-sudo.git'
license=('LGPL2.1')
depends=(
  'gcc-libs' # libgcc_s.so libstdc++.so
  'glibc' # libc.so
  'qt6-base' # libQt6Core.so libQt6Gui.so libQt6Widgets.so
  'sudo'
)
makedepends=(
  'git'
  'qt6-tools'
)
source=("git+https://github.com/aarnt/qt-sudo.git#tag=v${pkgver}")
sha256sums=('f859d9485170454b0ed156d44c44e56a30ef566be261ae105077eacbba24e61f')

build() {
  cd qt-sudo
  echo "Starting build..."
  qmake6 \
    PREFIX="${pkgdir}/usr" \
    QMAKE_CFLAGS="${CFLAGS}" \
    QMAKE_CXXFLAGS="${CXXFLAGS}" \
    QMAKE_LFLAGS="${LDFLAGS}"

  make
}

package() {
  cd qt-sudo
  make install
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
