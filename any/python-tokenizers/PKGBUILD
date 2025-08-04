# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>

: ${CARGO_HOME:=$SRCDEST/cargo-home}
: ${CARGO_TARGET_DIR:=target}
: ${RUSTUP_TOOLCHAIN:=stable}

_module="tokenizers"
_pkgname="python-$_module"
pkgname="$_pkgname"
pkgver=0.21.4
pkgrel=1
pkgdesc='Fast State-of-the-Art Tokenizers optimized for Research and Production'
url="https://github.com/huggingface/tokenizers"
license=('Apache-2.0')
arch=('i686' 'x86_64')

depends=('python')
makedepends=(
  'clang'
  'rust-bindgen'
  'python-build'
  'python-installer'
  'python-maturin'
  'python-setuptools-rust'
  'python-wheel'
)
checkdepends=(
  'python-datasets'
  #└─ 'python-huggingface-hub' # AUR
  #└─ 'python-multiprocess' # AUR
  'python-numpy'
  'python-pyarrow'
  'python-pytest'
  'python-requests'
  'python-setuptools-rust'
)

options=('!lto')

_pkgsrc="$_module-$pkgver"
_pkgext="tar.gz"
source=(
  "$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext"
  "norvig-big.txt"::"https://norvig.com/big.txt"
  "roberta.json"::"https://huggingface.co/roberta-large/raw/main/tokenizer.json"
)
sha256sums=('980f141601d9b6cc2d988657fd87e93c9d8599e3da7b4f5f77e3390a140edba3'
            'fa066c7d40f0f201ac4144e652aa62430e58a6b3805ec70650f678da5804e87b'
            '847bbeab6174d66a88898f729d52fa8d355fafe1bea101cf960dd404581df70e')

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
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
)

build() (
  _rust_env
  cd "$_pkgsrc/bindings/python"
  cargo build --frozen --release
  python -m build --no-isolation --wheel
)

check() {
  cd "$_pkgsrc/bindings/python"

  # data
  install -Dm644 "$srcdir/roberta.json" "data/roberta.json"
  install -Dm644 "$srcdir/norvig-big.txt" "data/big.txt"
  head -100 data/big.txt > data/small.txt

  # test in venv
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -s -v tests || :

  cargo test --no-default-features || :
}

package() {
  cd "$_pkgsrc"
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  cd "bindings/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
