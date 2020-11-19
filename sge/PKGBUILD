# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Manhong Dai <daimh@umich.edu>

pkgname=sge
pkgver=8.1.9
pkgrel=5
epoch=1
pkgdesc="The Son of Grid Engine is a community project to continue Sun's old gridengine."
arch=('x86_64')
url="https://arc.liv.ac.uk/trac/SGE"
license=('custom')
depends=(
	'awk'
	'grep'
	'hwloc'
	'libtirpc'
	'openmotif'
	'openssl-1.0'
	'python2'
	'tcsh'
)
makedepends=('make')
install=${pkgname}.install
source=(
	"https://arc.liv.ac.uk/downloads/SGE/releases/${pkgver}/${pkgname}_${pkgver}.tar.xz"
	"sgemaster@.service"
	"sgeexecd@.service"
	#"${pkgname}.sh"
)
md5sums=('a2f03ca8b803ca4da7d2dedadeca74bb'
         '0f4d29ce1dd17af61f48e61431020ea7'
         'b3e8d5b14639e1f16773f468dabec7de')

prepare() {
	cd "${pkgname}-${pkgver}"

	sed 's/} drmaa2_\(dict\|list\)_s;/};/g' -i source/libs/japi/drmaa2_list_dict.h

	sed '1s/python$/python2/' -i source/dist/util/resources/{jsv/jsv,monitoring/check_sge}.py

	# https://www.linuxquestions.org/questions/programming-9/union-wait-problem-269024
	sed 's|union wait w;|int w;|g' -i source/3rdparty/qtcsh/sh.proc.c

	# https://stackoverflow.com/questions/51675200/install-older-version-of-gnu-make-in-ubuntu-18-04
	sed 's/^\(# if _GNU_GLOB_INTERFACE_VERSION\) == \(GLOB_INTERFACE_VERSION\)/\1 >= \2/' -i source/3rdparty/qmake/glob/glob.c

	# https://svnweb.freebsd.org/ports/head/devel/kBuild/files/patch-src_kmk_make.h?view=markup&pathrev=539776
	sed '/^struct rlimit stack_limit;$/s/^/extern /' -i source/3rdparty/qmake/make.h
}

build() {
	cd "${pkgname}-${pkgver}/source"

	export SGE_INPUT_CFLAGS='-I/usr/include/tirpc -I/usr/include/openssl-1.0'
	export SGE_INPUT_LDFLAGS='-ltirpc -L/usr/lib/openssl-1.0 -lssl -lcrypto'
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

	find "${SGE_ROOT}/man" -type f -exec gzip {} \;
	find "${SGE_ROOT}/man" -type l -exec sh -c 'ln -sf $(readlink {}).gz {}.gz && rm {}' \;
	mv "${SGE_ROOT}/man" "${pkgdir}/usr/share/"
}
