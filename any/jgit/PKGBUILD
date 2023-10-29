# Maintainer: Kenneth Endfinger <kaendfinger@gmail.com>

pkgname=jgit
pkgver=6.7.0.202309050840_r
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

sha512sums=('14b1aec6647707c7f3c80750edf836956a8cb79adbb5bc5eaf130a8fcf7db60dc36d70eff325cb3bfa6a9f9518c3e3fcced225868df201fbf6f6aa8fb243b47e'
            '289185bead9328258444210c1bfc1867f54ebb3cd6112b7b8e05da8e1aee32ceab0a8da3c99aaf5615cb00fe0bd174a0dca43922baa53775688bbef0b86ceadb')

package() {
  install -Dm 755 "${srcdir}/jgit-${pkgver}.sh" "${pkgdir}/usr/bin/jgit"
  install -Dm 644 "license.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
