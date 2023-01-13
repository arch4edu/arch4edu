# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dev-utilities
_pkgver=2021.8.0
_debpkgrel=25328
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
sha256sums=('df8513238bb753f9d169ffc7967784478ea10a2ab3cb26246c66a0d51d96d33f'
            'e91dde74241905098eb7dc59faf37b1f3b6bb6c72fc2f4a7d17a2d6ad2d33937')

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2023.0.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dev-utilities/latest
}
