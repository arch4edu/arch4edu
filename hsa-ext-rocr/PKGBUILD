# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-ext-rocr
pkgver=3.5.1
pkgrel=1
_debfile=hsa-ext-rocr-dev_1.1.30501.0-rocm-rel-3.5-34-def83d8_amd64.deb
pkgdesc='ROCm Platform Runtime: Closed source components'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCR-Runtime'
license=('EULA')
depends=("hsa-rocr" "hsakmt-roct")
source=("https://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-ext-rocr-dev/$_debfile")
sha256sums=('0ef5132d086f36ce73161ff21bc4108e33f27cdff838b3f347729497050fa0ac')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
}
