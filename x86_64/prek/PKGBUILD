# Maintainer: Jamison Lahman <jamison+aur@lahman.dev>
# Contributor:

pkgname=prek
pkgver=0.3.6
pkgrel=1
pkgdesc="⚡ Better 'pre-commit', re-engineered in Rust"
arch=('x86_64')
url='https://github.com/j178/prek'
license=('MIT')
depends=('gcc-libs')
makedepends=('git' 'rust' 'libxml2')
checkdepends=('cargo-nextest')
options=('!lto')
_commit='dd53c3d715e3a94dc7ecc947891b9887371e21fe'
source=("$pkgname::git+$url.git#commit=$_commit")
md5sums=('SKIP')

pkgver() {
  cd "$pkgname" || exit

  git describe --tags | sed 's/^v//'
}

prepare() {
  cd "$pkgname" || exit

  cargo fetch --locked
}

build() {
  cd "$pkgname" || exit

  cargo build --frozen --release --target-dir target
}

# TODO: https://github.com/jmelahman/PKGBUILDs/issues/119
# check() {
#   cd "$pkgname" || exit
#
#   cargo nextest run \
#     --locked \
#     --workspace
# }

package() {
  cd "$pkgname" || exit

  # binary
  install -Dm755 -t "$pkgdir/usr/bin" "target/release/$pkgname"

  # shell completion
  install -Dm644 <(env PATH="$pkgdir/usr/bin" COMPLETE=bash "$pkgname") \
    "$pkgdir/usr/share/bash-completion/completions/$pkgname"
  install -Dm644 <(env PATH="$pkgdir/usr/bin" COMPLETE=zsh "$pkgname") \
    "$pkgdir/usr/share/zsh/site-functions/_$pkgname"
  install -Dm644 <(env PATH="$pkgdir/usr/bin" COMPLETE=fish "$pkgname") \
    "$pkgdir/usr/share/fish/vendor_completions.d/$pkgname.fish"

  # documentation
  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" README.md

  # license
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
