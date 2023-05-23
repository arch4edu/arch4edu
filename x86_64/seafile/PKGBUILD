# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile
pkgver=9.0.2
_pkgver="$pkgver-1"
pkgrel=2
pkgdesc='An online file storage and collaboration tool'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('GPL2')
depends=(
    'libsearpc'
    'libevent'
    'fuse'
    'python-future'
    'sqlite'
)
makedepends=(
    'vala'
    'intltool'
)
conflicts=('seafile-server')
source=(
    "seafile-$_pkgver.tar.gz::$url/archive/v$_pkgver.tar.gz"
    "seaf-cli@.service"
)
sha256sums=(
    '619dd87bcb3a2d1a8e3ce08ab53d73e622b7d5591d2ac33f719dd53c82e8467b'
    'c37510109c1de64c774896df39aece240c056b54414d2119fca01860211156ba'
)
provides=('seafile-client-cli')

prepare() {
    cd "$srcdir/seafile-$_pkgver"
    sed -i 's|(DESTDIR)@prefix@|@prefix@|' './lib/libseafile.pc.in'
}

build() {
    cd "$srcdir/seafile-$_pkgver"
    ./autogen.sh
    ./configure \
        --enable-console \
        --prefix='/usr' \
        PYTHON='/usr/bin/python'
    make
}

package() {
    cd "$srcdir/seafile-$_pkgver"
    make DESTDIR="$pkgdir" install

    install -Dm644 \
        "$srcdir/seaf-cli@.service" \
        "$pkgdir/usr/lib/systemd/system/seaf-cli@.service"
}
