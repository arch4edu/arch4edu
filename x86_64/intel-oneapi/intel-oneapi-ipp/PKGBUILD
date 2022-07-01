# Contributor : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-ipp
pkgname=(intel-oneapi-ipp intel-oneapi-ipp-static)
_pkgver=2021.6.0
_debpkgrel=626
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® Integrated Performance Primitives"
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
sha256sums=('abb9f14df006db5684f3b54a2a664adfaf10ca90320d97443104ffcc9e3c650f'
            'e7bbff3f04f6e7e9618c71aa6291a14198391abdbad25927119dc9c0127ea3aa'
            '8635703ac473eff8aa251e5324bd339cbccdbefd3c3fe1d895e9a6508fdd49fe'
            'c0683abd09e5d3759e62dcd96e496c9581416bee80300c189e4e81b55c145c4b'
            '6d107c6b8da27adb2d643596512282c26f557387d184b8271298df831b29421f'
            '140334f0e2bed5ecfaa1a9a5f8a65034aa87ad8104ec63c579259f21c97c24d8')

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

package_intel-oneapi-ipp() {
	depends=('intel-oneapi-common=2022.1.0'
    'intel-oneapi-tbb>=2021.6.0' 'intel-oneapi-compiler>=2022.1.0'
	'intel-oneapi-tbb<2021.6.1' 'intel-oneapi-compiler<2022.1.1')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/ipp/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
	install -Dm644 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	# cmake
	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/ipp/latest/lib/cmake/ipp" ${pkgdir}/usr/lib/cmake/ipp
}


package_intel-oneapi-ipp-static() {
	pkgdesc="$pkgdesc (static libs)"
	depends=("$pkgbase=$pkgver")
	options=(staticlibs)
	cd ${srcdir}
	for _file in $(find . -name '*.a'); do
		_filename=$(echo $_file | sed "s/.a$//g")
		if [ -f "$_filename.so" ]; then
			cp --parents ${_file} ${pkgdir}/
		fi
	done
}
