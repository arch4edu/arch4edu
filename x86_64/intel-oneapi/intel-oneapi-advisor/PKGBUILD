# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-advisor
_pkgver=2022.1.0
_debpkgrel=171
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
sha256sums=('09484eeef06a05d8d7a8a17e29d9e21fd13c62a71ff513f883f0b271bfc786bd')

build() {
	ar x ${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2022.1.0')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "${_pkgver}" ${pkgdir}/opt/intel/oneapi/advisor/latest
}
