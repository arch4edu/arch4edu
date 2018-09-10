# Maintainer: Andrew Crerar <crerar@archlinux.org>
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
pkgname="$_name-git"
pkgver=3.4.3.r121.gc331a214d0
pkgrel=1
pkgdesc="Open Source Computer Vision Library"
url="https://opencv.org/"
license=('BSD')
arch=('i686' 'x86_64')
depends=('intel-tbb' 'openexr' 'gst-plugins-base' 'libdc1394' 'cblas' 'lapack' 'libgphoto2' 'jasper')
makedepends=('git' 'cmake' 'python-numpy' 'python2-numpy' 'mesa' 'eigen' 'hdf5' 'lapacke' 'gtk3')
optdepends=('opencv-samples: samples'
            'gtk3: for the HighGUI module'
            'hdf5: Support for HDF5 format'
            'opencl-icd-loader: For coding with OpenCL'
            'python-numpy: Python 3 interface'
            'python2-numpy: Python 2 interface')
conflicts=('opencv')
provides=("$_name=$pkgver")
source=('git+https://github.com/opencv/opencv.git#branch=3.4'
        'git+https://github.com/opencv/opencv_contrib.git#branch=3.4')
sha512sums=('SKIP'
            'SKIP')

_cmakeopts=('-DWITH_OPENCL=ON'
            '-DWITH_OPENGL=ON'
            '-DWITH_TBB=ON'
            '-DOpenGL_GL_PREFERENCE=GLVND'
            '-DBUILD_WITH_DEBUG_INFO=OFF'
            '-DBUILD_TESTS=OFF'
            '-DBUILD_PERF_TESTS=OFF'
            '-DBUILD_EXAMPLES=ON'
            '-DINSTALL_C_EXAMPLES=ON'
            '-DINSTALL_PYTHON_EXAMPLES=ON'
            '-DCMAKE_INSTALL_PREFIX=/usr'
            '-DCMAKE_INSTALL_LIBDIR=lib'
            '-DCUDA_NVCC_FLAGS="--expt-relaxed-constexpr"')

# SSE only available from Pentium 3 onwards (i686 is way older)
[[ "$CARCH" = 'i686' ]] && _cmakeopts+=('-DCPU_BASELINE_DISABLE=SSE2')
[[ "$CARCH" = 'x86_64' ]] && _cmakeopts+=('-DCPU_BASELINE_DISABLE=SSE3 -DCPU_BASELINE_REQUIRE=SSE2')

pkgver() {
    cd "$srcdir/$_name"
    git describe --long | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

build() {
    mkdir -p build
    cd build

    cmake "${_cmakeopts[@]}" \
          -DOPENCV_EXTRA_MODULES_PATH="$srcdir"/opencv_contrib/modules \
          -DLAPACK_LIBRARIES="/usr/lib/liblapack.so;/usr/lib/libblas.so;/usr/lib/libcblas.so" \
          -DLAPACK_CBLAS_H="/usr/include/cblas.h" \
          -DLAPACK_LAPACKE_H="/usr/include/lapacke.h" \
          ../"$_name"

    make
}

package() {
    options=('staticlibs')

    cd build
    make DESTDIR="$pkgdir" install

    # install LICENSE file
    install -Dm644 "$srcdir"/"$_name"/LICENSE "$pkgdir"/usr/share/licenses/"$pkgname"

    cd "$pkgdir"/usr/share

    mv OpenCV opencv  # NOTE: Make the name casing consistent with what extra/opencv provides
}
