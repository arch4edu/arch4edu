# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=9.0.22
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
    'e69acbff805a25d2e6b7a3bc3cb4a107f61d6e61d38e538018f0f0d6dbb5c836'
    '6ceef1cb14af8ce3d06e17df67d0a80e5a22f3cd982792e517b7d85e8b695509'
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
