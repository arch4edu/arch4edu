# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Dmytro Aleksandrov <alkersan@gmail.com>

pkgname=rpi-imager
pkgver=1.7.4.1
pkgrel=1
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
    'aaee1a5186bc6b1ec4c93d44b5ae7437cc6a970a13951a5f649f9c2bcaa2a4dd1c5c76c9da37d768cd7b840d093eeb59cdeccefef23111705ff041b2a8c4d809'
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
