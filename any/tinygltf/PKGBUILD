# Maintainer: Ali Emre Gülcü <aliemreglc at gmail dot com>
# Update PKGSums: updpkgsums
# Update SRCINFO: makepkg --printsrcinfo > .SRCINFO

pkgname=tinygltf
pkgver=2.9.7
pkgrel=1
pkgdesc="Header only C++ tiny glTF library(loader/saver)"
arch=('any')
url="https://github.com/syoyo/$pkgname"
license=('MIT')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('9d31cf7f22e81febaf1ad587d7722582c154f7d9125673ee46c0c594765e8f35')

package() {
  cd $pkgname-$pkgver
  mkdir -p $pkgdir/usr/include/$pkgname $pkgdir/usr/share/licenses/$pkgname
  install *.h $pkgdir/usr/include/$pkgname
  install *.hpp $pkgdir/usr/include/$pkgname
  install LICENSE $pkgdir/usr/share/licenses/$pkgname
}
