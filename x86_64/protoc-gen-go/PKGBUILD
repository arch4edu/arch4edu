# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>
# Contributor: Aliaksandr Mianzhynski <amenzhinsky@gmail.com>

pkgname="protoc-gen-go"
pkgver=1.36.11
pkgrel=1
pkgdesc="Go support for Google's protocol buffers"
arch=(
  'aarch64'
  'i686'
  'x86_64'
)
url="https://github.com/protocolbuffers/protobuf-go"
license=(
  'BSD-3-Clause'
)
depends=(
  'glibc'
  'protobuf'
)
makedepends=(
  'go'
)
provides=(
  "protobuf-go=${pkgver}"
)
conflicts=(
  'protobuf-go'
)
replaces=(
  'protobuf-go'
)
_pkgsrc="${url##*/}-${pkgver}"
source=(
  "${_pkgsrc}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
)
sha256sums=('517b935001f3d43640489cd1aab531a3ed5927fb34379fa6cb1c1a514e9cb8e8')

prepare() {
  export GOMODCACHE="${srcdir}/go-mod-cache"

  cd "${srcdir}/${_pkgsrc}"
  go mod download -modcacherw -x
  go mod verify

  mkdir -p "build"
}

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOCACHE="${srcdir}/go-cache"
  export GOMODCACHE="${srcdir}/go-mod-cache"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  cd "${srcdir}/${_pkgsrc}"
  go build -v -o "build/${pkgname}" ./"cmd/${pkgname}"
}

check() {
  cd "${srcdir}/${_pkgsrc}"
  go test ./...
}

package() {
  cd "${srcdir}/${_pkgsrc}"
  install -vDm755 "build/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -vDm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -vDm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
