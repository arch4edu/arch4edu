# Maintainer:  Michael Lass <bevan@bi-co.net>
# Contributor: Hector Mtz-Seara <hseara.at.gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Christian Storm <Christian.Storm@gmx.de>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

_abbrv=8fbad5a1285926b177803087b35b0eb6b0fd0142
_locales=cf4b49404fc15cf9a37372e4707ce710b0935ccc
_styles=fe9db541ea06c31c8ff91c7c989fc8d4ef987b92

pkgname=jabref
pkgver=5.13
pkgrel=1
pkgdesc="Graphical Java application for managing BibTeX and biblatex (.bib) databases"
arch=(any)
url="https://www.jabref.org/"
license=(MIT)
depends=('archlinux-java-run>=10' 'java-environment=21')
makedepends=('gradle>=8')
optdepends=('python: browser extension')
options=(!strip !emptydirs)
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/JabRef/jabref/archive/v${pkgver}.tar.gz
        abbrv.jabref.org-${_abbrv}.tar.gz::https://github.com/JabRef/abbrv.jabref.org/archive/${_abbrv}.tar.gz
        locales-${_locales}.tar.gz::https://github.com/citation-style-language/locales/archive/${_locales}.tar.gz
        styles-${_styles}.tar.gz::https://github.com/citation-style-language/styles/archive/${_styles}.tar.gz
        jabref.sh
        jabref.desktop)
sha256sums=('35b4415acb3b8892d3d4e86d8a6f46095ba5e0f285f2daa53a19abaca0a76bca'
            '7be22f96eaea7a901f17830f7fccb72f46191b2fa9ec97e85ba9eabb9c4e7099'
            'ebb01bff2fdb76f88800badce3499adbae4d9cdf6d6cefc20cc4278df44a3829'
            'c593638e5be4cf93c0dd17d1c22865ecc8d91e31e8a1ab218e96204b44b00206'
            'f466d2cbf88d4d37c0e39cb3aa3fb5bb2f0ac486d617591b2b47817c762317b0'
            'aebafd8955b35d440c233f6e9d7cfa68bec17f58418320920b52c334e965db3a')

# Note on supported Java versions:
# The file build.gradle contains the version of Java that is required and tested.
# Newer versions typically work as well. However, if using the supplied gradle
# wrapper, it may use an old version of gradle that limits support for newer Java
# versions.

prepare() {
  cd ${pkgname}-${pkgver}

  cp -a "${srcdir}"/abbrv.jabref.org-${_abbrv}/* buildres/abbrv.jabref.org/
  cp -a "${srcdir}"/locales-${_locales}/* src/main/resources/csl-locales/
  cp -a "${srcdir}"/styles-${_styles}/* src/main/resources/csl-styles/
}

build() {
  cd ${pkgname}-${pkgver}

  mkdir -p "${srcdir}"/gradle
  export GRADLE_USER_HOME=${srcdir}/gradle

  export JAVA_HOME=$(archlinux-java-run -a 21 -b 21 -f jdk -j)
  echo "Using JDK from $JAVA_HOME to build JabRef."

  #./gradlew \
  /usr/bin/gradle \
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
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
  install -Dm644 src/main/resources/icons/jabref.svg "${pkgdir}"/usr/share/pixmaps/${pkgname}.svg

  # script to support browser extensions
  install -Dm755 buildres/linux/jabrefHost.py "${pkgdir}"/opt/jabref/lib/jabrefHost.py

  # lowercase alias (for convenience and required for browser extensions)
  ln -sf /usr/bin/JabRef "${pkgdir}"/usr/bin/jabref

  cd build
  cp -r resources "${pkgdir}"/usr/share/java/${pkgname}
  tar xf distributions/JabRef-${pkgver}.tar -C "${pkgdir}"/usr/share/java/${pkgname} JabRef-${pkgver}/lib --strip-components=1
}
