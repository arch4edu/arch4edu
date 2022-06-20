# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-language-runtime
_pkgver_major=5
_pkgver_minor=1
_pkgver_patch=3
_pkgver_magic=66
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc="ROCr - ROCm runtime"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=('rocm-core' 'hsakmt-roct' 'hsa-rocr' 'rocm-device-libs' 'comgr')
makedepends=()
source=("${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)-${_pkgver_magic}_amd64.deb")
sha256sums=('7dba7c8a534f75ba5a0e2f97a8fbc1dc4f44e514b7ba3b97a34a34f0b529adf0')


package() {
    tar -xf data.tar.gz
    install -Dm644 opt/rocm-${pkgver}/.info/version-lrt "$pkgdir/opt/rocm/.info/version-lrt"
}
