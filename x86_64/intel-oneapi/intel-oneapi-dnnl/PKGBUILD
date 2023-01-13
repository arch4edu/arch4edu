# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dnnl
_pkgver=2023.0.0
_debpkgrel=25399
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® oneAPI Deep Neural Network Library"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=("https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb"
"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-devel-${_pkgver}-${_debpkgrel}_amd64.deb"
"${pkgname}.conf"
"${pkgname}.sh")
sha256sums=('616f9fac7c702aa12fa032a80bcbda9988c3029300cbe0b7c71f7049885551dc'
            '6ab85bea0c202b2a31972ebf4eeda89d72403cac293f06617c397b9b7d123979'
            'f1fe419d6cbab4411c5fe68515b1fc8f317185b70a0c2b7400ba7c88dbd32c63'
            'd3fff0cb761be49b766d4fa2e9c34b38e5f99379520201f60654893db47b7dd7')

noextract=(
	"${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-devel-${_pkgver}-${_debpkgrel}_amd64.deb"
)

build() {
	ar x ${pkgname}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-devel-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz
}

package() {
	depends=('intel-oneapi-common=2023.0.0'
    'intel-oneapi-tbb>=2021.8.0' 'intel-oneapi-compiler>=2023.0.0' 
	'intel-oneapi-tbb<2021.8.1' 'intel-oneapi-compiler<2023.0.1' )
	provides=('onednn=2.6')
	conflicts=('onednn')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dnnl/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
	install -Dm644 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	# provide commuity/onednn
	# include
	mkdir -p ${pkgdir}/usr/include/
	mkdir -p ${pkgdir}/usr/include/oneapi/
	cd ${pkgdir}/opt/intel/oneapi/dnnl/latest/cpu_dpcpp_gpu_dpcpp/include
	for _file in $(find . -mindepth 1 -type f -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/dnnl/latest/cpu_dpcpp_gpu_dpcpp/include/${_file} ${pkgdir}/usr/include/${_file}
	done
	ln -sf /opt/intel/oneapi/dnnl/latest/cpu_dpcpp_gpu_dpcpp/include/oneapi/dnnl ${pkgdir}/usr/include/oneapi/dnnl
	# lib
	mkdir -p ${pkgdir}/usr/lib/
	cd ${pkgdir}/opt/intel/oneapi/dnnl/latest/cpu_dpcpp_gpu_dpcpp/lib
	for _file in $(find . -mindepth 1 -name '*.so*' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/dnnl/latest/cpu_dpcpp_gpu_dpcpp/lib/${_file} ${pkgdir}/usr/lib/${_file}
	done
	# cmake
	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/dnnl/latest/lib/cmake/dnnl" ${pkgdir}/usr/lib/cmake/dnnl
}
