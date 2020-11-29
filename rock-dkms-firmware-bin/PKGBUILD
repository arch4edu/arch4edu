# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rock-dkms-firmware-bin
pkgver=3.9.1
_pkgver=3.9-19
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
sha256sums=('3813d91b0973bc8efcc0984ae2ed8bf2ab190cadce076f6bb3d1222703747131')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"
  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms-firmware/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
