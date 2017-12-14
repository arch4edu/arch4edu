# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Frank Siegert < frank.siegert at googlemail dot com >
# Contributor: Scott Lawrence < bytbox at gmail dot com >
# Contributor: Thomas Dziedzic < gostrc at gmail dot com >
# Contributor: Sebastian Voecking < voeck at web dot de >

pkgname=root
pkgver=6.12.04
pkgrel=1
pkgdesc='C++ data analysis framework and interpreter from CERN.'
arch=('i686' 'x86_64')
url='http://root.cern.ch'
license=('LGPL2.1')
makedepends=('cmake')
depends=('cfitsio'
         'fftw'
         'ftgl'
         'gl2ps'
         'glew'
         'graphviz'
         'gsl'
         'hicolor-icon-theme'
         'intel-tbb'
         'libafterimage'
         'libiodbc'
         'libmariadbclient'
         'postgresql-libs'
         'python'
         'sqlite'
         'tex-gyre-fonts'  # solve the pixelized font problem as per Arch Wiki
         'unixodbc'
         'unuran'
         'xmlrpc-c')
optdepends=('blas: Optional extensions to TMVA'
            'fcgi: Language independent, high performant extension to CGI'
            'go: Go language support'
            'gcc-fortran: Enable the Fortran components of ROOT'
            'ocaml: OCAML support'
            'pythia: Pythia8 support'
            'python-numpy: numpy bindings'
            'tcsh: Legacy CSH support'
            'xrootd: XRootD support'
            'z3: Z3 Theorem prover support')
options=('!emptydirs')
install=root.install
source=("https://root.cern.ch/download/root_v${pkgver}.source.tar.gz"
        'root.install'
        'root.sh'
        'root.xml'
        'rootd'
        'settings.cmake')
sha256sums=('f438f2ae6e25496fa81df525935fb0bf2a403855d95c40b3e0f3a3e1e861a085'
            '72ba38e0faffa084ac2f787f360201f72b1733d27e36c3cb88eb2f3a4716fa61'
            '9d1f8e7ad923cb5450386edbbce085d258653c0160419cdd6ff154542cc32bd7'
            '50c08191a5b281a39aa05ace4feb8d5405707b4c54a5dcba061f954649c38cb0'
            '3c45b03761d5254142710b7004af0077f18efece7c95511910140d0542c8de8a'
            'a8db29f6acf32659daca8de35481b25ed847b2182e6033940f3568f3d1ad22fb')
prepare() {
    cd "${pkgname}-${pkgver}"

    msg2 'Adjusting to Python3...'
    2to3 -w etc/dictpch/makepch.py 2>&1 > /dev/null
}

build() {
    mkdir -p "${srcdir}/build"
    cd "${srcdir}/build"

    msg2 'Configuring...'
    CFLAGS="${CFLAGS} -pthread" \
    CXXFLAGS="${CXXFLAGS} -pthread" \
    LDFLAGS="${LDFLAGS} -pthread -Wl,--no-undefined" \
    cmake -C "${srcdir}/settings.cmake" "${srcdir}/${pkgname}-${pkgver}"

    msg2 'Compiling...'
    make ${MAKEFLAGS}
}

package() {
    cd "${srcdir}/build"

    msg2 'Installing...'
    make DESTDIR="${pkgdir}" install

    install -D "${srcdir}/root.sh" \
        "${pkgdir}/etc/profile.d/root.sh"
    install -D "${srcdir}/rootd" \
        "${pkgdir}/etc/rc.d/rootd"
    install -D -m644 "${srcdir}/root.xml" \
        "${pkgdir}/usr/share/mime/packages/root.xml"

    install -D -m644 "${srcdir}/${pkgname}-${pkgver}/build/package/debian/root-system-bin.desktop.in" \
        "${pkgdir}/usr/share/applications/root-system-bin.desktop"
    # replace @prefix@ with /usr for the desktop
    sed -e 's_@prefix@_/usr_' -i "${pkgdir}/usr/share/applications/root-system-bin.desktop"

    # fix python env call
    sed -e 's/@python@/python/' -i "${pkgdir}/usr/lib/root/cmdLineUtils.py"

    install -D -m644 "${srcdir}/${pkgname}-${pkgver}/build/package/debian/root-system-bin.png" \
        "${pkgdir}/usr/share/icons/hicolor/48x48/apps/root-system-bin.png"

    msg2 'Updating system config...'
    # use a file that pacman can track instead of adding directly to ld.so.conf
    install -d "${pkgdir}/etc/ld.so.conf.d"
    echo '/usr/lib/root' > "${pkgdir}/etc/ld.so.conf.d/root.conf"

    msg2 'Cleaning up...'
    rm -rf "${pkgdir}/etc/root/daemons"
}
