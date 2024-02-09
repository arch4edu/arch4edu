# Maintainer:
# Contributor: Filip Graliński <filipg@amu.edu.pl>

: ${CARGO_HOME:=${SRCDEST:-$startdir}/cargo-home}

_gitname="tokenizers"
_pkgname="python-$_gitname"
pkgname="$_pkgname"
pkgver=0.15.1
pkgrel=1
pkgdesc='Fast State-of-the-Art Tokenizers optimized for Research and Production'
url="https://github.com/huggingface/tokenizers"
license=('Apache-2.0')
arch=('i686' 'x86_64')

depends=(
  'python'
  'oniguruma'
)
makedepends=(
  'clang'
  'rust-bindgen'
  'git'
  'python-build'
  'python-installer'
  'python-maturin'
  'python-setuptools-rust'
  'python-wheel'
)

options=('!lto')

_pkgsrc="$_gitname"
source=("$_pkgsrc"::"git+$url.git#tag=v${pkgver%%.r*}")
sha256sums=('SKIP')

prepare() {
  export CARGO_HOME
  export GIT_DIR='.'
  export RUSTUP_TOOLCHAIN=stable

  cd "$_pkgsrc/bindings/python"

  # sed -E -e 's@, default-features = false@@' -i Cargo.toml

  sed -E -e 's@defaut@default@' -i Cargo.toml

  cargo update
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  export CARGO_HOME
  export GIT_DIR='.'
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target

  #export RUSTONIG_SYSTEM_LIBONIG=1

  cd "$_pkgsrc/bindings/python"
  cargo build --frozen --release
  python -m build --no-isolation --wheel
}

package() {
  cd "$_pkgsrc/bindings/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
