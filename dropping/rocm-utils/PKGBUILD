# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008@yahoo.com>
# Contributor: Lucas Magalhães <whoisroot@national.shitposting.agency>
pkgname=rocm-utils
pkgver=4.3.0
pkgrel=1
pkgdesc="ROCm Platform Runtime: Utils"
arch=('x86_64')
url="https://rocm-documentation.readthedocs.io/en/latest/"
license=()
depends=('rocminfo' 'rocm-clang-ocl')
makedepends=()
source=()
sha256sums=()

package() {
	mkdir -p "${pkgdir}/opt/rocm/.info"
	echo "${pkgver}-${pkgrel}" > "${pkgdir}/opt/rocm/.info/version-utils"
}
