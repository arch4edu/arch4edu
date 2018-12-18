# Maintainer: Sherlock Holo <sherlockya@gmail.com>
# Collaborator: user6553591 <Message on Reddit>

pkgname=python-websockets
pkgver=7.0
pkgrel=1
pkgdesc="An implementation of the WebSocket Protocol (RFC 6455)"
arch=('i686' 'x86_64')
url="https://github.com/aaugustin/websockets"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=("https://github.com/aaugustin/websockets/archive/$pkgver.tar.gz")
sha256sums=('39391d6d8eb1d3973fc104f32df54de653e3d7aa89584a43c761a1b5cb8ed74d')

build() {
    cd "$srcdir"/websockets-$pkgver
    python setup.py build
}

package() {
    cd "$srcdir"/websockets-$pkgver
    python setup.py install --skip-build --optimize=1 --root="$pkgdir"
    install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
