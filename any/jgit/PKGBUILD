# Maintainer: Kenneth Endfinger <kaendfinger@gmail.com>

pkgname=jgit
pkgver=7.7.0.202606012155_r
pkgrel=1
pkgdesc="A 100% pure java implementation of git"
arch=('any')
url="http://www.eclipse.org/jgit/"
license=('custom:EDL')
depends=('java-runtime-common')
source=("jgit-${pkgver}.sh::https://repo.eclipse.org/content/groups/releases//org/eclipse/${pkgname}/org.eclipse.${pkgname}.pgm/${pkgver//_/-}/org.eclipse.${pkgname}.pgm-${pkgver//_/-}.sh"
        "license.txt"
)
noextract=("org.eclipse.${pkgname}.pgm-${pkgver//_/-}.sh")

sha512sums=('6cec304c1db423db67fb4223f325c230114aa358bef78881132fbe6f83da692ef68211c71e1e1f5c5661bc9039558ae87ffa0e9db7d55c7e92af888cbfaf5dde'
            '289185bead9328258444210c1bfc1867f54ebb3cd6112b7b8e05da8e1aee32ceab0a8da3c99aaf5615cb00fe0bd174a0dca43922baa53775688bbef0b86ceadb')

package() {
  install -Dm 755 "${srcdir}/jgit-${pkgver}.sh" "${pkgdir}/usr/bin/jgit"
  install -Dm 644 "license.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
