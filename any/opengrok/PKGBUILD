# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: kalenz <https://aur.archlinux.org/account/kalenz>
# Contributor: Vojtech Horky <vojta . horky at-symbol seznam . cz>
pkgname=opengrok
pkgver=1.11.7
pkgrel=1
pkgdesc="A fast and usable source code search and cross reference engine, written in Java"
url="https://oracle.github.io/opengrok/"
arch=('any')
license=('CDDL')
depends=('tomcat10' 'sh' 'java-runtime>=11' 'ctags' 'unzip')
makedepends=('apache-ant' 'java-runtime-openjdk' 'git' 'maven' 'python')
source=(git+"https://github.com/oracle/${pkgname}.git#tag=${pkgver}")
install=opengrok.install
sha1sums=('SKIP')

prepare() {
  # Supress deprecated warnings (issue reported at https://github.com/oracle/opengrok/issues/4312 )
  sed -i '/Werror/d' ${pkgname}/pom.xml
}

build() {
  cd ${pkgname}
  mvn compile

  # The following fails if tests are run, but upstream disable tests for their
  # automated builds, so we do the same and assume it's fine
  mvn -DskipTests=true package
}

package() {
  # make destination for most stuff
  install -dm755 "${pkgdir}/usr/share/java/${pkgname}"

  # extract distribution archive into destination (use --no-same-owner to change owner to root instead of builduser)
  bsdtar xf "${pkgname}/distribution/target/${pkgname}-${pkgver}.tar.gz" -C "${pkgdir}/usr/share/java/${pkgname}" -s "/${pkgname}-${pkgver}//" --no-same-owner

  # link licenses to /usr/share/licenses
  install -dm755 "${pkgdir}/usr/share/licenses"
  ln -s /usr/share/java/${pkgname}/doc "${pkgdir}/usr/share/licenses/${pkgname}"
}

