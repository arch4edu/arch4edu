# Maintainer: Kyle Manna <kyle[at]kylemanna[d0t]com>
pkgname=python-ntplib
_pkgname=${pkgname/python-/}
pkgver=0.4.0
pkgrel=1
pkgdesc="Simple interface to query NTP servers from Python"
url="https://github.com/cf-natali/ntplib"
depends=('python')
makedepends=('python-build'
             'python-installer'
             'python-setuptools'
             'python-wheel'
            )
license=('MIT')
arch=('any')
source=("https://github.com/cf-natali/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('dcb87eaa875aa7a041ca8f49a38c4a8264eb73e5f8b421767b9d541f61a0c050')

build() {
    cd "$srcdir/$_pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$_pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl

    rm -rf ${pkgdir}/usr/lib/python*/site-packages/tests/

    install -d "$pkgdir/usr/share/licenses/$pkgname/"
    install -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname"
}

