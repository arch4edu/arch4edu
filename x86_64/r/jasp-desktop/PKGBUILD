#Maintainer: sukanka <su975853527 AT gmail.com>

_pkgname=jasp
_pkgver=0.16.4
pkgname=jasp-desktop
pkgver=0.16.4
pkgrel=5
pkgdesc="A complete statistical package for both Bayesian and Frequentist statistical methods"
arch=('x86_64' 'aarch64')
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
'qt6-shadertools'

# jaspBase
"r-jaspbase"
"r-jaspgraphs"
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
"r-jaspprophet"
"r-jaspreliability"
"r-jaspsem"
"r-jaspsummarystatistics"
"r-jaspvisualmodeling"
)
provides=($_pkgname)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/jasp-stats/jasp-desktop/archive/refs/tags/v${pkgver}.tar.gz"
'jasp.sh'
"jaspColumnEncoder::git+https://github.com/jasp-stats/jaspColumnEncoder.git"
# only needed in v0.16.4
"Qt640.patch::https://github.com/jasp-stats/jasp-desktop/compare/v0.16.4..f2956103.diff"
)
sha256sums=('8671a8f73669e40c0ef4a9e088591a45559bc84bc6a3c745367ffcbca992602d'
            'e0714d980e7549b4c7dcbae50370e95b6ad2e7f0cf21a534ceb3a5a83ee583fd'
            'SKIP'
            '2e53de4fa2983b1a519b6ca0126cbac743e8048211369dcf9d3d58e0f786616d')

prepare(){
    cd $srcdir/${pkgname}-${pkgver}
    patch --strip=1 < ../Qt640.patch || true
    cp -rf $srcdir/jaspColumnEncoder/*  Common/jaspColumnEncoder

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

    cmake --build build
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
