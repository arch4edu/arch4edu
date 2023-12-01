# Maintainer: Leo Mao <leomaoyw at gmail dot com>
pkgname=python-fastrlock
_pkgname=fastrlock
pkgver=0.8.2
pkgrel=2
pkgdesc="A fast RLock implementation for CPython"
_github="scoder/fastrlock"
url="https://github.com/scoder/fastrlock"
arch=('x86_64')
license=('MIT')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'cython')
source=("https://github.com/scoder/fastrlock/archive/v$pkgver.tar.gz")
md5sums=('e82127c20837472a0d0df167461a55c7')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python -m installer --destdir="$pkgdir" --compile-bytecode=1 dist/*.whl
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
