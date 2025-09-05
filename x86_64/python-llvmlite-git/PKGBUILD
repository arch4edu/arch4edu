#  Maintainer: Blair Bonnett <blair dot bonnett at gmail dot com>
# Contributor: Quan Guo <guotsuan at gmail dot com>

pkgname=python-llvmlite-git
pkgver=0.46.0dev0.r2.g81461681
pkgrel=1
pkgdesc="A lightweight LLVM Python binding for writing JIT compilers (Git version)"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD-2-Clause')

depends=(
  'gcc-libs'
  'glibc'
  'python'
  'llvm-libs'
)
makedepends=(
  'cmake'
  'git'
  'llvm'
  'python-build'
  'python-installer'
  'python-setuptools'
)
optdepends=(
  'python-graphviz: visualising control-flow graphs'
)
provides=("python-llvmlite=$pkgver")
conflicts=('python-llvmlite')

source=(
  'llvmlite::git+https://github.com/numba/llvmlite.git'
)
sha256sums=(
  'SKIP'
)

pkgver() {
  cd llvmlite
  git describe --long | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

build() {
  cd llvmlite
  export LLVMLITE_SHARED=1
  python -m build --no-isolation --wheel
}

check() {
  cd llvmlite
  python runtests.py
}

package() {
  cd llvmlite
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # Remove tests from final package.
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -r "$pkgdir/$site_packages/llvmlite/tests"
}
