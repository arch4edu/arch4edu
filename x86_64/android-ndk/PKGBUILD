# Maintainer: Miguel Revilla Rodríguez <yo at miguelrevilla dot com>
# Contributor: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: frownlee <florez.brownlee@gmail.com>

pkgname=android-ndk
pkgver=r26.d
pkgrel=1
pkgdesc='Android C/C++ developer kit'
arch=('x86_64')
url='https://developer.android.com/ndk/'
license=('GPL' 'LGPL' 'custom')
options=('!strip' 'staticlibs')
backup=("etc/profile.d/$pkgname.sh")
install="$pkgname.install"
replaces=('android-ndk64')
depends=('bash' 'glibc' 'gcc-libs' 'zlib')
# makedepends are just for making namcap happy. AUR packages are not added to
# avoid unneeded efforts
makedepends=('bzip2' 'libxcrypt-compat' 'python' 'perl' 'libc++')
optdepends=(
  'ncurses5-compat-libs: for curses module in bundled Python'
  'bzip2: for bz2 module in bundled Python'
  'libxcrypt-compat: for crypt module in bundled Python'
  'python: various helper scripts'
  'perl: various helper scripts'
  'libc++: for some LLVM components'
)
source=("$pkgname.sh")
source_x86_64=("https://dl.google.com/android/repository/$pkgname-${pkgver/./}-linux.zip")
# SHA1 sums is kept to follow upstream releases https://github.com/android-ndk/ndk/issues/673
sha1sums=('38c46b7b1a1c54a0845d027a8eaf37ed0447d3b2')
sha1sums_x86_64=('fcdad75a765a46a9cf6560353f480db251d14765')
sha256sums=('2050ff500443f6cfa4567c02248cb3ec6ccbc67ce81b32d8dda79383c5103db2')
sha256sums_x86_64=('eefeafe7ccf177de7cc57158da585e7af119bb7504a63604ad719e4b2a328b54')

package() {
  install -Ddm755 "$pkgdir/opt"
  mv "$pkgname-${pkgver/./}" "$pkgdir/opt/$pkgname"

  install -Dm644 $pkgname.sh -t "$pkgdir/etc/profile.d/"

  # make sdkmanager and gradle recognize NDK
  install -Ddm755 "$pkgdir"/opt/android-sdk
  ln -s /opt/$pkgname "$pkgdir"/opt/android-sdk/ndk-bundle
}
