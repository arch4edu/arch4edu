# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=9.0.14
pkgrel=1
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
    "$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
    'fix_build_with_QT6.diff'
)
sha256sums=(
    '540ea559dc8773ce20232aec103d381cb7f2efe11cefbb0c14db40455a7800e4'
    '3b07339e4cd5f453d4cbec400201daa35c5813761f241b56793aab553362c068'
)

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    patch -p1 -i "$srcdir/fix_build_with_QT6.diff"
}

build() {
    cmake -B build -S "$srcdir/$pkgname-$pkgver" \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DBUILD_SHIBBOLETH_SUPPORT=ON
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
