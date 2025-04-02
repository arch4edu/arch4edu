# Maintainer: pingplug < aur at pingplug dot me >
# Maintainer: Adrià Arrufat <swiftscythe@gmail.com>
# Contributor: perlawk

pkgname=dlib
pkgver=19.24.8
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
sha256sums=('819cfd28639fe80ca28039f591a15e01772b7ada479de4a002b95bcb8077ce80')

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
