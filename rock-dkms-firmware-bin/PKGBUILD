# Maintainer: acxz <akashpatel2008@yahoo.com>
pkgname=rock-dkms-firmware-bin
pkgver=3.5
_pkgver=$pkgver-30
pkgrel=1
pkgdesc="Linux AMD GPU firmware from ROC in DKMS format."
arch=('any')
url="https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver"
license=('GPL')
depends=('dkms')
provides=('rock-dkms-firmware')
conflicts=('rock-dkms-firmware')
options=('!strip' '!emptydirs')
source=("http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms-firmware_${_pkgver}_all.deb")

sha256sums=('1777f6b321800f9c0727322c2e5151634fae572889b5c27dfc71549894a4f291')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"
  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms-firmware/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
