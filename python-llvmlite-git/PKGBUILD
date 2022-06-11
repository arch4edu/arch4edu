#  Maintainer: Blair Bonnett <blair dot bonnett at gmail dot com>
# Contributor: Quan Guo <guotsuan at gmail dot com>

pkgname=python-llvmlite-git
_gitname=llvmlite
pkgver=0.38.0dev0.r93.g00320f6
pkgrel=1
pkgdesc="A lightweight LLVM python binding for writing JIT compilers (Git version)"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python' 'llvm11-libs')
makedepends=('git' 'llvm11')
provides=("python-llvmlite=$pkgver")
conflicts=('python-llvmlite')
source=(${_gitname}::git+https://github.com/numba/llvmlite.git)
sha256sums=('SKIP')

pkgver() {
  cd "$_gitname"
  git describe --long | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

build() {
  cd "$srcdir/$_gitname"
  python setup.py build
}

check() {
  cd "$srcdir/$_gitname"
  python runtests.py
}

package() {
  cd ${srcdir}/${_gitname}
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
