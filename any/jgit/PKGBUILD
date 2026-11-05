# Maintainer: Kenneth Endfinger <kaendfinger@gmail.com>

pkgname=jgit
pkgver=7.8.1.202611041320_r
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

sha512sums=('7e35a16b15aa5a6ddf1dfaceb833174dd2bbe701ea57e2dae0addbec1c7ec2589d07d47136f49393af20a0aa71b4e20bbf281dfe97e2fad05db078338ab4577f'
            '289185bead9328258444210c1bfc1867f54ebb3cd6112b7b8e05da8e1aee32ceab0a8da3c99aaf5615cb00fe0bd174a0dca43922baa53775688bbef0b86ceadb')

package() {
  install -Dm 755 "${srcdir}/jgit-${pkgver}.sh" "${pkgdir}/usr/bin/jgit"
  install -Dm 644 "license.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
