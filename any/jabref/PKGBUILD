# Maintainer:  Michael Lass <bevan@bi-co.net>
# Contributor: Hector Mtz-Seara <hseara.at.gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Christian Storm <Christian.Storm@gmx.de>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

_abbrv=b69f1d607a57488276f3402bbf610d9129e7f6fb
_locales=e631a52dcea396be20d031b6456e91dba7772224
_styles=b2be5aeeee7f00fd2032ac1daad995bbe95398cf

pkgname=jabref
pkgver=5.15
pkgrel=2
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
        jabref.desktop
        https://patch-diff.githubusercontent.com/raw/JabRef/jabref/pull/11517.patch)
sha256sums=('2bf75d7f96aa1f5c74b675e3e0b4dda703027b3c3d8ede0616dd2218f5a74259'
            '902c30710bdd46bcafa954b174dc3e080d9902d8dc43f40602c357155e894312'
            '5b1a86d2d9eb2ffd40e62d72d06ec9fce9b1b048961529f1e596dfedd6322b17'
            '667513b7df0763a2c971f9c0017f88e6e4c7d5b44328516c53c5bfdbe8adb167'
            'f466d2cbf88d4d37c0e39cb3aa3fb5bb2f0ac486d617591b2b47817c762317b0'
            'aebafd8955b35d440c233f6e9d7cfa68bec17f58418320920b52c334e965db3a'
            'ecf10a20e009f0801cd885f7c32842d14320957446d07d3f69300a85a1dfb8d0')

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

  patch -p1 < "${srcdir}"/11517.patch
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
