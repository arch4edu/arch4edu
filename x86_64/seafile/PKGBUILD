# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile
pkgver=9.0.17
pkgrel=1
pkgdesc='An online file storage and collaboration tool'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('GPL2')
depends=(
    'argon2'
    'libsearpc'
    'libevent'
    'libwebsockets'
    'fuse'
    'sqlite'
)
makedepends=(
    'vala'
    'intltool'
)
conflicts=('seafile-server')
source=(
    "seafile-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
    "seaf-cli@.service"
)
sha256sums=(
    '4e7f284d1b98797c7e2ebc711013a576df5ac6e5bbecf209724efe69514b9ed3'
    'c37510109c1de64c774896df39aece240c056b54414d2119fca01860211156ba'
)
provides=('seafile-client-cli')

prepare() {
    cd "$srcdir/seafile-$pkgver"
    sed -i 's|(DESTDIR)@prefix@|@prefix@|' './lib/libseafile.pc.in'
}

build() {
    cd "$srcdir/seafile-$pkgver"
    ./autogen.sh
    ./configure \
        --enable-console \
        --prefix='/usr' \
        PYTHON='/usr/bin/python'
    make
}

package() {
    cd "$srcdir/seafile-$pkgver"
    make DESTDIR="$pkgdir" install

    install -Dm644 \
        "$srcdir/seaf-cli@.service" \
        "$pkgdir/usr/lib/systemd/system/seaf-cli@.service"
}
