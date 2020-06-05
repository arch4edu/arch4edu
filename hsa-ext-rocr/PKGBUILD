# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-ext-rocr
pkgver=3.5.0
pkgrel=1
_debfile=hsa-ext-rocr-dev_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.deb
pkgdesc='ROCm Platform Runtime: Closed source components'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCR-Runtime'
license=('EULA')
depends=("hsa-rocr" "hsakmt-roct")
source=("http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-ext-rocr-dev/$_debfile")
sha256sums=('e8f5ac2bd13658ab0f471d6088088ec14c791f5f39d163dd4bdbda75021f22a1')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
}
