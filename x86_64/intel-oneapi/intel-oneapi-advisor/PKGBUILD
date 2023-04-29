# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-advisor
_pkgver=2023.1.0
_debpkgrel=43480
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® Advisor"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb"
)
noextract=(
	"${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb"
)
sha256sums=('06c3115ee1dd01fb68b623ad2ed624b56ba5a6762cd315758150d00037c3018a')

build() {
	ar x ${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2023.1.0')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "${_pkgver}" ${pkgdir}/opt/intel/oneapi/advisor/latest
}
