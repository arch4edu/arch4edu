# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=javahelp2
pkgver=2.0.05.r89
pkgrel=1
pkgdesc="Java based help system"
arch=('any')
url="https://javahelp.java.net/"
#"https://java.net/projects/javahelp/"
license=(GPL2)
makedepends=('apache-ant' 'subversion')
depends=('java-runtime')
source=("${pkgname}::svn+https://svn.java.net/svn/javahelp~svn")
sha256sums=('SKIP')

pkgver() {
    cd "$srcdir/${pkgname}"
    local ver="$(svnversion | tr -d '[:alpha:]')"
    printf "2.0.05.r%s" "$ver"
}

build(){
    cd "${srcdir}/${pkgname}/trunk/javahelp_nbproject"
    ant release
}

package() {
    cd "${srcdir}/${pkgname}/trunk/javahelp_nbproject/dist/lib"
    install -dm755 "${pkgdir}/usr/share/java/javahelp"
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../bin
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../../lib
    # These are jars from tomcat5 and jdic-stub.jar
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
}
