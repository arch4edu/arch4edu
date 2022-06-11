# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>

pkgname=fop-hyph
pkgver=2.2
pkgrel=1
pkgdesc="The hyphenation pattern files compiled for FOP"
arch=('any')
url="http://offo.sourceforge.net/"
license=('unknown')
depends=('java-runtime' 'fop>=1.0')
source=("https://sourceforge.net/projects/offo/files/offo-hyphenation/2.2/offo-hyphenation-compiled.zip")
md5sums=('5ec09cce6d8a09bc53a6441790021ecf')
sha1sums=('2ea3d35de0ed1fb451199d8e2e15ac57b11c6718')
sha256sums=('3b503122b488bd30f658e9757c3b3066dd7a59f56c3a9bbb3eaae2d23b7d883f')
sha512sums=('04bc87533d8462c5473fa7cd480fd142f9f32447c34e55fac28e9811d3b63e57ff11ba03160d592310dff44999a7f8d595d02a377eaa8d9df634381ef0ea66c7')

package() {
	cd "${srcdir}/offo-hyphenation-compiled/"
	install -Dm644 "${pkgname}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
