# Maintainer: Hildigerr Vergaray <Maintainer at YmirSystems dot com>
# Contributor: Beej <beej@beej.us>
# Contributor: Ivan c00kiemon5ter Kanakarakis <ivan.kanak@gmail.com>
pkgname="termcap"
pkgver="1.3.1"
pkgrel=8
pkgdesc="Enables programs to use display computer terminals in a device-independent manner"
arch=('i686' 'x86_64' 'aarch64')
url="http://www.catb.org/~esr/terminfo/"
license=("GPL")
source=("http://ftp.gnu.org/gnu/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('91a0e22e5387ca4467b5bcb18edf1c51b930262fd466d5fda396dd9d26719100')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}/"

    gcc -ansi -Wno-error=implicit-function-declaration -fPIC -c "${pkgname}.c" -DHAVE_STRING_H=1 -DHAVE_UNISTD_H=1 -DSTDC_HEADERS=1
    gcc -ansi -Wno-error=implicit-function-declaration -fPIC -c tparam.c -DHAVE_STRING_H=1 -DHAVE_UNISTD_H=1 -DSTDC_HEADERS=1
    gcc -ansi -Wno-error=implicit-function-declaration -fPIC -c version.c -DHAVE_STRING_H=1 -DHAVE_UNISTD_H=1 -DSTDC_HEADERS=1

    gcc -Wno-error=implicit-function-declaration -shared -Wl,-soname,"lib${pkgname}.so" \
        -o "lib${pkgname}.so.${pkgver}" "${pkgname}.o" tparam.o version.o
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    install -D -m755 "lib${pkgname}.so.${pkgver}" "${pkgdir}/usr/lib/lib${pkgname}.so.${pkgver}"
	ln -s "${pkgdir}/usr/lib/lib${pkgname}.so.${pkgver}" "${pkgdir}/usr/lib/lib${pkgname}.so"

    for infofile in termcap.info*
    do install -D -m644 "${srcdir}/${pkgname}-${pkgver}/${infofile}" "${pkgdir}/usr/share/info/${infofile}"
    done
}

