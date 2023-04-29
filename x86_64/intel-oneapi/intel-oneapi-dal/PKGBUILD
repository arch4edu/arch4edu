# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dal
_pkgver=2023.1.0
_debpkgrel=46349
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® oneAPI Data Analytics Library"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-common-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
    "https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-daal4py-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
    "https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-scikit-learn-intelex-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}.conf"
	"${pkgname}.sh"
)
noextract=(
	"${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
	"${pkgname}-common-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb"
    "${pkgname}-daal4py-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
    "${pkgname}-scikit-learn-intelex-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
)
sha256sums=('1c7c79398aad2010590ac092087bd8430232cf79bd859b8f3a5ac08bf8b1e9f9'
            '202b28dc9cba1d978d3dd296b66fb2de266adb53f8c1aaeead3dd70d713756d6'
            'ffa4620fe6deeb71779ecc8ea6e4b113d93d0abb326632ec87a2be6aa62b579f'
            '72f539982ef75acc8d236144529715d656f35b3ffff486f5205295aa97fe097b'
            'ef04ef5b2e0357c0f72c05055af64715a87b464685f9899ac4fe9d794ac55113'
            'b5b749e93e9677d71420e4be36d60c3c00e345719909978c4db1fae23eff96b3'
            '3bb0049f5245c836472bdb977106ad9fb706d2d04d2544c49c11839d01361cbf'
            '9e93f51d0857508a661c9724d0f4041fcc449aa0bd19cfd78d3bf6065c09ed62')

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-common-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-common-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_all.deb
	tar xvf data.tar.xz

    ar x ${pkgname}-daal4py-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
    tar xvf data.tar.xz

    ar x ${pkgname}-scikit-learn-intelex-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
    tar xvf data.tar.xz

	rm -r opt/intel/oneapi/conda_channel
}

package() {
	depends=('intel-oneapi-common=2023.1.0'
    'intel-oneapi-tbb>=2021.9.0' 'intel-oneapi-tbb<2021.9.1' 'intel-oneapi-compiler>=2023.0.0' 'intel-oneapi-compiler<2023.0.1')
	mv ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/dal/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
	install -Dm644 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	# cmake
	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/dal/latest/lib/cmake/oneDAL" ${pkgdir}/usr/lib/cmake/oneDAL

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/dal/latest/lib/pkgconfig
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/dal/latest/lib/pkgconfig/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done
}
