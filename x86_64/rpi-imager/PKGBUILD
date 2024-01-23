# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Dmytro Aleksandrov <alkersan@gmail.com>

pkgname=rpi-imager
pkgver=1.8.5
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

b2sums=('a3268674a9d8345c23b765beef041404185eb31a25cefc2adee0d6de7910aa526c1b1f0073e4fd959ae3aa04764c9890355835295dab40149d07e37b0869a890'
        '18b8cb55be4e46279dfab42f8d742d52f5ad68d74b45195066d8d2422aa6875d644fbc81f293629f71bd12498a402a91a359a7793058429d5d60a20f061ceef2')

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
