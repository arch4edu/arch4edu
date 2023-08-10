# Contributor: Doug Newgard <dnewgard at outlook dot com>
# Contributor: James P. Harvey <jamespharvey20 at gmail dot com>
# Contributor: Christoph Bayer <chrbayer@criby.de>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Fredy García <frealgagu at gmail dot com>

pkgname=mongodb-tools
pkgver=100.7.5
pkgrel=1
epoch=1
pkgdesc="Import, export, and diagnostic tools for MongoDB"
arch=('x86_64')
url="https://github.com/mongodb/mongo-tools"
license=('Apache')
depends=('glibc' 'krb5')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mongodb/mongo-tools/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('9cda0fc218e779541de94e069f784daae346f8f587fe0cbad126df073c5c154b')

prepare() {
# Patch version check for release
  sed -e "s/runCmd.*get-version.*/\"$pkgver\", *new(error)/" \
      -e "s/git\.SHA1(ctx)/\"release\", *new(error)/" \
      -e "/github.com\/craiggwilson\/goke\/pkg\/git/d" \
      -i mongo-tools-$pkgver/buildscript/build.go
}

build() {
  cd mongo-tools-$pkgver

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  go run build.go build
}

package() {
  install -Dm755 mongo-tools-$pkgver/bin/* -t "$pkgdir/usr/bin/"
}
