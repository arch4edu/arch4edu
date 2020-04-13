# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-ext-rocr
pkgver=3.3.0
pkgrel=2
_debfile=hsa-ext-rocr-dev_1.1.30300.0-rocm-rel-3.3-19-23fc088b_amd64.deb
pkgdesc='ROCm Platform Runtime: Closed source components'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCR-Runtime'
license=('EULA')
depends=("hsa-rocr" "hsakmt-roct")
source=("http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-ext-rocr-dev/$_debfile")
sha256sums=('6b44e286b395d946b865ec1f3cc546356396785ac1fde591d07af02d0aa7c25d')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
}
