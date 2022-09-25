# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>
# Contributor: wuxxin <wuxxin@gmail.com>

pkgname=rocm-hip-sdk
_pkgver_major=5
_pkgver_minor=2
_pkgver_patch=3
_pkgver_magic=109
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc="Develop applications using HIP and libraries for AMD platforms"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=(
  'rocm-hip-libraries'
  'rocm-llvm'
  'rocm-core'
  'rocm-hip-runtime'
  'hipblas'
  'hipcub'
  'hipfft'
  'hipsparse'
  'hipsolver'
  'miopen-hip'
  'rccl'
  'rocalution'
  'rocblas'
  'rocfft'
  'rocprim'
  'rocrand'
  'rocsolver'
  'rocsparse'
  'rocthrust'
)
makedepends=()
source=("${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)-${_pkgver_magic}_amd64.deb")
sha256sums=('580d152a8bab21e8706a4bee0a8f356d08f97466f1dc89d6c8982b1b431904f1')


package() {
    tar -xf data.tar.gz
    install -D opt/rocm-${pkgver}/.info/version-hip-sdk "$pkgdir/opt/rocm/.info/version-hip-sdk"
}
