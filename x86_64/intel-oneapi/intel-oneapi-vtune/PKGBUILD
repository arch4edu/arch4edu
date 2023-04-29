# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-vtune
pkgname=(intel-oneapi-vtune intel-oneapi-vtune-static)
_pkgver=2023.1.0
_debpkgrel=44286
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® VTune(TM) Profiler"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
options=("!strip")
source=("https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-vtune-${_pkgver}-${_debpkgrel}_amd64.deb"
"${pkgbase}.sh")
sha256sums=('770d9503d07411d94a45c8e0cf320e1b38d22e12ec3c39a769cc138008f2144a'
            'b1647fa8a328380b2f1c52fcdac3c8c7408db0d16d819064d3d9e2cdc13df93a')

build() {
	tar xvf data.tar.xz
}

package_intel-oneapi-vtune() {
	depends=('intel-oneapi-common=2023.1.0')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/vtune/latest

	install -Dm644 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/vtune/latest/include/pkgconfig/lib64
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/vtune/latest/include/pkgconfig/lib64/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done
}

package_intel-oneapi-vtune-static() {
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
