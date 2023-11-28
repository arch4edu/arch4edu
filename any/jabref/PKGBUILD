# Maintainer:  Michael Lass <bevan@bi-co.net>
# Contributor: Hector Mtz-Seara <hseara.at.gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Christian Storm <Christian.Storm@gmx.de>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

_abbrv=cf71cb48dbd78b2d85856e689e2834f14b91fdbc
_locales=3fd551ca87ea464f89b1509e4987015691f3132b
_styles=010b77c19b0928db4cc046258d6797a937e0f460

pkgname=jabref
pkgver=5.11
pkgrel=3
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
sha256sums=('d09666f240a9ba8a4bb1759b44a676e723f7b48477e57ef0189349ad4489b822'
            '9345f022dca8d341928adecd0e82be00b205371da71ec0109d86a20c4b9b25c2'
            'a2533c5dfc43de52e8acedd656c5af257c7da4baf8dda844b81c7f98d4e018e8'
            'c5629699d899cc02d09062c76f8c8e6a0d2f44c99ef402b6671b0aa46b942372'
            '6a377ca631aab1d6a9bba927714e0571a19fbf4c1bb6b798921ca254e3e0588f'
            'b0e3ed5cde4072a2d10de887b50217c03bbe30a1ea9b39bea1255ea80db15b77')

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
  install -Dm644 LICENSE.md "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE.md
  install -Dm644 src/main/resources/icons/jabref.svg "${pkgdir}"/usr/share/pixmaps/${pkgname}.svg

  # script to support browser extensions
  install -Dm755 buildres/linux/jabrefHost.py "${pkgdir}"/opt/jabref/lib/jabrefHost.py

  # lowercase alias (for convenience and required for browser extensions)
  ln -sf /usr/bin/JabRef "${pkgdir}"/usr/bin/jabref

  cd build
  cp -r resources "${pkgdir}"/usr/share/java/${pkgname}
  tar xf distributions/JabRef-${pkgver}.tar -C "${pkgdir}"/usr/share/java/${pkgname} JabRef-${pkgver}/lib --strip-components=1
}
