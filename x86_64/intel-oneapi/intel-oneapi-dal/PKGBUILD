# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dal
_pkgver=2023.0.0
_debpkgrel=25395
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
sha256sums=('5c60fd10142bf8030a371da57ded1281b1cc27f1a450dfdcaf2b9cd19d838ebd'
            'cdefa731b17c8bfe9f69ba61161004d33650273bdd8ef2fc784eb206abf51d4d'
            '0e5a00df088bb049c4e725a9f0ecfc437646e932dddb15506d1b4fd6793ddf34'
            'fe8210d31da4e6d1e4b4cae5b83cb44a3bbbe36b8ccb23199604b25770ec07a5'
            'de4fdfe444c91d05ab6f1818986a8f79824fd15dd2d2c44c2879097ca44ce8e9'
            'c32974d14adb3871cd6f08989d425e53f1e14108f3142f470406f414bfd62ee7'
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
	depends=('intel-oneapi-common=2023.0.0'
    'intel-oneapi-tbb>=2021.8.0' 'intel-oneapi-tbb<2021.8.1' 'intel-oneapi-compiler>=2023.0.0' 'intel-oneapi-compiler<2023.0.1')
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
