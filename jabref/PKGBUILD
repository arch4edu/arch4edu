# Maintainer:  Michael Lass <bevan@bi-co.net>
# Contributor: Hector Mtz-Seara <hseara.at.gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Christian Storm <Christian.Storm@gmx.de>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=jabref
pkgver=5.1
pkgrel=2
pkgdesc="Graphical Java application for managing BibTeX and biblatex (.bib) databases"
arch=(any)
url="https://www.jabref.org/"
license=(MIT)
depends=('archlinux-java-run>=7' 'java-runtime>=13')
makedepends=('java-environment>=13')
options=(!strip !emptydirs)
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/JabRef/jabref/archive/v${pkgver}.tar.gz
        jabref.sh
        jabref.desktop
        0001-Fix-locating-jabref-in-jabrefHost.py.patch)
sha256sums=('c98ec9a7b4113945a27f9b49c9176bb6e5fa50c933562866dc0cc39dd18b7402'
            '0d5ca38d2c4a5c60b0778f36317794d2fb13f20b13d8473f69b41a6caebcb839'
            'e499b4af1fc45223fdafd801a4dd8a1c3c59384c71bc2e6985ab701da97df717'
            '1f01194665bfd91faaaa5a177b408d5af5f9dc3357795af4388eb61d2cad9f7c')

prepare() {
  cd ${pkgname}-${pkgver}

  # https://github.com/JabRef/jabref/pull/6963/
  patch -p1 < "${srcdir}"/0001-Fix-locating-jabref-in-jabrefHost.py.patch
}

build() {
  cd ${pkgname}-${pkgver}

  mkdir -p "${srcdir}"/gradle
  export GRADLE_USER_HOME=${srcdir}/gradle

  export JAVA_HOME=$(archlinux-java-run -a 13 -f jdk -j)
  echo "Using JDK from $JAVA_HOME to build JabRef."

  ./gradlew \
    --no-daemon \
    -PprojVersion="${pkgver}" \
    -PprojVersionInfo="${pkgver}--ArchLinux--${pkgrel}" \
    assemble
}

package() {
  install -dm755 "${pkgdir}"/usr/share/java/${pkgname}
  install -Dm755 jabref.sh "${pkgdir}"/usr/bin/JabRef
  install -Dm644 jabref.desktop "${pkgdir}"/usr/share/applications/${pkgname}.desktop

  cd ${pkgname}-${pkgver}
  install -Dm644 LICENSE.md "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE.md
  install -Dm644 src/main/resources/icons/jabref.svg "${pkgdir}"/usr/share/pixmaps/${pkgname}.svg

  # script to support browser extensions
  install -Dm755 buildres/linux/jabrefHost.py "${pkgdir}"/opt/jabref/lib/jabrefHost.py

  # lowercase alias (for convenience and required for browser extensions)
  ln -sf /usr/bin/JabRef "${pkgdir}"/usr/bin/jabref

  cd build
  cp -r resources "${pkgdir}"/usr/share/java/${pkgname}
  tar xf distributions/JabRef-${pkgver}.tar -C "${pkgdir}"/usr/share/java/${pkgname} JabRef-${pkgver}/lib --strip-components=1
  rm "${pkgdir}"/usr/share/java/${pkgname}/lib/*-mac.*
}
