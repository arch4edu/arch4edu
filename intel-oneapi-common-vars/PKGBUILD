# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-common-vars
pkgver=2021.2.0
_debpkgrel=195
pkgrel=1
pkgdesc="oneAPI Common Environment Scripts"
arch=('any')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${pkgver}-${_debpkgrel}_all.deb")
sha256sums=('8d3abdd2b117d5be4bbc215bb901df043cb7c3711c43b3d10a99f36c8f83855c')

build() {
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common-licensing')
	mv ${srcdir}/opt ${pkgdir}
}
