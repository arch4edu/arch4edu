# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dpcpp-ct
_pkgver=2023.1.0
_debpkgrel=44450
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® DPC++ Compatibility Tool"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-dpcpp-ct-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-dpcpp-ct-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb")
sha256sums=('062a8186d07999286875f13de68b7516c10ed4466c408b03558b318e2cffa291'
            '0f0d427b2518e9498a94566eae6b32c9c8e41b12361ebf236846e8a57c302d44')

noextract=(
	"intel-oneapi-dpcpp-ct-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-dpcpp-ct-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
)

build() {
	ar x intel-oneapi-dpcpp-ct-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x intel-oneapi-dpcpp-ct-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2023.1.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dpcpp-ct/latest
}
