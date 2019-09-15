# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: saxonbeta <saxonbeta at gmail>
# Contributor: Pierre Gueth <pierre.gueth at gmail>
# Contributor: Daniel YC Lin <dlin.tw at gmail>
# Contributor: Tim Huetz <tim at huetz biz>

pkgname=libsvm
pkgver=3.24
_srcver="${pkgver/./}"
pkgrel=1
pkgdesc='A library for Support Vector Machines classification (includes binaries and bindings for python and java)'
arch=('x86_64')
url='https://www.csie.ntu.edu.tw/~cjlin/libsvm/'
license=('BSD')
depends=('gcc-libs')
makedepends=('qt5-base' 'python')
optdepends=('qt5-base: for Qt5 interface with svm-toy'
            'python: for python modules and python CLI tools'
            'gnuplot: for using svm-easy.py'
            'java-runtime: for java bindings')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/cjlin1/libsvm/archive/v${_srcver}.tar.gz"
        '001-libsvm-fix-qt-headers-path.patch'
        '002-libsvm-use-archlinux-flags.patch'
        '003-libsvm-fix-tools-path.patch')
sha256sums=('3ba1ac74ee08c4dd57d3a9e4a861ffb57dab88c6a33fd53eac472fc84fbb2a8f'
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
    cd "${pkgname}-${_srcver}"
    
    printf '%s\n' '  -> Building library and CLI binaries...'
    make lib all
    
    printf '%s\n' '  -> Building Qt5 interface...'
    make -C svm-toy/qt
}

package() {
    cd "${pkgname}-${_srcver}"
    
    local _pyver
    local _sover
    _pyver="$(python -c 'import sys; print("%s.%s" %sys.version_info[0:2])')"
    _sover="$(find . -maxdepth 1 -type f -regextype posix-basic -regex '.*/libsvm.so.[0-9]*$' | awk -F'.' '{ print $NF }')"
    
    # binaries
    install -D -m755 svm-predict        -t "${pkgdir}/usr/bin"
    install -D -m755 svm-scale          -t "${pkgdir}/usr/bin"
    install -D -m755 svm-train          -t "${pkgdir}/usr/bin"
    install -D -m755 svm-toy/qt/svm-toy -t "${pkgdir}/usr/bin"
    
    # library
    install -D -m755 "libsvm.so.${_sover}" -t "${pkgdir}/usr/lib"
    ln -s "libsvm.so.${_sover}" "${pkgdir}/usr/lib/libsvm.so"
    
    # header
    install -D -m644 svm.h -t "${pkgdir}/usr/include/libsvm"
    
    # python modules
    ## NOTE: 'grid.py' can be used either as a python module or a CLI/tool
    ## https://github.com/cjlin1/libsvm/blob/v324/tools/README#L163-L164
    install -D -m644 python/commonutil.py -t "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm"
    install -D -m644 python/svm.py        -t "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm"
    install -D -m644 python/svmutil.py    -t "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm"
    ln -s ../../../../bin/svm-grid.py        "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm/grid.py"
    printf '' | install -D -m644 /dev/stdin  "${pkgdir}/usr/lib/python${_pyver}/site-packages/libsvm/__init__.py"
    
    # python CLI/tools
    install -D -m755 tools/checkdata.py "${pkgdir}/usr/bin/svm-checkdata.py"
    install -D -m755 tools/easy.py      "${pkgdir}/usr/bin/svm-easy.py"
    install -D -m755 tools/grid.py      "${pkgdir}/usr/bin/svm-grid.py"
    install -D -m755 tools/subset.py    "${pkgdir}/usr/bin/svm-subset.py"
    
    # java
    install -D -m644 java/libsvm.jar -t "${pkgdir}/usr/share/java"
    
    # license
    install -D -m644 COPYRIGHT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
