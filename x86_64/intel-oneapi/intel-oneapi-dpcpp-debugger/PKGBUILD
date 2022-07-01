# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dpcpp-debugger
_pkgver=2021.6.0
_debpkgrel=178
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® Distribution for GDB*"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}.conf"
)
noextract=(
	"${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
)
sha256sums=('aba62716b81c21d431abbeda55d28db9326cbfbe13dd633c4df4655da62b85d4'
            '91db109a0cfe173057d88fa8a8580b84870e73bbb576ba22883e6d8cff4bb88e'
            'b27f24587d796719ac01160026e085817b077b65b25cca2959cb782eb714b965')

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	rm -rf opt/intel/oneapi/debugger/${_pkgver}/src
}

package() {
	depends=('intel-oneapi-common=2022.1.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/debugger/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
}
