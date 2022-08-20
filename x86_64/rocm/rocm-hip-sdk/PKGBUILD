# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>
# Contributor: wuxxin <wuxxin@gmail.com>

pkgname=rocm-hip-sdk
_pkgver_major=5
_pkgver_minor=2
_pkgver_patch=1
_pkgver_magic=79
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=2
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
sha256sums=('b39ad15eaf503d2385c47022aa531b0e3bdc015f73791228ada8e7ea8f37cb6c')


package() {
    tar -xf data.tar.gz
    install -D opt/rocm-${pkgver}/.info/version-hip-sdk "$pkgdir/opt/rocm/.info/version-hip-sdk"
}
