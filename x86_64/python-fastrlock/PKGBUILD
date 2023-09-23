# Maintainer: Leo Mao <leomaoyw at gmail dot com>
pkgname=python-fastrlock
_pkgname=fastrlock
pkgver=0.8.2
pkgrel=1
pkgdesc="A fast RLock implementation for CPython"
_github="scoder/fastrlock"
url="https://github.com/scoder/fastrlock"
arch=('x86_64')
license=('MIT')
depends=('python')
makedepends=('python' 'python-setuptools' 'cython')
source=("https://github.com/scoder/fastrlock/archive/v$pkgver.tar.gz")
md5sums=('e82127c20837472a0d0df167461a55c7')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
