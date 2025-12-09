# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>
# Contributor: Aliaksandr Mianzhynski <amenzhinsky@gmail.com>

pkgname="protoc-gen-go-grpc"
pkgver=1.6.0
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
  "${_pkgsrc}.tar.gz::${url}/archive/cmd/${pkgname}/v${pkgver}.tar.gz"
)
sha256sums=('6e269733f8728b6583ce7e8ca4b2aafec286f4ac4e878a8d75477787ba8c389b')

prepare() {
  export GOMODCACHE="${srcdir}/go-mod-cache"

  cd "${srcdir}/${_pkgsrc}"
  mkdir -p "build"

  cd "cmd/${pkgname}"
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
  install -vDm755 "build/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -vDm644 "README.md"  "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -vDm644 "AUTHORS"    "${pkgdir}/usr/share/doc/${pkgname}/AUTHORS"
  install -vDm644 "LICENSE"    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -vDm644 "NOTICE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/NOTICE"
}
