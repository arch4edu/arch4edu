# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dev-utilities
_pkgver=2021.6.0
_debpkgrel=989
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel oneAPI Dev Utilities"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
)
noextract=(
	"${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
)
sha256sums=('4efe2d3556804ce77818014227e86b62e34000f511f9ea8774e064956eac2bf1'
            'b9a4895851bbb6d69a0a87c2a12aea34b34553ab15f224a5ab81d8b98a14bc3d')

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2022.1.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dev-utilities/latest
}
