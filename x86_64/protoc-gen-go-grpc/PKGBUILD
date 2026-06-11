# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>
# Contributor: Aliaksandr Mianzhynski <amenzhinsky@gmail.com>

pkgname="protoc-gen-go-grpc"
pkgver=1.6.2
pkgrel=1
epoch=1
pkgdesc="gRPC bindings generator for Go language"
arch=(
  'aarch64'
  'i686'
  'x86_64'
)
url="https://github.com/grpc/grpc-go"
license=(
  'Apache-2.0'
)
depends=(
  'glibc'
  'protoc-gen-go'
)
makedepends=(
  'go'
)
_pkgsrc="${url##*/}-cmd-${pkgname}-v${pkgver}"
source=(
  "${url}/archive/refs/tags/cmd/${pkgname}/v${pkgver}/${_pkgsrc}.tar.gz"
)
sha256sums=('a5f284c76292c8f4460aa57d0dfe81ee44f4670082a575f43324523ec6ef15e7')

prepare() {
  export GOMODCACHE="${srcdir}/go-mod-cache"

  cd "${srcdir}/${_pkgsrc}/cmd/${pkgname}"
  go mod download -modcacherw -x
  go mod verify
}

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOCACHE="${srcdir}/go-cache"
  export GOMODCACHE="${srcdir}/go-mod-cache"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  cd "${srcdir}/${_pkgsrc}/cmd/${pkgname}"
  go build -v -o "${srcdir}/${_pkgsrc}/build/${pkgname}" .
}

# check() {
#   cd "${srcdir}/${_pkgsrc}"
#   ./"cmd/${pkgname}/${pkgname}_test.sh"
# }

package() {
  cd "${srcdir}/${_pkgsrc}"
  install -vDm755 "build/${pkgname}" -t "${pkgdir}/usr/bin"
  install -vDm644 "README.md" -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -vDm644 "LICENSE" "NOTICE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
