# Maintainer: pingplug < aur at pingplug dot me >
# Maintainer: Adrià Arrufat <swiftscythe@gmail.com>
# Contributor: perlawk

pkgname=dlib
pkgver=19.24.6
pkgrel=2
pkgdesc="A general purpose cross-platform C++ library designed using contract programming and modern C++ techniques"
arch=('x86_64')
url="http://dlib.net"
license=('custom')
depends=('cblas'
         'lapack'
         'blas'
         'libjpeg-turbo'
         'libjxl'
         'libpng'
         'libwebp'
         'libx11')
optdepends=('ffmpeg: for FFmpeg support'
            'giflib: for GIF support'
            'sqlite: for sqlite support')
makedepends=('cmake' 'ninja')
source=("https://codeload.github.com/davisking/dlib/tar.gz/refs/tags/v${pkgver}")
sha256sums=('22513c353ec9c153300c394050c96ca9d088e02966ac0f639e989e50318c82d6')

build() {
    cd "${srcdir}"
    mkdir -p build && cd build
    cmake -GNinja \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib \
        -DBUILD_SHARED_LIBS=ON \
        -DCMAKE_BUILD_TYPE=Release \
        -DUSE_AVX_INSTRUCTIONS=OFF \
        -DDLIB_USE_CUDA=OFF \
        "../${pkgbase}-${pkgver}"
    ninja ${MAKEFLAGS:--j1}
}

package() {
    cd "${srcdir}/build"
    DESTDIR=${pkgdir} ninja install
    install -Dm644 "../${pkgbase}-${pkgver}/dlib/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgbase}/LICENSE"
    # remove redundant external libraries
    rm -r "${pkgdir}/usr/include/dlib/external"
}
