# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Frank Siegert < frank.siegert at googlemail dot com >
# Contributor: Scott Lawrence < bytbox at gmail dot com >
# Contributor: Thomas Dziedzic < gostrc at gmail dot com >
# Contributor: Sebastian Voecking < voeck at web dot de >

pkgname=root-extra
_pkgname=root
pkgver=6.08.04
pkgrel=1
provides=('root')
conflicts=('root')
pkgdesc='C++ data analysis framework and interpreter from CERN with extra features enabled.'
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
'libmysqlclient'
'postgresql-libs'
'pythia8'
'python'
'sqlite'
'tex-gyre-fonts'  # solve the pixelized font problem as per Arch Wiki
'unixodbc'
'unuran'
'xmlrpc-c'
'xrootd-abi0'
)
optdepends=('blas: Optional extensions to TMVA'
            'gcc-fortran: Enable the Fortran components of ROOT'
            'tcsh: Legacy CSH support'
)
options=('!emptydirs')
install=root-extra.install
source=("https://root.cern.ch/download/root_v${pkgver}.source.tar.gz"
'JupyROOT_encoding.patch'
'JupyROOT_fix.patch'
'root-extra.install'
'root.sh'
'root.xml'
'rootd'
'settings.cmake')
sha256sums=('51d8fb902b29223f4c621f7f316e3b9d9fe41cd53403e7274cb5cf47ade9c500'
            'dbf08ee3b506a2089f58d55ec9b1e6b77f337a6d2ebbb081e69cf729e531da3f'
            'a17309295f998ed826dcbf1b5d04de7ed44d64c35221806c75b775796578783d'
            'f1796729b0403026382bca43329692f5356c8ec46fc2c09f799a8b3d12d49a6f'
            '9d1f8e7ad923cb5450386edbbce085d258653c0160419cdd6ff154542cc32bd7'
            'b103d46705883590d9e07aafb890ec1150f63dc2ca5f40d67e6ebef49a6d0a32'
            '3c45b03761d5254142710b7004af0077f18efece7c95511910140d0542c8de8a'
            '40503aebd8a0ab5380a24d69145cf7d93d483d4d9330e4c23fb04e55c9ed2caf')
prepare(){
    cd ${_pkgname}-${pkgver}

    # Apply optional JupyROOT fixes while waiting for upstream to release
    # patch -p1 -i ${srcdir}/JupyROOT_encoding.patch
    # patch -p1 -i ${srcdir}/JupyROOT_fix.patch

    2to3 -w etc/dictpch/makepch.py 2>&1 > /dev/null
}

build() {
    [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
    cd ${srcdir}/build

    CFLAGS="${CFLAGS} -pthread" \
    CXXFLAGS="${CXXFLAGS} -pthread" \
    LDFLAGS="${LDFLAGS} -pthread -Wl,--no-undefined" \
    cmake -C ${srcdir}/settings.cmake ${srcdir}/${_pkgname}-${pkgver}

    make ${MAKEFLAGS}
}

package() {
    cd ${srcdir}/build

    make DESTDIR=${pkgdir} install

    install -D ${srcdir}/root.sh \
        ${pkgdir}/etc/profile.d/root.sh
    install -D ${srcdir}/rootd \
        ${pkgdir}/etc/rc.d/rootd
    install -D -m644 ${srcdir}/root.xml \
        ${pkgdir}/usr/share/mime/packages/root.xml

    install -D -m644 ${srcdir}/${_pkgname}-${pkgver}/build/package/debian/root-system-bin.desktop.in \
        ${pkgdir}/usr/share/applications/root-system-bin.desktop
    # replace @prefix@ with /usr for the desktop
    sed -e 's_@prefix@_/usr_' -i ${pkgdir}/usr/share/applications/root-system-bin.desktop

    # fix python env call
    sed -e 's/@python@/python/' -i ${pkgdir}/usr/lib/root/cmdLineUtils.py

    install -D -m644 ${srcdir}/${_pkgname}-${pkgver}/build/package/debian/root-system-bin.png \
        ${pkgdir}/usr/share/icons/hicolor/48x48/apps/root-system-bin.png

    # use a file that pacman can track instead of adding directly to ld.so.conf
    install -d ${pkgdir}/etc/ld.so.conf.d
    echo '/usr/lib/root' > ${pkgdir}/etc/ld.so.conf.d/root.conf

    rm -rf ${pkgdir}/etc/root/daemons
}
