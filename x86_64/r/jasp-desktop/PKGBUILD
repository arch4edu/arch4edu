#Maintainer: sukanka <su975853527 AT gmail.com>

_pkgname=jasp
_pkgver=0.16.3
pkgname=jasp-desktop
pkgver=0.16.3
pkgrel=1
pkgdesc="A complete statistical package for both Bayesian and Frequentist statistical methods"
arch=('x86_64')
url="https://github.com/jasp-stats/jasp-desktop"
license=('AGPL3')
makedepends=("cmake" 'boost' 'jsoncpp'
'openssl'
'autoconf'
'zlib'
'bison'
'flex'
'jags'
'gcc-fortran'
'qtcreator'
'git'
'patchelf'
)
depends=('r'
'qt6-5compat'
'readstat'
'libarchive'
'r-rinside'
'qt6-base'
'qt6-webengine'

# jaspBase
"r-jaspbase"
"r-jaspgraphs"
"r-jaspresults"
"r-jasptools"

#jaspCommon
"r-jaspdescriptives"
"r-jaspttests"
"r-jaspanova"
"r-jaspmixedmodels"
"r-jaspregression"
"r-jaspfrequencies"
"r-jaspfactor"

#jaspExtra
"r-jaspaudit"
"r-jaspbain"
"r-jaspbsts"
"r-jaspcircular"
"r-jaspcochrane"
"r-jaspdistributions"
"r-jaspequivalencettests"
"r-jaspjags"
"r-jasplearnbayes"
"r-jaspmachinelearning"
"r-jaspmetaanalysis"
"r-jaspnetwork"
"r-jaspprocesscontrol"
"r-jaspreliability"
"r-jaspsem"
"r-jaspsummarystatistics"
"r-jaspvisualmodeling"
"r-jaspprophet"
)
provides=($_pkgname)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/jasp-stats/jasp-desktop/archive/refs/tags/v${pkgver}.tar.gz"
'jasp.sh'
"jaspColumnEncoder::git+https://github.com/jasp-stats/jaspColumnEncoder.git"
'jaspResults::git+https://github.com/jasp-stats/jaspResults.git'
)
sha256sums=('6ce2062384761d88babf939e9a9a8c4aaa6737c3381cb0ede3c39f8576ba64b7'
            'e0714d980e7549b4c7dcbae50370e95b6ad2e7f0cf21a534ceb3a5a83ee583fd'
            'SKIP'
            'SKIP')

prepare(){
    cd $srcdir/${pkgname}-${pkgver}
    cp -rf $srcdir/jaspColumnEncoder/*  Common/jaspColumnEncoder
    cp -rf $srcdir/jaspResults/*        R-Interface/jaspResults

    find Tools/CMake -name *.cmake -print0 | xargs -0 sed -i "s|/usr/local|/usr|g"
    sed -i "s|lib='\${R_LIBRARY_PATH}'|lib='${srcdir}/usr/lib/R'|g"  Tools/CMake/R.cmake

    # Do NOT install modules here, they are listed in dependencies
    find Modules/ -name '*.in' -print0 | xargs -0 sed -i '1,$d;1a print("I am OK!")'
}


build(){
    cd $srcdir/${pkgname}-${pkgver}
    mkdir -p ${srcdir}/usr/lib/R
    cmake -S . -B build -DCUSTOM_R_PATH=/usr/lib/R -DLINUX_LOCAL_BUILD=OFF -DINSTALL_R_MODULES=OFF \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr/lib/${pkgname} -DCMAKE_INSTALL_LIBDIR=lib

        # -DBUILD_TESTS=ON does not work on linux.

    cmake --build build -- -j 5
}

package() {
    cd $srcdir/${pkgname}-${pkgver}/build
    make install DESTDIR=${pkgdir}
    install -Dm755 $srcdir/jasp.sh ${pkgdir}/usr/bin/jasp

    cd ${pkgdir}/usr/lib/${pkgname}
    mv share ${pkgdir}/usr
    mv Resources ${pkgdir}/usr/share/${pkgname}
    ln -s /usr/share/${pkgname} ${pkgdir}/usr/lib/${pkgname}/Resources

    rm -rf lib64
    rm -rf Modules/{renv-cache,*.log}


    # fix RPATH
    patchelf --add-rpath /usr/lib/R/library/RInside/lib/ \
        ${pkgdir}/usr/lib/jasp-desktop/bin/JASPEngine
    sed -i "s|^Exec.*|Exec=jasp %f|g" \
        ${pkgdir}/usr/share/applications/org.jaspstats.JASP.desktop

    rm -rf ${pkgdir}/usr/lib/jasp-desktop/{renv-root,renv-cache,bin/org.jaspstats.JASP}
}
