# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rock-dkms-firmware-bin
pkgver=3.10
_pkgver=3.10-27
pkgrel=1
pkgdesc="Linux AMD GPU firmware from ROC in DKMS format."
arch=('any')
url="https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver"
license=('GPL')
depends=('dkms')
provides=('rock-dkms-firmware')
conflicts=('rock-dkms-firmware')
options=('!strip' '!emptydirs')
source=("${pkgname}-${pkgver}.tar.gz"::"http://repo.radeon.com/rocm/apt/${pkgver}/pool/main/r/rock-dkms/rock-dkms-firmware_${_pkgver}_all.deb")
sha256sums=('a251a93e020f414726fde03709eeb8f4334ae01b4030d805141735d9d92f6421')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"
  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms-firmware/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
