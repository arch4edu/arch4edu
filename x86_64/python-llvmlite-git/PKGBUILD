#  Maintainer: Blair Bonnett <blair dot bonnett at gmail dot com>
# Contributor: Quan Guo <guotsuan at gmail dot com>

pkgname=python-llvmlite-git
_gitname=llvmlite
pkgver=0.42.0dev0.r2.g2488e03
pkgrel=1
pkgdesc="A lightweight LLVM Python binding for writing JIT compilers (Git version)"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python' 'llvm14-libs')
makedepends=(
  'git' 'llvm14' 'python-build' 'python-installer'
  'python-setuptools' 'python-wheel'
)
optdepends=(
  'python-graphviz: visualising control-flow graphs'
)
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
  LLVM_CONFIG=/usr/bin/llvm-config-14 python -m build --no-isolation --wheel
}

check() {
  cd "$srcdir/$_gitname"
  python runtests.py
}

package() {
  cd "${srcdir}/${_gitname}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
