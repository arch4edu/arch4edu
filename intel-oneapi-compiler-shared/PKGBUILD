# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-compiler-shared
pkgver=2021.2.0
_debpkgrel=610
pkgrel=3
pkgdesc="Intel(R) Compiler Shared Files"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-runtime-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-common-${pkgver}-${pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-common-runtime-${pkgver}-${pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-classic-fortran-shared-runtime-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}.conf"
)
noextract=(
	"${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-runtime-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-common-${pkgver}-${pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}-common-runtime-${pkgver}-${pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-dpcpp-cpp-classic-fortran-shared-runtime-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
)
sha256sums=('a491103d6a6e954bb02cbbcd7a90f0e68f968fda9a807a45167864e1d90588aa'
            '248c0d1736ba22647a3d194ba9f3ab56e9f5fb8aa6b6e4294744be552503371f'
            'c3f9221c674cfd40087382cb801e95587c2d6f551c1a0ded945a43ef27ebc4dd'
            '2f190d34f79b5518f3769d8cfb9bd46a55f68bd8a10099ace5e9018339e96042'
            '0af1a42f77ece189b33565c23d471fa10316cb0f09b99f185e8a70a827e20b36'
            '281bd45641b4b00eb4feffc7b47ea9371a6e584a9c12213bd9b6c71389a4bba6')
install="${pkgname}.install"

build() {
	ar x ${pkgname}-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-runtime-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-common-${pkgver}-${pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-common-runtime-${pkgver}-${pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	ar x "intel-oneapi-compiler-dpcpp-cpp-classic-fortran-shared-runtime-${pkgver}-${pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-dpcpp-debugger' 'intel-oneapi-openmp' 'intel-oneapi-common-vars' 'intel-oneapi-common-licensing')
	mv ${srcdir}/opt ${pkgdir}

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
}
