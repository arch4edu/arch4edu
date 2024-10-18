# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>

: ${CARGO_HOME:=$SRCDEST/cargo-home}
: ${CARGO_TARGET_DIR:=target}
: ${RUSTUP_TOOLCHAIN:=stable}

_module="tokenizers"
_pkgname="python-$_module"
pkgname="$_pkgname"
pkgver=0.20.1
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
  'python-build'
  'python-installer'
  'python-maturin'
  'python-setuptools-rust'
  'python-wheel'
)

options=('!lto')

_pkgsrc="$_module-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext")
sha256sums=('1ac66047e780dae3feb9c6f85dbb95e8861e99d86590969383f871589a3f1ef0')

_rust_env() {
  export CARGO_HOME CARGO_TARGET_DIR RUSTUP_TOOLCHAIN
  export GIT_DIR='.'
}

prepare() (
  _rust_env
  cd "$_pkgsrc/bindings/python"

  # fix typo
  sed -E -e 's@defaut@default@' -i Cargo.toml

  cargo update
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
)

build() (
  _rust_env
  cd "$_pkgsrc/bindings/python"
  cargo build --frozen --release
  python -m build --no-isolation --wheel
)

package() {
  cd "$_pkgsrc/bindings/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
