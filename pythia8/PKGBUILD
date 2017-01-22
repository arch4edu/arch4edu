# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Joshua Ellis < josh at jpellis dot me >
# Contributor: Stefano Campanella < stefanocampanella1729 at gmail dot com >
pkgname=pythia8
_pkgname=pythia
pkgver=8.2.19
_pkgid=$_pkgname`echo ${pkgver} | tr -d '.'`
pkgrel=3
pkgdesc="Generation of high-energy physics events."
arch=('i686' 'x86_64')
url="http://home.thep.lu.se/Pythia/"
license=('GPL')
depends=('bash' 'boost-libs')
provides=('pythia')
conflicts=('pythia')
source=("http://home.thep.lu.se/~torbjorn/${pkgname}/${_pkgid}.tgz"
'pythia.sh')
md5sums=('3459b52b5da1deae52cbddefa6196feb'
         '0320534e1be7155cfb8ee19c7f8480cc')
_srcpath=${srcdir}/${_pkgid}
options=('!emptydirs')

build(){
    cd ${srcdir}/${_pkgid}
  ./configure --prefix=/usr \
    --prefix-include=/usr/include/ \
    --prefix-lib=/usr/lib/ \
    --enable-shared \
    --with-boost \
    --with-boost-include=/usr/include/ \
    --with-boost-lib=/usr/lib/ \
    --with-gzip \
    --with-gzip-include=/usr/include/ \
    --with-gzip-lib=/usr/lib/ \
    --with-python \
    --with-python-include=/usr/include/python3.5m/ \
    --with-python-lib=/usr/lib/python3.5/ \
    --cxx-common='-fPIC -O3 -march=native'

    make ${MAKEFLAGS}
}

package() {
    mkdir -p "${pkgdir}/usr"
    install -Dm755 "${srcdir}/${_pkgid}/bin/pythia8-config" "${pkgdir}/usr/bin/pythia8-config"
    install -D "${srcdir}/pythia.sh" "${pkgdir}/etc/profile.d/pythia.sh"

    cp -r "${srcdir}/${_pkgid}/include" "${pkgdir}/usr/"
    cp -r "${srcdir}/${_pkgid}/share" "${pkgdir}/usr/"
    cp -r "${srcdir}/${_pkgid}/examples" "${pkgdir}/usr/share/Pythia8/"

    install -Dm755 "${srcdir}/${_pkgid}/lib/libpythia8.so" "${pkgdir}/usr/lib/libpythia8.so"
    install -Dm755 "${srcdir}/${_pkgid}/lib/_pythia8.so" "${pkgdir}/usr/lib/python3.5/site-packages/_pythia8.so"
    install -Dm755 "${srcdir}/${_pkgid}/lib/pythia8.py" "${pkgdir}/usr/lib/python3.5/site-packages/pythia8.py"
}
