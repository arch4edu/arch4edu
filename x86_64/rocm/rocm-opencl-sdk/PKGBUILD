# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-opencl-sdk
_pkgver_major=5
_pkgver_minor=2
_pkgver_patch=0
_pkgver_magic=65
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc="Develop applications in OpenCL for the AMD platform"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=('rocm-core' 'rocm-language-runtime' 'rocm-opencl-runtime' 'rocm-llvm')
makedepends=()
source=("${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver%.$_pkgver_patch}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)-${_pkgver_magic}_amd64.deb")
sha256sums=('cf0ea6d5a4b285e4af3f83646ddcf50533902d200e1caa84fee281ad77a80e04')


package() {
    tar -xf data.tar.gz
    install -Dm644 opt/rocm-${pkgver}/.info/version-ocl-sdk "$pkgdir/opt/rocm/.info/version-ocl-sdk"
}
