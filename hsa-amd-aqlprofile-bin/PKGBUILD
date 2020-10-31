# Maintainer: acxz <akashpatel at yahoo dot com>

pkgname=hsa-amd-aqlprofile-bin
_pkgname=hsa-amd-aqlprofile
pkgver=3.9.0
_pkgver=3.9
pkgrel=1
_debfile="hsa-amd-aqlprofile_1.0.0_amd64.deb"
pkgdesc='AQLPROFILE library for AMD HSA runtime API extension support'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/'
license=('EULA')
depends=('hsa-rocr')
provides=('hsa-amd-aqlprofile')
conflicts=('hsa-amd-aqlprofile')
source=("$pkgname-$pkgver::http://repo.radeon.com/rocm/apt/${_pkgver}/pool/main/h/hsa-amd-aqlprofile/${_debfile}")
sha256sums=('5ec3d37e7ec3349b4fa54c15756af8ebcbb3d761ac913ccb05030c692400049e')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  rename -- "${_pkgname#hsa}" '' "$pkgdir/opt/rocm/$_pkgname"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
}
