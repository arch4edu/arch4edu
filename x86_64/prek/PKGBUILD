# Maintainer: Jamison Lahman <jamison+aur@lahman.dev>
# Contributor:
# Source: https://github.com/jmelahman/pkgbuilds

pkgname=prek
pkgver=0.5.7
pkgrel=1
pkgdesc="⚡ Better 'pre-commit', re-engineered in Rust"
arch=('x86_64')
url='https://github.com/j178/prek'
license=('MIT')
depends=('gcc-libs')
makedepends=('git' 'rust' 'libxml2')
# TODO: https://github.com/jmelahman/PKGBUILDs/issues/119
# checkdepends=('cargo-nextest')
options=('!lto')
_commit='8569a4ac59a79212fe152f3c815505775301ec1d'
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

  # aws-lc-sys compiles jitterentropy with -O0, which makepkg's -O2 overrides.
  export CFLAGS="${CFLAGS/-O2/}"

  CARGO_PROFILE_RELEASE_STRIP=false \
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
  install -Dm644 <("$pkgdir/usr/bin/$pkgname" util generate-shell-completion bash) \
    "$pkgdir/usr/share/bash-completion/completions/$pkgname"
  install -Dm644 <("$pkgdir/usr/bin/$pkgname" util generate-shell-completion zsh) \
    "$pkgdir/usr/share/zsh/site-functions/_$pkgname"
  install -Dm644 <("$pkgdir/usr/bin/$pkgname" util generate-shell-completion fish) \
    "$pkgdir/usr/share/fish/vendor_completions.d/$pkgname.fish"
  install -Dm644 <("$pkgdir/usr/bin/$pkgname" util generate-shell-completion elvish) \
    "$pkgdir/usr/share/elvish/lib/$pkgname.elv"
  install -Dm644 <("$pkgdir/usr/bin/$pkgname" util generate-shell-completion nushell) \
    "$pkgdir/usr/share/nu/scripts/$pkgname.nu"

  # documentation
  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" README.md

  # license
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
