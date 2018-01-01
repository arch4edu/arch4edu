# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: kalenz <https://aur.archlinux.org/account/kalenz>
# Contributor: Vojtech Horky <vojta . horky at-symbol seznam . cz>
pkgname=opengrok
pkgver=1.0
pkgrel=3
pkgdesc="A fast and usable source code search and cross reference engine, written in Java"
url="https://oracle.github.io/opengrok/"
arch=('any')
license=('CDDL')
depends=('tomcat8' 'sh' 'java-runtime>=8' 'ctags' 'unzip')
makedepends=('apache-ant' 'jdk8-openjdk')
source=(${pkgname}-${pkgver}.tar.gz::"https://github.com/oracle/opengrok/archive/1.0.tar.gz")
sha1sums=('d1bbcdb4ceae2f631a44cd78bff9a361c83ca42e')

prepare() {
  cd ${pkgname}-${pkgver}
  # jre7 unsupported and doesn't work, hardcode jre8 java
  # note: jre9 might work, but untested
  sed -i '2iJAVA=/usr/lib/jvm/java-8-openjdk/bin/java' OpenGrok
}

build() {
  cd ${pkgname}-${pkgver}
  ant
}

package() {
  # Recreate 'ant dist' in $pkgdir rather than archive
  # take some liberties with directory naming and permissions
  cd ${pkgname}-${pkgver}

  # install docs
  for file in README.txt CHANGES.txt LICENSE.txt NOTICE.txt paths.tsv logging.properties; do
    install -Dm644 ${file} "${pkgdir}/usr/share/doc/opengrok/${file}"
  done
  install -Dm644 doc/EXAMPLE.txt "${pkgdir}/usr/share/doc/opengrok/EXAMPLE.txt"

  # install script
  install -Dm755 OpenGrok "${pkgdir}/usr/share/java/opengrok/bin/OpenGrok"

  # install tools
  install -Dm755 tools/Messages "${pkgdir}/usr/share/java/opengrok/bin/Messages"
  install -Dm755 tools/Groups "${pkgdir}/usr/share/java/opengrok/bin/Groups"

  # install dist files, excluding servlet-api jar
  install -dm755 "${pkgdir}/usr/share/java/opengrok/lib"
  cp -r dist/* "${pkgdir}/usr/share/java/opengrok/lib"
  rm "${pkgdir}/usr/share/java/opengrok/lib/lib/servlet-api-2.5.jar"

  # move man page
  install -dm755 "${pkgdir}/usr/share/man/man1/"
  mv "${pkgdir}/usr/share/java/opengrok/lib/opengrok.1" "${pkgdir}/usr/share/man/man1/"

  # link OpenGrok script to /usr/bin
  install -dm755 "${pkgdir}/usr/bin"
  ln -s /usr/share/java/opengrok/bin/OpenGrok "${pkgdir}/usr/bin/opengrok"

  # link license
  install -dm755 "${pkgdir}/usr/share/licenses/opengrok"
  ln -s /usr/share/doc/opengrok/LICENSE.txt "${pkgdir}/usr/share/licenses/opengrok/"
}
