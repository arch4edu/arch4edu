# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

pkgname=console-bridge
_pkgname=console_bridge
pkgver=1.0.2
pkgrel=2
pkgdesc="A ROS-independent package for logging that seamlessly pipes into rosconsole/rosout for ROS-dependent packages."
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7hv' 'aarch64')
url="http://www.ros.org/"
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake' 'cppcheck')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/$_pkgname/archive/$pkgver.tar.gz" "fix_repository_path.patch")
sha256sums=('303a619c01a9e14a3c82eb9762b8a428ef5311a6d46353872ab9a904358be4a4'
            '2a5df5a0876791793805111b82e3ae159d3cdc04218f351f014b4d9461ceb26d')

prepare() {
    patch -d "$_pkgname-$pkgver" -p0 -i "$srcdir/fix_repository_path.patch"
}

build() {
    cmake -B "build-$pkgver" -S "$_pkgname-$pkgver" \
        -DBUILD_TESTING=ON \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5
    cmake --build "build-$pkgver"
}

check() {
    AMENT_CPPCHECK_ALLOW_SLOW_VERSIONS=1 cmake --build "build-$pkgver" -t test
}

package() {
    DESTDIR="$pkgdir/" cmake --install "build-$pkgver"

    # install licence
    install -Dm644 "$_pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
