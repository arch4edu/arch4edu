# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: kalenz <https://aur.archlinux.org/account/kalenz>
# Contributor: Vojtech Horky <vojta . horky at-symbol seznam . cz>
pkgname=opengrok
pkgver=1.3.11
pkgrel=1
pkgdesc="A fast and usable source code search and cross reference engine, written in Java"
url="https://oracle.github.io/opengrok/"
arch=('any')
license=('CDDL')
depends=('tomcat8' 'sh' 'java-runtime>=8' 'ctags' 'unzip')
makedepends=('apache-ant' 'java-runtime-openjdk' 'git' 'maven' 'subversion' 'python')
source=(git+"https://github.com/oracle/${pkgname}.git#tag=${pkgver}")
sha1sums=('SKIP')

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

  # move man dir down to /usr/share
  mv "${pkgdir}/usr/share/java/${pkgname}/man" "${pkgdir}/usr/share/"

  # link licenses to /usr/share/licenses
  install -dm755 "${pkgdir}/usr/share/licenses"
  ln -s /usr/share/java/${pkgname}/doc "${pkgdir}/usr/share/licenses/${pkgname}"
}

