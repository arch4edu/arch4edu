# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: Kien Dang <mail at kien dot ai>
# Contributor: Julie Shapiro <jshapiro at nvidia dot com>
pkgname=nvidia-container-toolkit
pkgver=1.14.5
pkgrel=1
pkgdesc="NVIDIA container runtime toolkit"
arch=('x86_64')
url="https://github.com/NVIDIA/nvidia-container-toolkit"
license=('Apache-2.0')
depends=("libnvidia-container-tools=$pkgver")
makedepends=('git' 'go')
provides=('nvidia-container-runtime')
conflicts=('nvidia-container-runtime' 'nvidia-container-runtime-hook')
replaces=('nvidia-container-runtime-hook')
backup=('etc/nvidia-container-runtime/config.toml')
options=('!makeflags' '!lto')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
#        'go-nvml-79.patch'  # only for Go 1.21.X
        )
sha256sums=('6c6ae02b46a56e3a8b23ab3b0d0f46ad908d0771e6db4b3f6b5cfa64050ce83c')

prepare() {
  cd "$pkgname-$pkgver"
  mkdir -p build

  # gen/nvml: add --export-dynamic linker flag
  # https://github.com/NVIDIA/go-nvml/issues/36
#  cd vendor/github.com/NVIDIA/go-nvml
#  git apply "$srcdir/go-nvml-79.patch"
}

build() {
  cd "$pkgname-$pkgver"
  export GOPATH="$srcdir/gopath"
  export GOTOOLCHAIN=go1.20.8
  go build -v \
    -ldflags "-extldflags=-Wl,-z,lazy -s -w -X github.com/NVIDIA/$pkgname/internal/info.version=$pkgver" \
    -o build ./...

  # Clean module cache for makepkg -C
  go clean -modcache
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 build/nvidia-{ctk,container-runtime,container-runtime{.cdi,.legacy,-hook}} -t \
    "$pkgdir/usr/bin/"
  ln -s nvidia-container-runtime-hook "$pkgdir/usr/bin/nvidia-container-toolkit"

  # Generate the default config
  "$pkgdir"/usr/bin/nvidia-ctk --quiet config --config-file="$pkgdir"/etc/nvidia-container-runtime/config.toml --in-place
}
