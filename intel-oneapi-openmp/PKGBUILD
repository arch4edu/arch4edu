# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-openmp
pkgver=2021.2.0
_debpkgrel=610
pkgrel=1
pkgdesc="Intel® OpenMP* Runtime Library 2021.2.0 for Linux* for Intel(R) 64"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-common-${pkgver}-${pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}.conf"
)
noextract=(
	"${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-common-${pkgver}-${pkgver}-${_debpkgrel}_all.deb"
)
sha256sums=('aaec45cb7240bcf5626728d5b59afb121a10ea4db46707bf38b061caa5161ef3'
            '54760ad7e180c4a2ba13b8a695f9e657be586ecd58c5cceb60c831bcafc7cba6'
            '83c341462ed40bff10af52f44a617634e958782899b5e6a210f3ccb9151e3acc')
install="${pkgname}.install"

build() {
	ar x ${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-common-${pkgver}-${pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	rm -r opt/intel/oneapi/conda_channel
}

package() {
	depends=('intel-oneapi-common-vars' 'intel-oneapi-common-licensing')
	mv ${srcdir}/opt ${pkgdir}

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
}
