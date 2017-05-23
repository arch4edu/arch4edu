# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=javahelp2
pkgver=2.0.05.r89
pkgrel=2
pkgdesc="Java based help system"
arch=('any')
# Old URLs
#"https://javahelp.java.net/"
#"https://java.net/projects/javahelp/"
# New URL
url="https://javaee.github.io/javahelp/"
license=('custom' 'CDDL' 'GPL2')
#makedepends=('apache-ant' 'git')
makedepends=('apache-ant')
depends=('java-runtime')
# Old source
#source=("${pkgname}::svn+https://svn.java.net/svn/javahelp~svn")
# New source
# currently lacks everything
#source=("${pkgname}::git+https://github.com/javaee/javahelp.git")
source=("${pkgname}-${pkgver}.tar.xz::https://www.dropbox.com/s/ywczc6bdrh7h2hj/javahelp2.tar.xz?dl=1")
sha256sums=('9047c842ff7963b2cc3116d59c796450609597a09c722a5fa918e14c82912e7b')

build(){
    cd "${srcdir}/${pkgname}/javahelp_nbproject"
    ant release
}

package() {
    cd "${srcdir}/${pkgname}/javahelp_nbproject/dist/lib"
    install -dm755 "${pkgdir}/usr/share/java/javahelp"
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../bin
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../../lib
    # These are jars from tomcat5 and jdic-stub.jar
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
}
