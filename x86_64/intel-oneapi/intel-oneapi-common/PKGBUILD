# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-common
pkgver=2022.1.0
_debpkgrel=161
pkgrel=1
pkgdesc="oneAPI Common"
arch=('any')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-vars-${pkgver}-${_debpkgrel}_all.deb"
"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-licensing-${pkgver}-${pkgver}-${_debpkgrel}_all.deb")
sha256sums=('52a2726739652b4d3021a9f21d8ca664cd5582853b561e421f003b94789a4469'
            '30f36ef653964ac629ce77c2c2d21a923c7ba4ff88936c39a8f39237b7446cca')
noextract=(
	"${pkgname}-vars-${pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}-licensing-${pkgver}-${pkgver}-${_debpkgrel}_all.deb"
)
build() {
	ar x ${pkgname}-vars-${pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz
	ar x ${pkgname}-licensing-${pkgver}-${pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz
}

package() {
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$pkgver" ${pkgdir}/opt/intel/oneapi/licensing/latest
}
