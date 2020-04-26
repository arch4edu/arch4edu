# Maintainer: Ranieri Althoff <ranisalt+aur at gmail.com>
# Contributor: Ilya Elenskiy <elenskiy.ilya@gmail.com>

pkgname=hsa-amd-aqlprofile
pkgver=3.3.0
pkgrel=1
_debfile="hsa-amd-aqlprofile_1.0.0_amd64.deb"
pkgdesc='AQLPROFILE library for AMD HSA runtime API extension support'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/HSA-AqlProfile-AMD-extension'
license=('EULA')
depends=(hsa-rocr)
source=("http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-amd-aqlprofile/${_debfile}")
sha256sums=('bbf465283bfc7a055b95b277c108a8bc5604e1ac2a9af7c3fa084989654e239a')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  rename -- "${pkgname#hsa}" '' "$pkgdir/opt/rocm/$pkgname"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
}

