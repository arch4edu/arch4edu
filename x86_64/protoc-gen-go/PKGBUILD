# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>
# Contributor: Aliaksandr Mianzhynski <amenzhinsky@gmail.com>

pkgname="protoc-gen-go"
pkgver=1.36.1
pkgrel=1
pkgdesc="Go support for Google's protocol buffers"
arch=('x86_64' 'aarch64' 'i686')
url="https://github.com/protocolbuffers/protobuf-go"
license=('BSD-3-Clause')
depends=('glibc')
makedepends=('go')
optdepends=('protobuf: protoc generator')
_pkgsrc="protobuf-go-${pkgver}"
source=("${_pkgsrc}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('28a6c9eb62a06e65e866bcdb2005c63f9ee7b57c271617ed761f309c7ece17fb')

prepare() {
  cd "${srcdir}/${_pkgsrc}"
  mkdir -p "build"
}

build() {
  cd "${srcdir}/${_pkgsrc}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -o "build/${pkgname}" ./"cmd/${pkgname}"
}

check() {
  cd "${srcdir}/${_pkgsrc}"
  go test ./...
}

package() {
  cd "${srcdir}/${_pkgsrc}"
  install -vDm755 "build/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -vDm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -vDm644 "PATENTS"   "${pkgdir}/usr/share/doc/${pkgname}/PATENTS"
  install -vDm644 "LICENSE"   "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
