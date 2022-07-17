# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-language-runtime
_pkgver_major=5
_pkgver_minor=2
_pkgver_patch=0
_pkgver_magic=65
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc="ROCr - ROCm runtime"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=('rocm-core' 'hsakmt-roct' 'hsa-rocr' 'rocm-device-libs' 'comgr')
makedepends=()
source=("${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver%.$_pkgver_patch}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)-${_pkgver_magic}_amd64.deb")
sha256sums=('68efc7f3e5797dd46380e56343d724fef208b8a89cfd8b622ef23c9e2b74b1d6')


package() {
    tar -xf data.tar.gz
    install -Dm644 opt/rocm-${pkgver}/.info/version-lrt "$pkgdir/opt/rocm/.info/version-lrt"
}
