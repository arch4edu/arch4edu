# Maintainer: Rémi Saurel <patadune@gmail.com>
# Contributor: Matthew Longley <randomticktock@gmail.com>

pkgname=javacc
pkgver=6.1.3
pkgrel=2
pkgdesc="Parser/scanner generator for Java"
arch=('any')
url="http://javacc.java.net/"
license=('BSD')
depends=('java-environment' 'apache-ant')
makedepends=('subversion')
_svn_tag="release_6_1_3"
source=("svn+https://svn.java.net/svn/javacc~svn/tags/$_svn_tag")
sha256sums=('SKIP')

build() {
    cd "$srcdir/$_svn_tag"
    ant
}

package() {
    cd "$srcdir/$_svn_tag"

    install -D LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    mkdir -m755 -p "$pkgdir/usr/share/java/$pkgname/bin" "$pkgdir/usr/bin"

    # install examples
    cp -R "examples/" "$pkgdir/usr/share/java/$pkgname/examples"

    # install documentation
    cp -R "www/doc/" "$pkgdir/usr/share/java/$pkgname/doc"

    # install jar
    install -m755 -D "target/$pkgname-$pkgver.jar" "$pkgdir/usr/share/java/$pkgname/bin/lib/$pkgname.jar"

    # generate scripts to allow direct execution
    for i in jjtree jjdoc javacc; do
	printf "#\!bin/sh\nJAR=\"/usr/share/java/$pkgname/bin/lib/javacc.jar\"\n\njava -classpath \"\$JAR\" $i \"\$@\"\n" > "$pkgdir/usr/share/java/$pkgname/bin/$i";
	ln -s "/usr/share/java/$pkgname/bin/$i" "$pkgdir/usr/bin/$i";
    done

    # Set permissions
    chmod -R 755 "$pkgdir/usr/share/java/$pkgname/bin" "$pkgdir/usr/bin"
}
