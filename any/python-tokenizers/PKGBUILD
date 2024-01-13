# Maintainer: xiota / aur.chaotic.cx
# Contributor: Filip Graliński <filipg@amu.edu.pl>

: ${CARGO_HOME:=${SRCDEST:-${startdir:?}}/cargo}

_gitname="tokenizers"
_pkgname="python-$_gitname"
pkgname="$_pkgname"
pkgver=0.15.0
pkgrel=1
pkgdesc='Fast State-of-the-Art Tokenizers optimized for Research and Production'
url="https://github.com/huggingface/tokenizers"
license=('Apache')
arch=('i686' 'x86_64')

depends=(
  'python'
)
makedepends=(
  'git'
  'python-build'
  'python-installer'
  'python-maturin'
  'python-setuptools-rust'
  'python-wheel'
)

_pkgsrc="$_gitname"
source=("$_pkgsrc"::"git+$url.git#tag=v${pkgver%%.r*}")
sha256sums=('SKIP')

prepare() {
  export CARGO_HOME
  export GIT_DIR='.'
  export RUSTUP_TOOLCHAIN=stable

  cd "$_pkgsrc/bindings/python"
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  export CARGO_HOME
  export GIT_DIR='.'
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR="${CARGO_TARGET_DIR:-target}"

  cd "$_pkgsrc/bindings/python"
  cargo build --frozen --release
  python -m build --no-isolation --wheel
}

package() {
  cd "$_pkgsrc/bindings/python"
  python -m installer --destdir="${pkgdir:?}" dist/*.whl
}
