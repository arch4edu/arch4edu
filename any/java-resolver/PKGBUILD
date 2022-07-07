# Maintainer: Guillaume ALAUX <guillaume@archlinux.org>
_libname=xml-commons-resolver
pkgname=java-resolver
pkgver=1.2
pkgrel=4
pkgdesc="XML entity and URI resolver library"
arch=('any')
url="https://xml.apache.org/commons/components/resolver/"
license=('APACHE')
depends=('java-runtime-headless')
makedepends=('apache-ant')
checkdepends=('apache-ant')
source=(https://archive.apache.org/dist/xml/commons/${_libname}-${pkgver}.tar.gz{,.sig})
sha512sums=('0c91057da3198fc488c7b2c20afb029aa4441ad979159c378d532b02caa294d27e730ae2f9857062af5e3815a603a6110c5441dd3fe6b36c342a78beac3c8a6f'
            'SKIP')
validpgpkeys=('72F633CEAF1BEA18FAD0BB99FD49C07AC0926B13') # Michael Glavassevich <mrglavas@ca.ibm.com>

build() {
  cd ${_libname}-${pkgver}
  ant \
    -f resolver.xml \
    jar
}

check() {
  cd ${_libname}-${pkgver}
  ant \
    -f resolver.xml \
    check
}

package() {
  cd ${_libname}-${pkgver}/build
  install -Dm644 resolver.jar "${pkgdir}"/usr/share/java/resolver-${pkgver}.jar
  ln -s resolver-${pkgver}.jar "${pkgdir}"/usr/share/java/resolver.jar
}
