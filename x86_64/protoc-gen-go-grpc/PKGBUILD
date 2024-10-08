# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>
# Contributor: Aliaksandr Mianzhynski <amenzhinsky@gmail.com>

pkgname="protoc-gen-go-grpc"
pkgver=1.5.1
pkgrel=2
epoch=1
pkgdesc="gRPC bindings generator for Go language"
arch=('x86_64' 'aarch64' 'i686')
url="https://github.com/grpc/grpc-go"
license=('Apache-2.0')
depends=('glibc' 'protoc-gen-go')
makedepends=('go')
_pkgsrc="grpc-go-cmd-${pkgname}-v${pkgver}"
source=("${_pkgsrc}.tar.gz::${url}/archive/cmd/${pkgname}/v${pkgver}.tar.gz")
sha256sums=('54cb438abe590c9366e08251f811810fa004b1193154fe6e6a7d7c782a37332e')

prepare() {
  cd "${srcdir}/${_pkgsrc}"
  mkdir -p "build"
}

build() {
  cd "${srcdir}/${_pkgsrc}/cmd/${pkgname}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -o "${srcdir}/${_pkgsrc}/build/${pkgname}" .
}

# check() {
#   cd "${srcdir}/${_pkgsrc}"
#   ./"cmd/${pkgname}/${pkgname}_test.sh"
# }

package() {
  cd "${srcdir}/${_pkgsrc}"
  install -Dm755 "build/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "README.md"  "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -Dm644 "AUTHORS"    "${pkgdir}/usr/share/doc/${pkgname}/AUTHORS"
  install -Dm644 "LICENSE"    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 "NOTICE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/NOTICE"
}
