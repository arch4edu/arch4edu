# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocm-dev
pkgver=4.1.0
pkgrel=1
pkgdesc="ROCm Dev - Metapackage for the ROCm Development Stack"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
provides=('rocm')
depends=('comgr' 'hip-rocclr' 'hsa-amd-aqlprofile' 'hsakmt-roct' 'llvm-amdgpu'
         'openmp-extras' 'rocm-cmake' 'rocm-dbgapi' 'rocm-device-libs'
         'rocm-gdb' 'rocm-smi-lib64' 'rocm-utils' 'hsa-rocr'
         'rocprofiler' 'roctracer')
makedepends=()
source=()
sha256sums=()

package() {
	mkdir -p "${pkgdir}/opt/rocm/.info"
	echo "${pkgver}-${pkgrel}" > "${pkgdir}/opt/rocm/.info/version-dev"
}
