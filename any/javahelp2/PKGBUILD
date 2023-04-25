# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Maintainer: alexisph@gmail.com
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=javahelp2
# manual versioning
pkgver=2.0.05.r90
pkgrel=7
pkgdesc="Java based help system"
url="https://javaee.github.io/javahelp/"
license=('custom' 'CDDL' 'GPL2')
arch=('any')
depends=('java-runtime')
makedepends=('ant' 'git')
source=("${pkgname}::git+https://github.com/javaee/javahelp.git#commit=3ca862d8626096770598a3a256886d205246f4a4"
        'java9-fix.patch')
sha512sums=('SKIP'
            '089c778aa937cd288aeae6cc87aaa3747925bf32871266d5f1d2e243b105fb70823a9f4903e4c0fcb60f4c73ea62c2a2927ef56315a826c454a5be9b72b425a6')

prepare () {
    cd "${pkgname}"
    patch -Np1 -i ../java9-fix.patch
}

build() {
    cd "${pkgname}/javahelp_nbproject"
    # http://openjdk.java.net/jeps/182
    # > In JDK 9 and going forward, javac will use a "one + three back" policy of supported source and target options.
    # NOTE: I just hope, that it'll compile right.
    local java_ver="$(javac -version | sed -e 's/^javac\s\+\([0-9]\+\.[0-9]\+\).*$/\1/g')"
    # accepted: 1.8, 17
    # not accepted: 17.0
    case $java_ver in
      1.*) ;;
      *) java_ver="${java_ver%.*}" ;;
    esac
    ant -Djavac.source="$java_ver" -Djavac.target="$java_ver" release
}

package() {
    cd "${pkgname}/javahelp_nbproject/dist/lib"
    install -dm755 "${pkgdir}/usr/share/java/javahelp"
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../bin
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../../lib
    # These are jars from tomcat5 and jdic-stub.jar
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"

    install -dm755 "${pkgdir}/usr/share/licenses"
    install -D -m644 -- "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
