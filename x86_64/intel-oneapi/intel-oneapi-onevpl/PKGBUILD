# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-onevpl
_pkgver=2023.1.0
_debpkgrel=43488
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® oneAPI Video Processing Library"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
"${pkgname}.conf")
sha256sums=('e6962f9d56ca54aae4e74388b53e1e40e14652e905ad7bd7b31ff3f0dc5b771d'
            '54ff8fbee48b01b163bdd07efc1028da7858df10c967df01efc103b5a2a02027'
            '7f0a84aaa902934869e93ba0af66c4eb56f0df6c133a4d60af425e6ecc354f15')

noextract=(
	"${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
)

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2023.1.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/vpl/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf

	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/vpl/latest/lib/cmake/vpl" ${pkgdir}/usr/lib/cmake/vpl

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/vpl/latest/lib/pkgconfig
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/vpl/latest/lib/pkgconfig/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done
}
