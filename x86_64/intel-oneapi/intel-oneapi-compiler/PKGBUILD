# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-compiler
pkgname=(intel-oneapi-compiler intel-oneapi-compiler-static)
_pkgver=2022.1.0
_debpkgrel=3768
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=2
pkgdesc="Intel® oneAPI Compiler"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-fortran-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-shared-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-cpp-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-classic-fortran-shared-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-fortran-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-shared-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-shared-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-dpcpp-cpp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-openmp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-openmp-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-dpcpp-cpp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-fortran-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/intel-oneapi-compiler-fortran-runtime-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}.conf"
)
noextract=(
	"intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-fortran-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-shared-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-cpp-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-dpcpp-cpp-classic-fortran-shared-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-dpcpp-cpp-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-fortran-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-shared-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-shared-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-dpcpp-cpp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-openmp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-openmp-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-dpcpp-cpp-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-dpcpp-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
	"intel-oneapi-compiler-dpcpp-cpp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-fortran-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"intel-oneapi-compiler-fortran-runtime-${_pkgver}-${_debpkgrel}_amd64.deb"
)
sha256sums=('0407cf12127f641f1e1b50e8e8e3c6c9cd27be40b849d697401fa8c140604c23'
            '70d05bfb37754c26e706ce5703b772671685660a386188be817ed81bb2e2a025'
            '206e3fb5d65391b62a086f21aea82820c1862d1b0665e667fd72d389f6fddfeb'
            '3185dc02473b3d3a34234dd82a17c285e43701455636f93be235b52c2ac6f2c6'
            'd505ca48613799f5cd63d22a006f8db69f3bbf999269183fda418f1c04c3088d'
            '2877196318d0640b9590cf6914f339b17a9d2bea60958bb03246d5aff1d34ab0'
            '77b7201b5fe991152528ec40d586114edef12bb79c1a1a8fbfd6bd23c2aba5e1'
            '5bc6452a32f5781c96498515d061d8fe9d7bba13b41eb983fe9bb0f792621906'
            'adf5082079e72ec8634fa363bb3fd0fb4f394e4f1f927949ed06a2f3f1661956'
            'c9961b90a9c4f4636c78292b5ba3d6cf6bbd7081f1ce4a4690bb7db94596226e'
            'c748adc3bac2f0f4c3419f0b1e5bdc34d1508832819deeef68336c290a2fd2be'
            'c525c416c61cac9aa4e22fec78be95b88d33bca13360d0444c22da52eb8dd318'
            '34fa220340f3d488beb06bb7fb879712e5a999d7580574f63805b0c93fe506fc'
            'aaa06115d6cbad606373a61a512162f132c52360f6058970d7a4df55300fb826'
            'ba1a53e93fbd60fad4d17a0d38f14b8553775508e5400feffc95fbf0a3da562b'
            '746d30e0794d0b60ab3d7cd31be9d7981b98c2b0305c238f1a9af5612a22b123'
            '3335b168e758d72aa84f4f16524d311dd48448d34b57fbe3ff62068246b1cbfa'
            'f21f641c75ade271f4ad31e8501aeada97f7ec583942dcfe4b41d6016bd2fd35'
            'e87ad5fb97bc6bacc8758c7ba70cf2232cdc5951806f23052e043a8542b0ef6b'
            '45c79bc0eb26e871838d47632cc15c53f6ef13f9371aab71b815b87379aaa46a'
            '272e9a6015f25f777e092d5c8c4c435e08d4fe640ba7f15d09cd36e07654b83f')

build() {
	ar x "intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-fortran-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-shared-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-cpp-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-cpp-classic-fortran-shared-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-cpp-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-fortran-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-shared-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-shared-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-dpcpp-cpp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-openmp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-openmp-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-cpp-runtime-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-eclipse-cfg-${_pkgver}-${_debpkgrel}_all.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-dpcpp-cpp-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-fortran-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz
	ar x "intel-oneapi-compiler-fortran-runtime-${_pkgver}-${_debpkgrel}_amd64.deb"
	tar xvf data.tar.xz

	rm -r opt/intel/oneapi/conda_channel
}

package_intel-oneapi-compiler() {
	depends=(
		'intel-oneapi-dpcpp-debugger>=2021.6.0'
		'intel-oneapi-mpi>=2021.6.0'
		'intel-oneapi-dpl>=2021.7.0'
		'intel-oneapi-tbb>=2021.6.0'
		'intel-oneapi-dev-utilities>=2021.6.0'

		'intel-oneapi-dpcpp-debugger<2021.6.1'
		'intel-oneapi-mpi<2021.6.1'
		'intel-oneapi-dpl<2021.7.1'
		'intel-oneapi-tbb<2021.6.1'
		'intel-oneapi-dev-utilities<2021.6.1'

		'intel-oneapi-common=2022.1.0'
	)
	provides=("intel-oneapi-openmp" "intel-oneapi-compiler-shared-runtime" "intel-oneapi-compiler-dpcpp-cpp-runtime")
	conflicts=("intel-oneapi-openmp" "intel-oneapi-compiler-shared-runtime" "intel-oneapi-compiler-dpcpp-cpp-runtime")
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "${_pkgver}" ${pkgdir}/opt/intel/oneapi/compiler/latest

	cd ${pkgdir}/opt/intel/oneapi/compiler/${_pkgver}/linux/lib
	ln -sf ./libffi.so.6.0.1 libffi.so.6.0
	ln -sf ./libffi.so.6.0 libffi.so.6

	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/compiler/latest/linux/IntelDPCPP" ${pkgdir}/usr/lib/cmake/IntelDPCPP

	install -Dm644 ${srcdir}/${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
}

package_intel-oneapi-compiler-static() {
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

