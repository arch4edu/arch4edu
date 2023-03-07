# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-compiler
pkgname=(intel-oneapi-compiler intel-oneapi-compiler-static)
_pkgver=2023.0.0
_debpkgrel=25370
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
sha256sums=('073796db3c0452a08987dd9492f6abc80934c369d80e039bdeeaed39c387d46b'
            'b5e39e8d1b9b8e4d86cd51e32f79f1cef3fe786d78e071deb5ff6a25b5d106e6'
            'cfec359010bf71862af2c716b4fa887364d91845a7dc492f7a0c55d428145a3f'
            '2fa8d9f8bdbada124da24f1d161b4b882f85f54bcc341149ea5a5d1e9dcc826d'
            '3828f3cb147ec574de90e5fb518355a913c0d727e9d37e63db3a1e06a98f188a'
            'c7dc0168580eb6d1eb34fef3dfe4595d2af8ee978a84c9461e1974a3624341c6'
            '21fb81767abbf198b1adadc06e8a2ae912fa4b9a3f121448b6c0576433618677'
            'ef2791532a7f5afee609e2e81ddadebf1306a248a84b711959a1be3112d8a509'
            '8c38115b6c132b0c012834e7f7b55c003daac81beaec1678bb19111b848efbfb'
            'a1dcc49438fc1a83474a6f3bc4543ca6cf7dcb0b5a8dcd1bdffed9ac488825fd'
            '39c8f307c67129ef8d466561f39bbed3445548fc9bba48aabe58314cbcf0ae91'
            '2aa3f782f8c5ea1920d7fbabd7758b95b110764c53418f73d3c156164d84f44a'
            '91aafe8566afc0326b236462e09dfd937b32c91fd04628f6445317479862147d'
            'b324474eae8bd5bd010df52de880eea55566e91dc043462879fc295ea6b3039c'
            '7928a9aef5854d60424a9abc6669920f5c46dfd4c8381fcdc9e28bddcf507b8c'
            '63f63e8e1f02ce34baec35d4892b89a940a745a488fff8d1e04437ab079e7543'
            '52a1aa257be0014d298f7dc61579768744c4bc0c59fdc951c368322c75facacf'
            '81a18fca09c78da5bb943fc55b42a5cf38a076e4495e655216611f7b75cbe66b'
            '86260591af48f75726f9b6ab898140070174e78cd0710089528e6a8e47a2bad4'
            'df5282db2ff27092fe6ed7574d77684fdd6ee82a14816cd8dcb072d3201e2460'
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
		'intel-oneapi-dpcpp-debugger>=2023.0.0'
		'intel-oneapi-mpi>=2021.8.0'
		'intel-oneapi-dpl>=2022.0.0'
		'intel-oneapi-tbb>=2021.8.0'
		'intel-oneapi-dev-utilities>=2021.8.0'

		'intel-oneapi-dpcpp-debugger<2023.0.1'
		'intel-oneapi-mpi<2021.8.1'
		'intel-oneapi-dpl<2022.0.1'
		'intel-oneapi-tbb<2021.8.1'
		'intel-oneapi-dev-utilities<2021.8.1'

		'intel-oneapi-common=2023.0.0'
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

