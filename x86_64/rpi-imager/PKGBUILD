#Maintainer: Dmytro Aleksandrov <alkersan@gmail.com>

pkgname=rpi-imager
pkgver=1.7.2
pkgrel=1
pkgdesc="Raspberry Pi Imaging Utility"
depends=('hicolor-icon-theme' 'libarchive' 'qt5-base' 'qt5-declarative'
         'qt5-quickcontrols2' 'qt5-svg' 'util-linux')
optdepends=('dosfstools: SD card bootloader support'
            'udisks2: Needed if you want to be able to run rpi-imager as a regular user')
makedepends=('cmake' 'qt5-tools')
arch=('x86_64' 'aarch64')
url="https://github.com/raspberrypi/rpi-imager"
license=("Apache")

source=(
  "${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
  "remove_update_checking.patch"
)

sha256sums=('babdcda0a38c5dc3893eef3d2d7138d6d23ba7e306f0f840b6970c579490a57a'
            '95c3b12b6dfa1535e87dfda880e8fea6771d4d5057b1188c766133b3521b5daa')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  patch --strip=1 --input="$srcdir/remove_update_checking.patch"
}

build() {
  rm -rf build
  cmake -B build -S "${pkgname}-${pkgver}/src" \
    -DCMAKE_BUILD_TYPE='None' \
    -DCMAKE_INSTALL_PREFIX='/usr'

  make -C build
}

package() {
  make -C build DESTDIR="${pkgdir}" install
}
