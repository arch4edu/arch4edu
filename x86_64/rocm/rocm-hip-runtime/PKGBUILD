# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-hip-runtime
_pkgver_major=5
_pkgver_minor=3
_pkgver_patch=2
_pkgver_str="${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)"
_pkgver_magic=96
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
source=(# https://repo.radeon.com/rocm/apt/5.3.2/pool/main/r/rocm-hip-runtime/rocm-hip-runtime_5.3.2.50302-96~22.04_amd64.deb
        "${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver/.0/}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_str}-${_pkgver_magic}~${_pkgver_ubunturel}_amd64.deb")
sha256sums=('0f14e1bc045ce41874612653264a4d465f2cd4f6a2f993b0992df788716d7b07')

prepare() {
  tar -xf data.tar.gz
}

package() {
    install -Dm644 opt/rocm-${pkgver}/.info/version-hiprt "$pkgdir/opt/rocm/.info/version-hiprt"
}
