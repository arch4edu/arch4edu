# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=brunsli
pkgver=0.1
pkgrel=4
pkgdesc='Lossless JPEG repacker'
arch=('x86_64')
url='https://github.com/google/brunsli/'
license=('MIT')
depends=('gcc-libs' 'glibc')
makedepends=('cmake' 'git' 'python')
source=("git+https://github.com/google/brunsli.git#tag=v${pkgver}"
        'git+https://github.com/google/brotli.git'
        'git+https://github.com/google/googletest.git'
        'git+https://github.com/google/highwayhash.git')
sha256sums=('842cb1ec23a6d244e6eebd1b253ae44e0bbff57c0fbf5dc8b153b10220ec4ca2'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
    git -C brunsli submodule init
    git -C brunsli config --local submodule.third_party/brotli.url "${srcdir}/brotli"
    git -C brunsli config --local submodule.third_party/googletest.url "${srcdir}/googletest"
    git -C brunsli config --local submodule.third_party/highwayhash.url "${srcdir}/highwayhash"
    git -C brunsli -c protocol.file.allow='always' submodule update
}

build() {
    cmake -B build -S brunsli \
        -G 'Unix Makefiles' \
        -DCMAKE_BUILD_TYPE:STRING='None' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DCMAKE_POLICY_VERSION_MINIMUM:STRING="3.5.0" \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -D -m755 build/{cbrunsli,dbrunsli} -t "${pkgdir}/usr/bin"
    install -D -m644 brunsli/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
