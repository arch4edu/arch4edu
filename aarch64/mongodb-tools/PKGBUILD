# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Maintainer: Christoph Bayer <chrbayer@criby.de>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Fredy García <frealgagu at gmail dot com>

pkgname=mongodb-tools
pkgver=4.2.18_rc0
_pkgver=4.2.18-rc0
pkgrel=1
epoch=1
pkgdesc="The MongoDB tools provide import, export, and diagnostic capabilities."
arch=('x86_64')
url="https://github.com/mongodb/mongo-tools"
license=('Apache')
depends=('libpcap')
makedepends=('go-pie')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/mongodb/mongo-tools/archive/refs/tags/r${_pkgver}.tar.gz")
sha256sums=('2a7380f582419396888e95c01e35262a37e6ad36eb149788adb844c005ad8d35')

_tools=('bsondump' 'mongostat' 'mongofiles' 'mongoexport' 'mongoimport' 'mongorestore' 'mongodump' 'mongotop' 'mongoreplay')

prepare() {
  cd "${srcdir}"
  install -d build/src/github.com/mongodb/bin
  mv "mongo-tools-r${_pkgver}" build/src/github.com/mongodb/mongo-tools
}

build() {
  cd "${srcdir}/build/src/github.com/mongodb/mongo-tools"
  ./set_goenv.sh
  export GOPATH="$srcdir/build"
  export GO111MODULE=auto

  for tool in "${_tools[@]}"; do
    echo "Building ${tool}..."
    go build -o "bin/${tool}" -tags "ssl sasl" "${tool}/main/${tool}.go"
  done
}

package() {
  cd "${srcdir}/build/src/github.com/mongodb/mongo-tools"
  for tool in "${_tools[@]}"; do
    install -Dm755 "bin/${tool}" "${pkgdir}/usr/bin/${tool}"
  done
}
