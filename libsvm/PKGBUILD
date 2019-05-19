# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: saxonbeta <saxonbeta at gmail>
# Contributor: Pierre Gueth <pierre.gueth at gmail>
# Contributor: Daniel YC Lin <dlin.tw at gmail>
# Contributor: Tim Huetz <tim at huetz biz>

pkgname=libsvm
pkgver=3.23
_srcver="${pkgver/./}"
pkgrel=7
pkgdesc='A library for Support Vector Machines classification (includes binaries and bindings for python and java)'
arch=('i686' 'x86_64')
url='https://www.csie.ntu.edu.tw/~cjlin/libsvm/'
license=('BSD')
depends=('gcc-libs')
makedepends=('qt5-base' 'python')
optdepends=('qt5-base: for Qt5 interface with svm-toy'
            'python: for python modules and python CLI tools'
            'python2: for python2 modules'
            'gnuplot: for using svm-easy.py'
            'java-runtime: for java bindings')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/cjlin1/libsvm/archive/v${_srcver}.tar.gz"
        '001-libsvm-fix-qt-headers-path.patch'
        '002-libsvm-use-archlinux-flags.patch'
        '003-libsvm-fix-tools-path.patch')
sha256sums=('7a466f90f327a98f8ed1cb217570547bcb00077933d1619f3cb9e73518f38196'
            '01d28d48ca955921cff3ee39e6235fbcbe6f13587c056b05797388afc0c45432'
            'ba986c03199445ec0a9d1d113f54753e61f691ad4c66cad80b1f7d6ccf0c2d17'
            '58338a8eac252459c665eb6f1f03f4b86cd541b2c6942357329be022f3bb6fce')

prepare() {
    cd "${pkgname}-${_srcver}"
    
    patch -Np1 -i "${srcdir}/001-libsvm-fix-qt-headers-path.patch"
    patch -Np1 -i "${srcdir}/002-libsvm-use-archlinux-flags.patch"
    patch -Np1 -i "${srcdir}/003-libsvm-fix-tools-path.patch"
}

build() {
    printf '%s\n' '  -> Building library and CLI binaries...'
    cd "${pkgname}-${_srcver}"
    make lib all
    
    printf '%s\n' '  -> Building Qt5 interface...'
    cd svm-toy/qt
    make
}

package() {
    cd "${pkgname}-${_srcver}"
    
    local _pyver
    local _sover
    
    _pyver="$(python -c 'import sys; print("%s.%s" %sys.version_info[0:2])')"
    _sover="$(find . -maxdepth 1 -type f -regextype posix-basic -regex '.*libsvm.so.[0-9]$' | awk -F'.' '{ print $NF }')"
    
    # binaries
    install -D -m755 svm-predict        -t "${pkgdir}/usr/bin"
    install -D -m755 svm-scale          -t "${pkgdir}/usr/bin"
    install -D -m755 svm-train          -t "${pkgdir}/usr/bin"
    install -D -m755 svm-toy/qt/svm-toy -t "${pkgdir}/usr/bin"
    
    # library
    install -D -m755 "libsvm.so.${_sover}" -t "${pkgdir}/usr/lib"
    cd "${pkgdir}/usr/lib"
    ln -s "libsvm.so.${_sover}" libsvm.so
    
    # header
    cd "${srcdir}/${pkgname}-${_srcver}"
    install -D -m644 svm.h -t "${pkgdir}/usr/include/libsvm"
    
    # python modules
    ## NOTE: 'grid.py' can be used either as a python module or a CLI/tool
    ## https://github.com/cjlin1/libsvm/blob/v323/tools/README#L163-L164
    cd "${srcdir}/${pkgname}-${_srcver}/python"
    install -D -m644 commonutil.py -t "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm"
    install -D -m644 commonutil.py -t "${pkgdir}/usr/lib/python2.7/site-packages/libsvm"
    install -D -m644 svm.py        -t "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm"
    install -D -m644 svm.py        -t "${pkgdir}/usr/lib/python2.7/site-packages/libsvm"
    install -D -m644 svmutil.py    -t "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm"
    install -D -m644 svmutil.py    -t "${pkgdir}/usr/lib/python2.7/site-packages/libsvm"
    cd "${srcdir}/${pkgname}-${_srcver}/tools"
    install -D -m644 grid.py  -t "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm"
    install -D -m644 grid.py  -t "${pkgdir}/usr/lib/python2.7/site-packages/libsvm"
    sed -i '1s/python$/python2/' "${pkgdir}/usr/lib/python2.7/site-packages/libsvm/"{commonutil,grid,svm,svmutil}.py
    printf '' | install -D -m644 /dev/stdin "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm/__init__.py"
    printf '' | install -D -m644 /dev/stdin "${pkgdir}/usr/lib/python2.7/site-packages/libsvm/__init__.py"
    
    # python CLI/tools
    install -D -m755 checkdata.py "${pkgdir}/usr/bin/svm-checkdata.py"
    install -D -m755 easy.py      "${pkgdir}/usr/bin/svm-easy.py"
    install -D -m755 grid.py      "${pkgdir}/usr/bin/svm-grid.py"
    install -D -m755 subset.py    "${pkgdir}/usr/bin/svm-subset.py"
    
    # java
    cd "${srcdir}/${pkgname}-${_srcver}/java"
    install -D -m644 libsvm.jar -t "${pkgdir}/usr/share/java"
    
    # license
    cd "${srcdir}/${pkgname}-${_srcver}"
    install -D -m644 COPYRIGHT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
