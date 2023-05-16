# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-compiler
pkgname=(intel-oneapi-compiler intel-oneapi-compiler-static)
_pkgver=2023.1.0
_debpkgrel=46305
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
sha256sums=('8a85a64359f8ea49d82a0a1e89d9a456d3447f917c5a0682d2f6b3d09c6fe48e'
            '2b12ab367bbf7e07d1f9da0b3ec6b3dd409703cb08802cd1e87b78192d90cf39'
            '312bc5e47b7254c5637110a31c48509e09bdcb4af07a8edfddc3d190cd83d9b7'
            '014104b9721d7fca7bb2529ed810f27e9a73410698e9cc643ded7f909a7f17cf'
            '9d9bdb76756be285ce181aef01744e6bc8547d402cc98fe75e930daad67b1ceb'
            'd38895ab3046195929b7109b8bf80b3a0cd14507fda096ab7d0577aaea79b727'
            '354e65a469a9ab8e5c72684ff8c2dc5731356bc7be45012eff23e75302624edf'
            '9c117b25ddee699d1a8162ab101b9c23beeea5e9a3f2409414ee6bbc78d6593b'
            'bb137c02afd6c372e0734c424e2087c9509fbe2f154eee1f363e39368f794334'
            '894eaf13bfe840d2f5df49685e9f5bb9ca8212bc2c8ddf848adcabb3806db8bd'
            'fa3f4c23f527f1ced767fef56c022e252daedd08fab752ec653985f178d509b6'
            '5acd0dc9fc540355bc19317be5d79686f2acb90ac28486dd0717c423e4c94326'
            '6455ee16e4b5ab482ca57a607c20b7387ebc74ab0e1787d2a0beb7ad38c74443'
            'd4cb4adfbfc1ba289996f4b55e85fef73348ee193314552b08a3c59c2af2c8e0'
            '7a1689b820bc2210197f576ba9a18428810e7084afabc447c4de416a5691aefc'
            'd0eec67fe7e3b36c8c5b1d07a17779f739fd2fd1881f6b1848169faffcb855c6'
            'd02cd7aea9d98e935f7f4051f2f41126143f37450de0ad4d44e14eebec96e61d'
            'f8c75298a5885773be07ed17afa4800a895450b9232b0d96eb9721297b18a319'
            'c8c73b7a88ed594c53a424dc3ed1dc497259da960dad5eb902982f5c31059e8d'
            'a80d6c6606653ad4e45dc34410b2fa4f60dc7c50041ba27b73981e7c2743c7cc'
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
		'intel-oneapi-dpcpp-debugger>=2023.1.0'
		'intel-oneapi-mpi>=2021.9.0'
		'intel-oneapi-dpl>=2022.1.0'
		'intel-oneapi-tbb>=2021.9.0'
		'intel-oneapi-dev-utilities>=2021.9.0'

		'intel-oneapi-dpcpp-debugger<2023.1.1'
		'intel-oneapi-mpi<2021.9.1'
		'intel-oneapi-dpl<2022.1.1'
		'intel-oneapi-tbb<2021.9.1'
		'intel-oneapi-dev-utilities<2021.9.1'

		'intel-oneapi-common=2023.1.0'
	)
	provides=(
		"intel-oneapi-openmp" 
		"intel-oneapi-compiler-shared" 
		"intel-oneapi-compiler-shared-runtime" 
		"intel-oneapi-compiler-shared-runtime-libs"
		"intel-oneapi-compiler-dpcpp-cpp-runtime" 
		"intel-oneapi-compiler-dpcpp-cpp-runtime-libs" 
		)
	conflicts=(
		"intel-oneapi-openmp" 
		"intel-oneapi-compiler-shared" 
		"intel-oneapi-compiler-shared-runtime" 
		"intel-oneapi-compiler-shared-runtime-libs"
		"intel-oneapi-compiler-dpcpp-cpp-runtime" 
		"intel-oneapi-compiler-dpcpp-cpp-runtime-libs" 
		)
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

