# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=brunsli
pkgver=0.1
pkgrel=1
pkgdesc='Lossless JPEG repacker'
arch=('x86_64')
url='https://github.com/google/brunsli/'
license=('MIT')
depends=('gcc-libs')
makedepends=('git' 'cmake')
source=("git+https://github.com/google/brunsli.git#tag=v${pkgver}"
        'git+https://github.com/google/brotli.git'
        'git+https://github.com/google/googletest'
        'git+https://github.com/google/highwayhash.git')
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
    cd brunsli
    git submodule init
    git config --local submodule.third_party/brotli.url "${srcdir}/brotli"
    git config --local submodule.third_party/googletest.url "${srcdir}/googletest"
    git config --local submodule.third_party/highwayhash.url "${srcdir}/highwayhash"
    git submodule update
}

build() {
    cmake -B build -S brunsli \
        -DCMAKE_BUILD_TYPE:STRING='None' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -Wno-dev
    make -C build
}

package() {
    make -C build DESTDIR="$pkgdir" install
    install -D -m755 build/cbrunsli -t "${pkgdir}/usr/bin"
    install -D -m755 build/dbrunsli -t "${pkgdir}/usr/bin"
    install -D -m644 brunsli/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
