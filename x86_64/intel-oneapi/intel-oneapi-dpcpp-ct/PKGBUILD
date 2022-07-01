# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dpcpp-ct
_pkgver=2022.1.0
_debpkgrel=172
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® DPC++ Compatibility Tool"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-dpcpp-ct-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-dpcpp-ct-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb")
sha256sums=('df6998ea28a885dceb4445b8f331d08c0fd68c9e5d85b98dba83278bde42bdb9'
            'b8e0053bf3c8ec14c3fdcc4e54b71c15c6f0ac7ee2f7ea22cf4bb677003ebf00')

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
	depends=('intel-oneapi-common=2022.1.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dpcpp-ct/latest
}
