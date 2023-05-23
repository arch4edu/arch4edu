# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=9.0.2
_pkgver="$pkgver-1"
pkgrel=2
pkgdesc='GUI client for synchronizing your local files with seafile server'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('Apache')
depends=(
    "seafile>=$pkgver"
    'qt6-base'
    'qt6-webengine'
    'qt6-5compat'
)
optdepends=('gtk-update-icon-cache')
makedepends=('cmake' 'qt6-tools')
source=(
    "$pkgname-$_pkgver.tar.gz::$url/archive/v$_pkgver.tar.gz"
    'fix_build_with_QT6.diff'
)
sha256sums=(
    '5f3b616cdc4e527986fed220f5640b647c6c05215254c6070b70ed73a08c801b'
    '5fc54daff54d3ea4e263aea6c23b8c812fe5287e487a56bbf05cf935dd149229'
)

prepare() {
    cd "$srcdir/$pkgname-$_pkgver"
    patch -p1 -i "$srcdir/fix_build_with_QT6.diff"
}

build() {
    cmake -B build -S "$srcdir/$pkgname-$_pkgver" \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DBUILD_SHIBBOLETH_SUPPORT=ON
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
