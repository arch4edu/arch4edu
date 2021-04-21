# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=arch4edu-keyring
pkgver=20200805
pkgrel=1
pkgdesc='arch4edu PGP keyring'
arch=('any')
url='https://github.com/arch4edu/keyring'
license=('GPL')
optdepends=('pkgstats: install to submit package usage statistics')
source=("$url/archive/$pkgver.tar.gz")
install=${pkgname}.install
sha512sums=('4e0482cbba53a509976f769bbe2a9715fefa7c6362439715a576b084bf8b2dd3c58e21066af786616c12b9ff47c508adf18cf55522f8c452a33195910a04ce1a')

package() {
  cd "$srcdir/keyring-$pkgver"

  install -Dm644 arch4edu.gpg $pkgdir/usr/share/pacman/keyrings/arch4edu.gpg
  install -Dm644 arch4edu-revoked $pkgdir/usr/share/pacman/keyrings/arch4edu-revoked
  install -Dm644 arch4edu-trusted $pkgdir/usr/share/pacman/keyrings/arch4edu-trusted
}

