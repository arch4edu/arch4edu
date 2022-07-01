# Maintainer : Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-ippcp
pkgname=(intel-oneapi-ippcp intel-oneapi-ippcp-static)
_pkgver=2021.6.0
_debpkgrel=536
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® Integrated Performance Primitives Cryptography common"
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
sha256sums=('b76fe7205a9d7d36942afaef70bd2fbf41f8ba7b3d64024225f398c93c5696c5'
            'c9c49c3ae07393ceb86055dfb6e7dd777be3adbd29678265e1e7027484eb4300'
            'd89cc7b3e290673891c72f303b11fa2422fd79faa6756c4ab3080e1a2c36e736'
            '314658f2bed9e4d816179b8fd315baa86c2f3188ee570c0d5832df855bc5a44e'
            '76925aa5c6d4dfcb5f87dbc6b51f5480a36abd05ff9e5cc7531bb95c7bee059c'
            '8c52433232e6b703f31298646385430887676b2c6fdbcb909d181b3fb436dd7f')

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

package_intel-oneapi-ippcp() {
	depends=('intel-oneapi-common=2022.1.0')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/ippcp/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
	install -Dm755 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	mkdir -p ${pkgdir}/usr/lib/cmake
	ln -sfT "/opt/intel/oneapi/ippcp/latest/lib/cmake/ippcp" ${pkgdir}/usr/lib/cmake/ippcp

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/ippcp/latest/lib/pkgconfig
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/ippcp/latest/lib/pkgconfig/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done
}

package_intel-oneapi-ippcp-static() {
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

