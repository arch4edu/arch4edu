# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>

: ${CARGO_HOME=$SRCDEST/cargo-home}

_gitname="tokenizers"
_pkgname="python-$_gitname"
pkgname="$_pkgname"
pkgver=0.20.0
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
source=("$_pkgsrc"::"git+$url.git#tag=v$pkgver")
sha256sums=('SKIP')

_rust_env() {
  export CARGO_HOME
  export GIT_DIR='.'
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
}

prepare() {
  _rust_env

  cd "$_pkgsrc/bindings/python"

  # fix typo
  sed -E -e 's@defaut@default@' -i Cargo.toml

  cargo update
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  _rust_env

  cd "$_pkgsrc/bindings/python"
  cargo build --frozen --release
  python -m build --no-isolation --wheel
}

package() {
  cd "$_pkgsrc/bindings/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
