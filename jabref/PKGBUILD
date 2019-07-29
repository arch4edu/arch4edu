# Maintainer:  Michael Lass <bevan@bi-co.net>
# Contributor: Hector Mtz-Seara <hseara.at.gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Christian Storm <Christian.Storm@gmx.de>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=jabref
pkgver=4.3.1
pkgrel=3
pkgdesc="GUI frontend for BibTeX, written in Java"
arch=('any')
url="https://www.jabref.org/"
license=('MIT')
depends=('archlinux-java-run>=4' 'java8-openjfx'

         # Additional dependencies for the JavaFX UI, determined using
         # ldd /usr/lib/jvm/java-8-openjdk/jre/lib/amd64/libglass.so|awk '{print $3}'|xargs pacman -Qo|awk '{print $4}'|sort -u
         'atk'
         'bzip2'
         'cairo'
         'expat'
         'fontconfig'
         'freetype2'
         'fribidi'
         'gcc-libs'
         'gdk-pixbuf2'
         'glib2'
         'glibc'
         'graphite'
         'gtk2'
         'harfbuzz'
         'libdatrie'
         'libffi'
         'libpng'
         'libthai'
         'libutil-linux'
         'libx11'
         'libxau'
         'libxcb'
         'libxcomposite'
         'libxcursor'
         'libxdamage'
         'libxdmcp'
         'libxext'
         'libxfixes'
         'libxi'
         'libxinerama'
         'libxrandr'
         'libxrender'
         'libxtst'
         'pango'
         'pcre'
         'pixman'
         'zlib'
)
optdepends=(
   'gsettings-desktop-schemas: For web search support'
)
source=(https://github.com/JabRef/jabref/releases/download/v${pkgver}/JabRef-${pkgver}.jar
        https://raw.githubusercontent.com/JabRef/jabref/v${pkgver}/LICENSE.md
        jabref.sh
        jabref.desktop)
noextract=(JabRef-${pkgver}.jar)
sha256sums=('5b52ee079c430a59d99006a644bba3d191c21d1ec9e6bae5c87493ad74ccc395'
            'd0a8248eeaafc526f1137703fdc5aac1c8fae106f94c4bef56e3650e2c4c73a7'
            'c88d83bd310f5824ba8fbfad08c128b60aac3509a8302aabc0ac429d3a51738d'
            'a26845ba60ef2588c52d7d18259a977b146c777f935573bacdffcdcefa2b41b5')

prepare() {
  cd ${srcdir}
  bsdtar -xf JabRef-${pkgver}.jar icons/${pkgname}.svg
}

package() {
  cd ${srcdir}
  install -Dm755 JabRef-${pkgver}.jar ${pkgdir}/usr/share/java/${pkgname}/JabRef-${pkgver}.jar

  install -Dm755 ${pkgname}.sh ${pkgdir}/usr/bin/${pkgname}
  sed -i "s/VERSION/${pkgver}/" ${pkgdir}/usr/bin/${pkgname}

  install -Dm644 ${pkgname}.desktop ${pkgdir}/usr/share/applications/${pkgname}.desktop
  install -Dm644 icons/${pkgname}.svg ${pkgdir}/usr/share/pixmaps/${pkgname}.svg
  install -Dm644 LICENSE.md ${pkgdir}/usr/share/licenses/jabref/LICENSE.md
}
