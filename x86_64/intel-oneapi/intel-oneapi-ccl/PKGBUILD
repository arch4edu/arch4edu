# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-ccl
pkgname=(intel-oneapi-ccl intel-oneapi-ccl-static)
_pkgver=2021.6.0
_debpkgrel=568
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® oneAPI Collective Communications Library"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}.conf"
	"${pkgname}.sh"
)
noextract=(
	"${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
)
sha256sums=('d224c7026151c6d3c0830a9578b7ab904cc5c3c4ba1f491a26bbfacf58a7fa7a'
            'eaa5d539f514453bb1ca12cdb33edebbda0ce7057f05b61b030c682ca28f51bf'
            '711518e543c0b4cd40cda37357936d6c5923da64862f7afa54f673f3daadd065'
            'dcd7b76690d94a2e86d926fbfe8d5297e616e5a49dc8d6eb146c36262aaa2041')

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	rm -r opt/intel/oneapi/conda_channel
}

package_intel-oneapi-ccl() {
	depends=('intel-oneapi-common=2022.1.0' 'intel-oneapi-mpi>=2021.6.0' 'intel-oneapi-mpi<2021.6.1')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "${_pkgver}" ${pkgdir}/opt/intel/oneapi/ccl/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
	install -Dm644 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/ccl/latest/lib/cmake/oneCCL" ${pkgdir}/usr/lib/cmake/oneCCL

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/ccl/latest/lib/pkgconfig
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/ccl/latest/lib/pkgconfig/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done
}

package_intel-oneapi-ccl-static() {
	pkgdesc="Intel® oneAPI Collective Communications Library (static libs)"
	depends=("intel-oneapi-ccl=$pkgver")
	options=(staticlibs)
	cd ${srcdir}
	for _file in $(find . -name '*.a'); do
		_filename=$(echo $_file | sed "s/.a$//g")
		if [ -f "$_filename.so" ]; then
			cp --parents ${_file} ${pkgdir}/
		fi
	done
}
