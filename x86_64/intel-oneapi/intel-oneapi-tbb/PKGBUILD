# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-tbb
_pkgver=2021.6.0
_debpkgrel=835
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® oneAPI Threading Building Blocks"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-common-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}.conf"
	"${pkgname}.sh"
)
noextract=(
	"${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}-common-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
)
sha256sums=('80617c7ebf590006fadaa271a8f193b2937eaf901ed51e626c02c9073a8dc9e4'
            'cbd83ad505eebf77a519ddce5a49bfaab378d9595fe0d60c4202836ea9bdd871'
            '148f21702a2cb0ae185aef720cce19e3e7abcd219ac20a0a8211a0b931b0b816'
            '956f1ebcc56cb3301d48f874e43906cfc2b18022cfa983916d0d160527d6b6aa'
            'ab4d154371df8bf81c4fd8f079137994c5c9a60f43bef4132e6ffcbfbb08e99d'
            '4904a123751aa5d6889fde1bc4e38ab70f21c0191442fcf26913b96cbcfdb95a')

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-common-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	rm -r opt/intel/oneapi/conda_channel
}

package() {
	depends=('intel-oneapi-common=2022.1.0')
	provides=("tbb=${_pkgver}" "intel-tbb=${_pkgver}")
	conflicts=('tbb' 'intel-tbb')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/tbb/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
	install -Dm755 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	# provide extra/tbb (except python binding)

	# cmake
	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/tbb/latest/lib/cmake/tbb" ${pkgdir}/usr/lib/cmake/tbb
	ln -sfT "/opt/intel/oneapi/tbb/latest/lib/cmake/tbb" ${pkgdir}/usr/lib/cmake/TBB

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/tbb/latest/lib/pkgconfig
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/tbb/latest/lib/pkgconfig/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done

	# include
	mkdir -p ${pkgdir}/usr/include/
	mkdir -p ${pkgdir}/usr/include/oneapi/
	ln -sf /opt/intel/oneapi/tbb/latest/include/tbb ${pkgdir}/usr/include/${_file}
	ln -sf /opt/intel/oneapi/tbb/latest/include/oneapi/tbb ${pkgdir}/usr/include/oneapi/tbb
	ln -sf /opt/intel/oneapi/tbb/latest/include/oneapi/tbb.h ${pkgdir}/usr/include/oneapi/tbb.h

	# lib
	mkdir -p ${pkgdir}/usr/lib/
	cd ${pkgdir}/opt/intel/oneapi/tbb/latest/lib/intel64/gcc4.8
	for _file in $(find . -mindepth 1 -name '*.so*' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/tbb/latest/lib/intel64/gcc4.8/${_file} ${pkgdir}/usr/lib/${_file}
	done
}


