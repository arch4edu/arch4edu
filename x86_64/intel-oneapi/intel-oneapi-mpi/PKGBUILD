# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Intel Corporation <http://www.intel.com/software/products/support>

pkgbase=intel-oneapi-mpi
pkgname=(intel-oneapi-mpi intel-oneapi-mpi-static)
_pkgver=2021.6.0
_debpkgrel=602
pkgver=${_pkgver}_${_debpkgrel}
pkgrel=1
pkgdesc="Intel® MPI Library Runtime Environment"
arch=('x86_64')
url='https://software.intel.com/content/www/us/en/develop/tools/oneapi.html'
license=("custom")
source=(
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"https://apt.repos.intel.com/oneapi/pool/main/${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}.conf"
	"${pkgname}.sh"
)
noextract=(
	"${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
	"${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb"
)
sha256sums=('d609d3cf310e43d9adc6c1a937c19b325e19117350452c85bc0289f0e5cf20a1'
            '3f22e78a8ab97a4ee3647925849c5492218b6379e3bd9d32411aacb290684e6f'
            'c994f2dc82f7479c229ee102775a12bb12d80fec364f511f8b73c1e4f0ae2653'
            '0910cf4e0613c8eaaf61070638981d5531348ce78770a7bf471f86061edb7f32')

build() {
	ar x ${pkgname}-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	ar x ${pkgname}-devel-${_pkgver}-${_pkgver}-${_debpkgrel}_amd64.deb
	tar xvf data.tar.xz

	rm -r opt/intel/oneapi/conda_channel
}

package_intel-oneapi-mpi() {
	depends=('intel-oneapi-common=2022.1.0')
	cp -r ${srcdir}/opt ${pkgdir}
	ln -sfT "$_pkgver" ${pkgdir}/opt/intel/oneapi/mpi/latest

	install -Dm644 ${pkgname}.conf ${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf
	install -Dm644 ${pkgname}.sh ${pkgdir}/etc/profile.d/${pkgname}.sh

	# pkgconfig
	cd ${pkgdir}/opt/intel/oneapi/mpi/latest/lib/pkgconfig
	install -d ${pkgdir}/usr/share/pkgconfig
	for _file in $(find . -mindepth 1 -name '*.pc' -printf "%f\n"); do
		ln -sf /opt/intel/oneapi/mpi/latest/lib/pkgconfig/${_file} ${pkgdir}/usr/share/pkgconfig/${_file}
	done
}

package_intel-oneapi-mpi-static() {
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
