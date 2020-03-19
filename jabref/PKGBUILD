# Maintainer:  Michael Lass <bevan@bi-co.net>
# Contributor: Hector Mtz-Seara <hseara.at.gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Christian Storm <Christian.Storm@gmx.de>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=jabref
pkgver=5.0
pkgrel=1
pkgdesc="Graphical Java application for managing BibTeX and biblatex (.bib) databases"
arch=(x86_64)
url="https://www.jabref.org/"
license=(MIT)
depends=(alsa-lib freetype2 libnet libxrender libxtst python)
source=(https://github.com/JabRef/jabref/releases/download/v${pkgver}/JabRef-${pkgver}-portable_linux.tar.gz
        https://raw.githubusercontent.com/JabRef/jabref/v${pkgver}/LICENSE.md
        https://raw.githubusercontent.com/JabRef/jabref/v${pkgver}/src/main/resources/icons/jabref.svg
        jabref.desktop)
sha256sums=('2231df4a429e819f795483419bb40242ad1f0dc2a7893e546e62649b6a275e6c'
            '057113b2e1e3eaeffdbbfbc57febca6e02c53cb63b14ffc9e1fbacf6ddc17638'
            '84408ddc8c6e41e4367f3b6cd171909fb1cf7ac808495f3a8033b64a2ff4c40b'
            'e499b4af1fc45223fdafd801a4dd8a1c3c59384c71bc2e6985ab701da97df717')

# Preparation for building from source. Currently, the jlink step fails with the following message:
# Process 'command '/usr/lib/jvm/java-13-openjdk/bin/jlink'' finished with non-zero exit value 1
#build() {
#  cd ...
#
#  export JAVA_HOME=/usr/lib/jvm/java-13-openjdk/
#
#  ./gradlew --no-daemon assemble
#  ./gradlew --no-daemon jlink
#}

package() {
  install -dm755 "${pkgdir}/opt/jabref" "${pkgdir}/usr/bin"

  cp -r "${srcdir}"/JabRef/{bin,lib} "${pkgdir}"/opt/${pkgname}
  ln -sf /opt/${pkgname}/bin/JabRef "${pkgdir}"/usr/bin/JabRef

  install -Dm644 "${srcdir}"/${pkgname}.desktop "${pkgdir}"/usr/share/applications/${pkgname}.desktop
  install -Dm644 "${srcdir}"/${pkgname}.svg "${pkgdir}"/usr/share/pixmaps/${pkgname}.svg
  install -Dm644 "${srcdir}"/LICENSE.md "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE.md
}
