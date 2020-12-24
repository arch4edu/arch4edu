# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rock-dkms-firmware-bin
pkgver=4.0
_pkgver=4.0-23
pkgrel=2
pkgdesc="Linux AMD GPU firmware from ROC in DKMS format."
arch=('any')
url="https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver"
license=('GPL')
depends=('dkms')
provides=('rock-dkms-firmware')
conflicts=('rock-dkms-firmware')
options=('!strip' '!emptydirs')
source=("${pkgname}-${pkgver}.tar.gz"::"http://repo.radeon.com/rocm/apt/${pkgver}/pool/main/r/rock-dkms/rock-dkms-firmware_${_pkgver}_all.deb")
sha256sums=('1694b0edcd20f9440443a7ffba2ee34d2e23cd73b3a681f84f925d8a1314fbd1')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"
  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms-firmware/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
