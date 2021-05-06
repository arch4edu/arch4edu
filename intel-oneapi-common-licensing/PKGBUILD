# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-common-licensing
pkgver=2021.2.0
_debpkgrel=195
pkgrel=1
pkgdesc="oneAPI Common License"
arch=('any')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_all.deb")
sha256sums=('b9c7b7bebf05b817a2640562253959a0745296337a40354e9a22234f31543821')

build() {
	tar xvf data.tar.xz
}

package() {
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$pkgver" ${pkgdir}/opt/intel/oneapi/licensing/latest
}
