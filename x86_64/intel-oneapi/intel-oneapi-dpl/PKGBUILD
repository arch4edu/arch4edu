# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dpl
_pkgver=2021.7.0
_debpkgrel=631
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® oneAPI DPC++ Library 2021.7.0 for Linux*"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-libdpstd-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb")
sha256sums=('1cc950ad392724d53161a3aca1716ef8b26d06b073de551daa9ac408ec215a5a')

build() {
	tar xvf data.tar.xz
	rm -r opt/intel/oneapi/conda_channel
}

package() {
	depends=('intel-oneapi-common=2022.1.0')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dpl/latest

	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/dpl/latest/lib/cmake/oneDPL" ${pkgdir}/usr/lib/cmake/oneDPL

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/dpl/latest/lib/pkgconfig
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/dpl/latest/lib/pkgconfig/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done
}
