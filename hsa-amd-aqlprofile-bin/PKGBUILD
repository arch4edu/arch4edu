# Maintainer: Ranieri Althoff <ranisalt+aur at gmail.com>
# Contributor: Ilya Elenskiy <elenskiy.ilya@gmail.com>
# Contributor: acxz <akashpatel at yahoo dot com>

pkgname=hsa-amd-aqlprofile
pkgver=3.5.0
pkgrel=1
_debfile="hsa-amd-aqlprofile_1.0.0_amd64.deb"
pkgdesc='AQLPROFILE library for AMD HSA runtime API extension support'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/HSA-AqlProfile-AMD-extension'
license=('EULA')
depends=(hsa-rocr)
source=("$pkgname-$pkgver::http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-amd-aqlprofile/${_debfile}")
sha256sums=('a0d0920049a2b97da289e37572e48b479a31eb7b23be23420244ef5636b7d334')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  rename -- "${pkgname#hsa}" '' "$pkgdir/opt/rocm/$pkgname"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
}

