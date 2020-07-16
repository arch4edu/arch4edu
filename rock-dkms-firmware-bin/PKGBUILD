# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rock-dkms-firmware-bin
pkgver=3.5.1
_pkgver=3.5-32
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
sha256sums=('75859a63c09b1fd57da1106b0b20c4d910345d09fa7cd634d6bb73dc5e594313')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"
  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms-firmware/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
