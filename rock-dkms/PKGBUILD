# Maintainer: Olaf Leidinger <oleid@mescharet.de>
pkgname=rock-dkms
pkgver=3.1.44
_pkgver=3.1-44
pkgrel=1
pkgdesc="Linux AMD GPU kernel driver from ROC in DKMS format."
arch=('any')
url="https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver"
license=('GPL')
depends=('dkms>=1.95')
backup=('etc/modprobe.d/blacklist-radeon.conf')
options=('!strip' '!emptydirs')
source=("http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms_${_pkgver}_all.deb")
sha256sums=('6d79b2162d1c0dc925afa62103f6fe28618c851dd345abf28cbb1346288d4a53')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"
  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
