# Maintainer: Kenneth Endfinger <kaendfinger@gmail.com>

pkgname=jgit
pkgver=7.6.0.202603022253_r
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

sha512sums=('d63824efed06ad23e868d7fe7e05a3dcbb4b4161eb1663b4bc5c61ea3c2cb3ba655c8cd19573c630d825ee1d366e4c8cc1b4125c826358b925914661a93545b5'
            '289185bead9328258444210c1bfc1867f54ebb3cd6112b7b8e05da8e1aee32ceab0a8da3c99aaf5615cb00fe0bd174a0dca43922baa53775688bbef0b86ceadb')

package() {
  install -Dm 755 "${srcdir}/jgit-${pkgver}.sh" "${pkgdir}/usr/bin/jgit"
  install -Dm 644 "license.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
