# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgname=intel-oneapi-dal
_pkgver=2021.6.0
_debpkgrel=915
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
sha256sums=('e53eecf391dfebcf81e3001e2792793eb4ab31ca314c772444062b85d1a3f0a6'
            '154d34597db9c8558a62b312e7357ce68cdb6f4732265f081b19f3f0fef1f8ed'
            '5c0a19bedba4bff264b87f12f50976ab1dc6176ebb7141e702a4a6d278e0eee0'
            '1787712381e202cc9d54f6184dec24fef5722b1c78e49679aa7e29c4266031ec'
            '064e5b747cbf6dbd88e3ba718d336d31d7178b8595ac7d2726f030759384b6f9'
            '7827f21d50858987da988786223add0ff4d2f29a900ee0f2a7f12675dcab8365'
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
	depends=('intel-oneapi-common=2022.1.0'
    'intel-oneapi-tbb>=2021.6.0' 'intel-oneapi-tbb<2021.6.1' 'intel-oneapi-compiler>=2022.1.0' 'intel-oneapi-compiler<2022.1.1')
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
