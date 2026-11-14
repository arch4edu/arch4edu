# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Simon Legner <Simon.Legner@gmail.com>
# Contributor: Chris Molozian (novabyte) <chris DOT molozian AT gmail DOT com>
# Contributor: Sanjuro Makabe (itti) <vuck AT gmx DOT de>

pkgbase=gradle
pkgname=('gradle' 'gradle-doc' 'gradle-src')
pkgver=9.9.0
pkgrel=1
pkgdesc='Powerful build system for the JVM'
url='https://gradle.org/'
arch=('any')
license=('Apache')
depends=(
  'bash'
  'coreutils'
  'findutils'
  'java-environment>=21'
  'sed'
  'which'
)
makedepends=(
  'asciidoc'
  'git'
  'groovy'
  'java-environment=8'
  'java-environment=11'
  'java-environment=17'
  'java-environment=25'
  'xmlto'
)
source=(https://services.gradle.org/distributions/${pkgbase}-${pkgver}-src.zip
        https://services.gradle.org/distributions/${pkgbase}-${pkgver}-all.zip
        ${pkgbase}.sh)
sha256sums=('c16d860198430fd8fd1c6914c4ca8283820d181ed0c5efa6fcce2275819a7bb4'
            '7aaba33a6aa7d03e0c7890869da1f1b5e1765c4d71db981a9d5db5cc47a10a6d'
            '4728dbdbe9fe416b82977cb7e456457e3ff0b88129291ee28e0d874ce8cc4891')
sha512sums=('45485b4b3c707b6473ead1408190343033208d405894832dbe71dc7952ff42078f56d24cd634c03f9468b41317032b77acd5f2a3e2eb63cc65c5ae4897d2d653'
            '40468c2bd953b4057319cd2144d1a7e7a65f6b021186d051461785dda9ddda8ea7175d57d2348c3b73ab08359d4773ca8f5ea7d7bdfecd4b6e94bd6f44ceca62'
            '9054a13f13a0d04bffefb2e5c1bcabfcd7b11e4d83d9180f65e0a09eeb8fea407d8c4e1e1e9b79191ba99e4eb372dbbb3189dd30833170c64cdb4484ca559441')

prepare() {
  cd ${pkgbase}-${pkgver}
  # remove adoptium references because we want to use our java implementation
  grep -lr "vendor = JvmVendorSpec.ADOPTIUM" | xargs sed -i "/JvmVendorSpec.ADOPTIUM/d"

  # inhibit automatic download of binary gradle
  sed -i -e "s#distributionUrl=.*#distributionUrl=file\:${srcdir}/${pkgbase}-${pkgver}-all.zip#" \
    -e '/^distributionSha256Sum=/d' \
    gradle/wrapper/gradle-wrapper.properties

  # isolated projects requires configuration cache; disable both so we can build without it
  sed -i '/org\.gradle\.\(unsafe\.\)\?isolated-projects/d' gradle.properties
  sed -i '/org\.gradle\.configuration-cache/d' gradle.properties
}

build() {
  cd ${pkgbase}-${pkgver}
  ./gradlew installAll \
    --info \
    -Porg.gradle.java.installations.paths=/usr/lib/jvm/java-21-openjdk \
    -Porg.gradle.java.installations.auto-download=false \
    -PfinalRelease=true \
    -Pgradle_installPath="$(pwd)/dist" \
    --no-configuration-cache
}

package_gradle() {
  cd ${pkgbase}-${pkgver}/dist
  optdepends=(
    'gradle-doc: gradle documentation'
    'gradle-src: gradle sources'
  )

  # install profile.d script
  install -Dm 644 "${srcdir}"/${pkgbase}.sh "${pkgdir}"/etc/profile.d/${pkgbase}.sh

  # create the necessary directory structure
  install -d "${pkgdir}"/usr/share/java/${pkgname}/bin
  install -d "${pkgdir}"/usr/share/java/${pkgname}/lib/{api,plugins,agents}
  install -d "${pkgdir}"/usr/share/java/${pkgname}/init.d
  install -d "${pkgdir}"/usr/bin

  # copy across jar files and module descriptor properties files
  install -Dm 644 lib/*.jar lib/*.properties "${pkgdir}"/usr/share/java/${pkgname}/lib
  install -Dm 644 lib/api/*.jar lib/api/*.properties "${pkgdir}"/usr/share/java/${pkgname}/lib/api
  install -Dm 644 lib/plugins/*.jar lib/plugins/*.properties "${pkgdir}"/usr/share/java/${pkgname}/lib/plugins
  install -Dm 644 lib/agents/*.jar lib/agents/*.properties "${pkgdir}"/usr/share/java/${pkgname}/lib/agents

  # copy across supporting text documentation and scripts
  install -m 644 NOTICE "${pkgdir}"/usr/share/java/${pkgname}
  install -m 755 bin/gradle "${pkgdir}"/usr/share/java/${pkgname}/bin
  install -m 644 init.d/*.* "${pkgdir}"/usr/share/java/${pkgname}/init.d

  # link gradle script to /usr/bin
  ln -s /usr/share/java/${pkgname}/bin/${pkgname} "${pkgdir}"/usr/bin
}

package_gradle-doc() {
  pkgdesc+=' (documentation)'
  options=('!strip')

  cd ${pkgbase}-${pkgver}/dist
  install -d "${pkgdir}"/usr/share/java/gradle/docs
  cp -r docs/* "${pkgdir}"/usr/share/java/gradle/docs
}

package_gradle-src() {
  pkgdesc+=' (sources)'
  options=('!strip')

  cd ${pkgbase}-${pkgver}/dist
  install -d "${pkgdir}"/usr/share/java/gradle/src
  cp -r src/* "${pkgdir}"/usr/share/java/gradle/src
}

# vim: ts=2 sw=2 et:
