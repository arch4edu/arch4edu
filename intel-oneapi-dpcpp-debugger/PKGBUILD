# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dpcpp-debugger
pkgver=10.1.1
_debpkgrel=80
pkgrel=1
pkgdesc="Intel® Distribution for GDB*"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-eclipse-cfg-${pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}.conf"
)
noextract=(
	"${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-eclipse-cfg-${pkgver}-${_debpkgrel}_all.deb"
)
sha256sums=('cbd18e772db0c9a781b2f340f1cdc06a29c8cc8499772be99f75fa67eba58bf3'
            '3f9ea224b178085a688effc2726ba65493c5fdf91bad53bb585c3c2bef17e1a5'
            'b27f24587d796719ac01160026e085817b077b65b25cca2959cb782eb714b965')

build() {
	ar x ${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-eclipse-cfg-${pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	rm -r opt/intel/oneapi/debugger/${pkgver}/src
}

package() {
	depends=('intel-oneapi-common-vars' 'intel-oneapi-common-licensing')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$pkgver" ${pkgdir}/opt/intel/oneapi/debugger/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
}
