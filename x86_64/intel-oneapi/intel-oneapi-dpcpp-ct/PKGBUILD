# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dpcpp-ct
_pkgver=2023.0.0
_debpkgrel=25483
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® DPC++ Compatibility Tool"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-dpcpp-ct-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-dpcpp-ct-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb")
sha256sums=('b10d895143588727a1d63541588104a944e78764f23fd21d8254158965924d6e'
            '9abf42b750fa6c656cddb15acbea8bd7e6d101bafe2cfc8c634bc4029618da65')

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
	depends=('intel-oneapi-common=2023.0.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dpcpp-ct/latest
}
