# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Dmytro Aleksandrov <alkersan@gmail.com>

pkgname=rpi-imager
pkgver=1.7.3
pkgrel=2
pkgdesc="Raspberry Pi Imaging Utility"
depends=(
    'hicolor-icon-theme'
    'libarchive'
    'qt5-svg'
    'qt5-quickcontrols2'
)
optdepends=(
    'dosfstools: SD card bootloader support'
    'udisks2: Needed if you want to be able to run rpi-imager as a regular user'
)
makedepends=('cmake' 'qt5-tools')
arch=('x86_64' 'aarch64')
url="https://github.com/raspberrypi/rpi-imager"
license=("Apache")

source=(
    "${pkgname}-${pkgver}.tar.gz::https://github.com/raspberrypi/${pkgname}/archive/v${pkgver}.tar.gz"
    "remove_update_checking.patch"
)

b2sums=(
    '72ab2c8388a11fd7ad6e442872ed5fd31c9d8ec5b2a66143a8ff45fd2db86a260e4cda7039db0af60a45e32512a3370f79190d9cebd25c4abb587e23a42fe445'
    '40bc85ec8d55876e440bf02bc13df7b77ff588a8508402eed9fc27a9e87043c189d70d061355aeac9f8c9b63aa6ea629ea9204f63ea579ab35e0e154e17d41b3'
)

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    patch --strip=1 --input="$srcdir/remove_update_checking.patch"
}

build() {
    #rm -rf build
    cmake -B build -S "${pkgname}-${pkgver}/src" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr'
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
