# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-hip-runtime
_pkgver_major=5
_pkgver_minor=3
_pkgver_patch=0
_pkgver_magic=63
_pkgver_ubunturel=22.04
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc="Packages to run HIP applications on the AMD platform"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=('rocm-core' 'rocm-language-runtime' 'rocminfo' 'hip-runtime-amd' 'rocm-llvm' 'rocm-cmake')
makedepends=()
optdepends=('hipify-clang: Translate CUDA code into HIP. Requires CUDA.')
source=("${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver/.0/}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)-${_pkgver_magic}~${_pkgver_ubunturel}_amd64.deb")
sha256sums=('69cef8d550af582666af0cec2e3315da9d7704b46cacca55b5adf087bf7d7cb8')

package() {
    tar -xf data.tar.gz
    install -Dm644 opt/rocm-${pkgver}/.info/version-hiprt "$pkgdir/opt/rocm/.info/version-hiprt"
}
