# Maintainer: Darkfish Tech <arch at darkfish dot com dot au>
# Contributor: Rémi Saurel <patadune@gmail.com>
# Contributor: Matthew Longley <randomticktock@gmail.com>

pkgname=javacc
pkgver=7.0.13
pkgrel=1
pkgdesc="Parser/scanner generator for Java"
arch=('any')
url="http://javacc.org/"
_url="https://github.com/javacc/javacc"
license=('BSD')
depends=('java-environment' )
makedepends=('apache-ant')
source=("${pkgname}-${pkgver}.tar.gz::${_url}/archive/${pkgname}-${pkgver}.tar.gz")
_pkgsrcdir=${pkgname}-${pkgname}-${pkgver}
sha256sums=('d1bfebb4ca9261c5c3b16b00280b3278a41b193ca8503f2987f72de453bf99c6')

build() {
    cd $_pkgsrcdir
    ant
}

package() {
    cd $_pkgsrcdir

    install -D LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    mkdir -m755 -p "$pkgdir/usr/share/java/$pkgname/bin" "$pkgdir/usr/bin"

    # install examples
    cp -R "examples/" "$pkgdir/usr/share/java/$pkgname/examples"

    # install documentation
    cp -R "docs/" "$pkgdir/usr/share/java/$pkgname/docs"

    # install jar
    install -m755 -D "target/$pkgname-$pkgver.jar" "$pkgdir/usr/share/java/$pkgname/bin/lib/$pkgname.jar"
    ln -s /usr/share/java/$pkgname/bin/lib/javacc.jar $pkgdir/usr/share/java/javacc.jar

    # generate scripts to allow direct execution
    for i in jjtree jjdoc javacc; do
        printf "#\!bin/sh\nJAR=\"/usr/share/java/$pkgname/bin/lib/javacc.jar\"\n\njava -classpath \"\$JAR\" $i \"\$@\"\n" > "$pkgdir/usr/share/java/$pkgname/bin/$i";
        ln -s "/usr/share/java/$pkgname/bin/$i" "$pkgdir/usr/bin/$i";
    done

    # Set permissions
    chmod -R 755 "$pkgdir/usr/share/java/$pkgname/bin" "$pkgdir/usr/bin"
}
