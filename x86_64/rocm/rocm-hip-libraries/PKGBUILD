# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-hip-libraries
_pkgver_major=5
_pkgver_minor=2
_pkgver_patch=0
_pkgver_magic=65
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc="Develop applications using HIP and libraries for AMD platforms"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=('rocm-core' 'rocm-hip-runtime'
        'rocsparse' 'rccl' 'rocsolver' 'rocrand' 'rocfft' 'rocblas'
        'rocalution' 'hipblas' 'hipfft' 'hipsparse' 'hipfort')
makedepends=()
source=("${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver%.$_pkgver_patch}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)-${_pkgver_magic}_amd64.deb")
sha256sums=('2aa40e1ead80b2b2d46910a0b36a915d632d2b36de04b6d4c0041efa0e007c95')


package() {
    tar -xf data.tar.gz
    install -Dm644 opt/rocm-${pkgver}/.info/version-hip-libraries "$pkgdir/opt/rocm/.info/version-hip-libraries"
}
