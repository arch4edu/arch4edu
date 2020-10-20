# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Manhong Dai <daimh@umich.edu>

pkgname=sge
pkgver=8.1.9
pkgrel=2
epoch=1
pkgdesc="The Son of Grid Engine is a community project to continue Sun's old gridengine."
arch=('x86_64')
url="https://arc.liv.ac.uk/trac/SGE"
license=('custom')
depends=(
	'awk'
	'fakeroot'
	'file'
	'gcc'
	'grep'
	'hwloc'
	'inetutils'
	'libtirpc'
	'libxt'
	'make'
	'openmotif'
	'patch'
	'tcsh'
)
install=${pkgname}.install
source=(
	"https://arc.liv.ac.uk/downloads/SGE/releases/${pkgver}/${pkgname}_${pkgver}.tar.xz"
	"sgemaster@.service"
	"sgeexecd@.service"
	#"${pkgname}.sh"
	"cl_ssl_framework.c.patch"
	"sge_passwd.c.patch"
	"drmaa2_list_dict.h.patch"
	"sh.proc.c.patch"
	"qmake.patch"
)
md5sums=('a2f03ca8b803ca4da7d2dedadeca74bb'
         '0f4d29ce1dd17af61f48e61431020ea7'
         'b3e8d5b14639e1f16773f468dabec7de'
         '209d58787a6980f1680dbf00f251403f'
         '573880df6c2915002af3422376933588'
         '4d77510a2601cc79f1260257f2989f08'
         '9ca5f0631567400952ac8099e0869393'
         '5f52ba50a206ebae0f25ec1852d86c5a')

prepare() {
	cd "${pkgname}-${pkgver}"
	patch -p1 < "${srcdir}/cl_ssl_framework.c.patch"
	patch -p1 < "${srcdir}/sge_passwd.c.patch"
	patch -p1 < "${srcdir}/drmaa2_list_dict.h.patch"
	patch -p1 < "${srcdir}/sh.proc.c.patch"
	patch -p1 < "${srcdir}/qmake.patch"
}

build() {
	cd "${pkgname}-${pkgver}/source"

	export SGE_INPUT_CFLAGS='-I/usr/include/tirpc'
	export SGE_INPUT_LDFLAGS='-ltirpc'
	flags='-no-java -no-jni'

	scripts/bootstrap.sh $flags
	./aimk $flags
	./aimk $flags -man
}

package() {
	cd "${pkgname}-${pkgver}/source"

	export SGE_ROOT="${pkgdir}/opt/${pkgname}"
	mkdir -p "${SGE_ROOT}"
	echo y | scripts/distinst -allall -local -noexit

	#install -D -m755 "${srcdir}/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
	install -D -m644 "${srcdir}/sgemaster@.service" "${pkgdir}/usr/lib/systemd/system/sgemaster@.service"
	install -D -m644 "${srcdir}/sgeexecd@.service" "${pkgdir}/usr/lib/systemd/system/sgeexecd@.service"

	mkdir -p "${pkgdir}/usr/share/licenses"
	mv "${srcdir}/${pkgname}-${pkgver}/LICENCES" "${pkgdir}/usr/share/licenses/${pkgname}"
}
