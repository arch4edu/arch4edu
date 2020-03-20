# Maintainer:  Michael Lass <bevan@bi-co.net>
# Contributor: Hector Mtz-Seara <hseara.at.gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Christian Storm <Christian.Storm@gmx.de>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=jabref
pkgver=5.0
pkgrel=2
pkgdesc="Graphical Java application for managing BibTeX and biblatex (.bib) databases"
arch=(any)
url="https://www.jabref.org/"
license=(MIT)
depends=(bash jre13-openjdk)
makedepends=(jdk13-openjdk)
options=(!strip !emptydirs)
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/JabRef/jabref/archive/v${pkgver}.tar.gz
        jabref.sh
        jabref.desktop)
sha256sums=('52ac917dd96f20a05b4beb7ea4c52edcf8c6170bd49b36178f599d48ecd3a822'
            '51379fbce194379d6c6b66cf9404361d42b916364fc1b5915553fe4b03d5f0e5'
            'e499b4af1fc45223fdafd801a4dd8a1c3c59384c71bc2e6985ab701da97df717')

build() {
  cd ${pkgname}-${pkgver}

  export JAVA_HOME=/usr/lib/jvm/java-13-openjdk/

  # Avoid storing maven packages in the user's home (comment out to cache resources)
  sed -i '/^\s*mavenLocal()\s*$/d' build.gradle

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

  cd build
  cp -r resources "${pkgdir}"/usr/share/java/${pkgname}
  tar xf distributions/JabRef-${pkgver}.tar -C "${pkgdir}"/usr/share/java/${pkgname} JabRef-${pkgver}/lib --strip-components=1
  rm "${pkgdir}"/usr/share/java/${pkgname}/lib/*-mac.*
}
