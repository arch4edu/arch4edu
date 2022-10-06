# NOTE
#
# This program was last updated on 2014, so it's unlikely to be updated again.
# Hence, I did not include pkgver on the source variable.
#
# This is my first PKGBUILD script ever. So, if there's any crashes, please contact me
# or edit the PKGBUILD manually.
#
# Baarakallahu fiikum

# Maintainer: Mochammad Naufal Septifiandi <septifiandinaufal@gmail.com>
pkgname=elkirtasse-bin
pkgver=3.6.8
pkgrel=1
epoch=
pkgdesc="Free and open source library program to read islamic books in Arabic."
arch=('x86_64')
url="https://sourceforge.net/projects/elkirtasse/files/elkirtasse_3.6.8/Ubuntu_13.10/elkirtasse_3.6.8-1_amd64.deb"
license=('GPL')
depends=(gcc gcc-libs qt4)
makedepends=()
optdepends=()
provides=()
source=("$url")
md5sums=('SKIP')

# build() {
# 	cd "$pkgname-$pkgver"
# 	./configure --prefix=/usr
# 	make
# }
# 
# check() {
# 	cd "$pkgname-$pkgver"
# 	make -k check
# }

package() {
    bsdtar -xf data.tar.gz
    mv usr "$pkgdir/"
    find "$pkgdir" -type d -exec chmod 777 {} \;
}
