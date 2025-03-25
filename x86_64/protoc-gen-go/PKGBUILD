# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>
# Contributor: Aliaksandr Mianzhynski <amenzhinsky@gmail.com>

pkgname="protoc-gen-go"
pkgver=1.36.6
pkgrel=1
pkgdesc="Go support for Google's protocol buffers"
arch=('aarch64' 'i686' 'x86_64')
url="https://github.com/protocolbuffers/protobuf-go"
license=('BSD-3-Clause')
depends=('glibc' 'protobuf')
makedepends=('go')
provides=('protobuf-go')
conflicts=('protobuf-go')
replaces=('protobuf-go')
_pkgsrc="protobuf-go-${pkgver}"
source=("${_pkgsrc}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('afa2b0e8f86d6da9d09c51ab4270d93c2888327220316982be9db345f523a6a1')

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
