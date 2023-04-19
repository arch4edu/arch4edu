# Maintainer: Nobbele <realnobbele@gmail.com>
# Contributor: Oscar Morante <oscar@mooistudios.com>
# Contributor: sinasio <synasius@gmail.com>
# Contributor: Marius Glo <marius@mgl.dev>

pkgname=unityhub
pkgver=3.4.2
pkgrel=1
pkgdesc="The Unity Hub is a standalone application that streamlines the way you find, download, and manage your Unity Projects and installations."
url="https://unity.com/"
arch=('x86_64')
license=('custom')
depends=('nss' 'gtk3' 'cpio' 'openssl-1.1')
optdepends=(
  'libappindicator-gtk3: The official deb says this an optional dependency'
  'gconf: Required by Unity 2019.4 or older'
  'libicu50: May fix issues related to empty compiler errors'
  'icu70: : May fix issues related to empty compiler errors'
)
source=(
  "$pkgname-$pkgver.deb::https://hub.unity3d.com/linux/repos/deb/pool/main/u/unity/unityhub_amd64/unityhub-amd64-${pkgver}.deb"
  'license.txt'
)
sha256sums=('235aadac3f7822932eb746ba2541c4ac76a4b2867ecfcfdd0c6f14ebc639cc91'
            'f0eb3a4bb148bb7f426e4f5b97e891265ac487710cbcba9282518537c7b5d833')
conflicts=('unityhub-beta')
OPTIONS=(!strip)
install='unityhub.install'

package() {
  tar -xf 'data.tar.bz2' -C "$pkgdir/"
  mkdir -p "$pkgdir/usr/bin"
  ln -sf '/opt/unityhub/unityhub' "$pkgdir/usr/bin/unityhub"

  install -Dm644 "$srcdir/license.txt" "$pkgdir/usr/share/licenses/$pkgname/license.txt"
}
