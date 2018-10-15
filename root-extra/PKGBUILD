# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Frank Siegert < frank.siegert at googlemail dot com >
# Contributor: Scott Lawrence < bytbox at gmail dot com >
# Contributor: Thomas Dziedzic < gostrc at gmail dot com >
# Contributor: Sebastian Voecking < voeck at web dot de >

pkgname=root-extra
_pkgname=root
pkgver=6.14.04
pkgrel=2
provides=('root' 'root-extra')
conflicts=('root')
pkgdesc='C++ data analysis framework and interpreter from CERN with extra features enabled.'
arch=('i686' 'x86_64')
url='http://root.cern.ch'
license=('LGPL2.1')
makedepends=('cmake'
             'llvm50>=5.0.2-5')
depends=('cfitsio'
         'cern-vdt'
         'fcgi'
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
         'pythia>=8.2.23-3'
         'python'
         'sqlite'
         'tex-gyre-fonts'  # solve the pixelized font problem as per Arch Wiki
         'unixodbc'
         'unuran'
         'xmlrpc-c'
         'xrootd>=4.6.0-2'
         'xxhash>=0.6.5-1')
optdepends=('blas: Optional extensions to TMVA'
            'go: Go language support'
            'gcc-fortran: Enable the Fortran components of ROOT'
            'ocaml: OCAML support'
            'python-numpy: numpy bindings for PyMVA'
            'tcsh: Legacy CSH support'
            'z3: Z3 Theorem prover support')
options=('!emptydirs')
install=root-extra.install
source=("https://root.cern.ch/download/root_v${pkgver}.source.tar.gz"
        'root-extra.install'
        'root.sh'
        'root.xml'
        'rootd'
        'settings.cmake'
        'exclude_clang_from_install_directive.patch'
        'fix_tmva_numpy_dependency.patch')
sha256sums=('463ec20692332a422cfb5f38c78bedab1c40ab4d81be18e99b50cf9f53f596cf'
            'f1796729b0403026382bca43329692f5356c8ec46fc2c09f799a8b3d12d49a6f'
            '9d1f8e7ad923cb5450386edbbce085d258653c0160419cdd6ff154542cc32bd7'
            '50c08191a5b281a39aa05ace4feb8d5405707b4c54a5dcba061f954649c38cb0'
            '3c45b03761d5254142710b7004af0077f18efece7c95511910140d0542c8de8a'
            '05c584402583ec85f813af83683b85bea33b58e103f25294c0c826de76a4baa2'
            'f2d07ccfa65dc0db8b41e36b67cc4cf471a0dec318f0f9f883711c5d2c0e296b'
            'bc0a31992c0da5004d6d9be8f0236e77185245f218ec49a6d86d9279c7bbb868')
prepare() {
    cd "${_pkgname}-${pkgver}"

    2to3 -w etc/dictpch/makepch.py 2>&1 > /dev/null

    patch -p1 -i "${srcdir}/exclude_clang_from_install_directive.patch"
    patch -p1 -i "${srcdir}/fix_tmva_numpy_dependency.patch"

    mkdir -p "${srcdir}/build"
    cd "${srcdir}/build"

    CFLAGS="${CFLAGS} -pthread" \
    CXXFLAGS="${CXXFLAGS} -pthread" \
    LDFLAGS="${LDFLAGS} -pthread -Wl,--no-undefined" \
    cmake -C "${srcdir}/settings.cmake" "${srcdir}/${_pkgname}-${pkgver}"
}

build() {
    cd "${srcdir}/build"

    make ${MAKEFLAGS}
}

package() {
    cd "${srcdir}/build"

    make DESTDIR="${pkgdir}" install

    install -D "${srcdir}/root.sh" \
        "${pkgdir}/etc/profile.d/root.sh"
    install -D "${srcdir}/rootd" \
        "${pkgdir}/etc/rc.d/rootd"
    install -D -m644 "${srcdir}/root.xml" \
        "${pkgdir}/usr/share/mime/packages/root.xml"

    install -D -m644 "${srcdir}/${_pkgname}-${pkgver}/build/package/debian/root-system-bin.desktop.in" \
        "${pkgdir}/usr/share/applications/root-system-bin.desktop"

    # replace @prefix@ with /usr for the desktop
    sed -e 's_@prefix@_/usr_' -i "${pkgdir}/usr/share/applications/root-system-bin.desktop"

    # fix python env call
    sed -e 's/@python@/python/' -i "${pkgdir}/usr/lib/root/cmdLineUtils.py"

    install -D -m644 "${srcdir}/${_pkgname}-${pkgver}/build/package/debian/root-system-bin.png" \
        "${pkgdir}/usr/share/icons/hicolor/48x48/apps/root-system-bin.png"

    # use a file that pacman can track instead of adding directly to ld.so.conf
    install -d "${pkgdir}/etc/ld.so.conf.d"
    echo '/usr/lib/root' > "${pkgdir}/etc/ld.so.conf.d/root.conf"

    rm -rf "${pkgdir}/etc/root/daemons"
}
