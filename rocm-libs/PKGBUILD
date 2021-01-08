# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocm-libs
pkgver=4.0.0
pkgrel=2
pkgdesc="ROCm Libs - Libraries utilizing HPC and Ultrascale GPU Computing of
ROCm"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=('hipblas' 'hipcub' 'hipsparse' 'miopen-hip' 'rocalution' 'rocblas'
         'rocfft' 'rocprim' 'rocrand' 'rocsolver' 'rocsparse' 'rocthrust')
makedepends=()
source=()
sha256sums=()

package() {
	mkdir -p "${pkgdir}/opt/rocm/.info"
	echo "${pkgver}-${pkgrel}" > "${pkgdir}/opt/rocm/.info/version-libs"
}
