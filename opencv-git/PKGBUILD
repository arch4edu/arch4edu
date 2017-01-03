# Maintainer: Andrew Crerar <andrew (at) crerar (dot) io>
# Contributor: Valentin Churavy <v.churavy@gmail.com>
# Contributor: Romain Reignier <rom.reignier@gmail.com>
# Contributor: Fabien Dubosson <fabien.dubosson@gmail.com>
# Contributor: David Manouchehri <david@davidmanouchehri.com>
# Contributor: CHEN Xing <cxcxcxcx@gmail.com>
# Contributor: Martin Imobersteg <martin.imobersteg@gmail.com>
# Contributor: Artyom Smirnov <smirnoffjr@gmail.com>
# Also largely inspired by `opencv` in extra, so including contributors too:
# Contributor: Ray Rashif <schiv@archlinux.org>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>

_name=opencv
pkgname="${_name}-git"
pkgver=3.2.0.r7.ga85b4b580
pkgrel=1
pkgdesc="Open Source Computer Vision Library"
url="http://opencv.org/"
license=('BSD')
arch=('i686' 'x86_64')
depends=('intel-tbb' 'openexr' 'xine-lib' 'libdc1394' 'gtkglext')
makedepends=('git' 'cmake' 'python2-numpy' 'python-numpy' 'mesa' 'eigen')
optdepends=('opencv-samples'
            'eigen'
            'opencl-icd-loader: For coding with OpenCL'
            'python-numpy: Python 3 interface'
            'python2-numpy: Python 2 interface')
conflicts=('opencv' 'opencv-git')
provides=("${_name}=${pkgver}")
source=('git+https://github.com/opencv/opencv.git'
        'git+https://github.com/opencv/opencv_contrib.git')
sha512sums=('SKIP'
            'SKIP')

_cmakeopts=('-D WITH_OPENCL=ON'
            '-D WITH_OPENGL=ON'
            '-D WITH_TBB=ON'
            '-D WITH_XINE=ON'
            '-D BUILD_WITH_DEBUG_INFO=OFF'
            '-D BUILD_TESTS=OFF'
            '-D BUILD_PERF_TESTS=OFF'
            '-D BUILD_EXAMPLES=ON'
            '-D INSTALL_C_EXAMPLES=ON'
            '-D INSTALL_PYTHON_EXAMPLES=ON'
            '-D CMAKE_BUILD_TYPE=Release'
            '-D CMAKE_INSTALL_PREFIX=/usr'
            '-D CMAKE_SKIP_RPATH=ON')

# SSE only available from Pentium 3 onwards (i686 is way older)
[[ "$CARCH" = 'i686' ]] && \
    _cmakeopts+=('-D ENABLE_SSE=OFF'
                 '-D ENABLE_SSE2=OFF'
                 '-D ENABLE_SSE3=OFF')

pkgver() {
    cd "${srcdir}/${_name}"
    git describe --long | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${_name}"

    cmake ${_cmakeopts[@]} \
      -DOPENCV_EXTRA_MODULES_PATH="${srcdir}/opencv_contrib/modules" \
      .

    make
}

package() {
    options=('staticlibs')

    cd "${srcdir}/${_name}"

    make DESTDIR="${pkgdir}" install

    # install LICENSE file
    install -Dm644 "${srcdir}/${_name}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
