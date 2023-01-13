# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-advisor
_pkgver=2023.0.0
_debpkgrel=25338
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
sha256sums=('e54ca225269f3b9ef37bc721908203062b6878a4421948e2294980e2f6867c2a')

build() {
	ar x ${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2023.0.0')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "${_pkgver}" ${pkgdir}/opt/intel/oneapi/advisor/latest
}
