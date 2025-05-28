# Maintainer: pingplug < aur at pingplug dot me >
# Maintainer: Adrià Arrufat <swiftscythe@gmail.com>
# Contributor: perlawk

pkgname=dlib
pkgver=20.0
pkgrel=1
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
sha256sums=('705749801c7896f5c19c253b6be639f4cef2c1831a9606955f01b600b3d86d80')

build() {
    cd "${srcdir}/${pkgbase}-${pkgver}"
    cmake -GNinja \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib \
        -DBUILD_SHARED_LIBS=ON \
        -DCMAKE_BUILD_TYPE=Release \
        -DUSE_AVX_INSTRUCTIONS=OFF \
        -DDLIB_USE_CUDA=OFF \
        -B build .
    ninja -C build ${MAKEFLAGS:--j1}
}

package() {
    cd "${srcdir}/${pkgbase}-${pkgver}/build"
    DESTDIR=${pkgdir} ninja install
    install -Dm644 "../dlib/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgbase}/LICENSE"
    # remove redundant external libraries
    rm -r "${pkgdir}/usr/include/dlib/external"
}
