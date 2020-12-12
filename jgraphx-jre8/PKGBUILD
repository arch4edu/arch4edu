# Maintainer: Anton Kudelin <kudelin at protonmail dot com>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname=jgraphx-jre8
_pkgname=jgraphx
pkgver=3.9.10
pkgrel=1
pkgdesc="Open source graph drawing component."
arch=('any')
url="https://github.com/jgraph/jgraphx"
license=('BSD')
depends=('java-runtime=8')
makedepends=('jdk8-openjdk' 'maven')
provides=('jgraphx')
conflicts=('jgraphx')
source=("$pkgname-v$pkgver.tar.gz::https://github.com/jgraph/jgraphx/archive/v$pkgver.tar.gz")
sha256sums=('76782db7856f53ddf6979a61f523e0485c91d5039a4b197921c988a1c0bbf02f')

prepare() {
  sed -i 's/1.5/1.7/g' "$srcdir/$_pkgname-$pkgver/pom.xml"
}

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  mvn -DskipTests=true clean package
}

check() {
  cd "$srcdir/$_pkgname-$pkgver"
  mvn test
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  install -Dm644 license.txt "$pkgdir/usr/share/licenses/$_pkgname/license.txt"
  install -Dm644 lib/jgraphx.jar "$pkgdir/usr/share/java/$_pkgname/$_pkgname.jar"
}
