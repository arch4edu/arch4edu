# Maintainer: Ranieri Althoff <ranisalt+aur at gmail.com>
# Contributor: Olaf Leidinger <oleid@mescharet.de>

pkgname=rock-dkms
pkgver=3.3.0
_pkgver=3.3-19
pkgrel=1
pkgdesc='Linux AMD GPU kernel driver from ROC in DKMS format.'
arch=('any')
url='https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver'
license=('GPL')
depends=('dkms')
backup=('etc/modprobe.d/blacklist-radeon.conf')
options=('!strip' '!emptydirs')
source=("https://repo.radeon.com/rocm/apt/debian/pool/main/r/$pkgname/${pkgname}_${_pkgver}_all.deb")
sha256sums=('9a6eb2b65360b5ec74de3212030506ae6706bd29dc65d45582dc9d61f16dd5a3')

package() {
  tar xf data.tar.xz -C "$pkgdir"
  install -Dm644 "$pkgdir/usr/share/doc/$pkgname/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
