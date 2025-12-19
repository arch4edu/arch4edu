# Maintainer: Nobbele <realnobbele@gmail.com>
# Contributor: Oscar Morante <oscar@mooistudios.com>
# Contributor: sinasio <synasius@gmail.com>
# Contributor: Marius Glo <marius@mgl.dev>

pkgname=unityhub
pkgver=3.15.4
pkgrel=1
pkgdesc="The Unity Hub is a standalone application that streamlines the way you find, download, and manage your Unity Projects and installations."
url="https://unity.com/"
arch=('x86_64')
license=('custom')
depends=('gtk3' 'libnotify' 'nss' 'libxss' 'libxtst' 'xdg-utils' 'at-spi2-core' 'util-linux-libs' 'libsecret' 'cpio' 'libxml2-legacy' '7zip' 'zip' 'unzip' 'tar')
optdepends=(
  'libappindicator-gtk3: The official deb says this an optional dependency'
)
source=(
  "$pkgname-$pkgver.deb::https://hub.unity3d.com/linux/repos/deb/pool/main/u/unity/unityhub_amd64/UnityHubSetup-$pkgver-amd64.deb"
  'license.txt'
  'services-config.json'
)
sha256sums=(
  '3bcad1e202d3a098147bc12c4efb24d404a118002c814e1ccb5f942135e2566f'
  'f0eb3a4bb148bb7f426e4f5b97e891265ac487710cbcba9282518537c7b5d833'
  '557964a3528219723750a7eabeb2e31a2d3e1b2c4a4b2e201b32d4035200562e'
)
conflicts=('unityhub-beta')
options=(!strip)
install='unityhub.install'

package() {
  tar -xf 'data.tar.bz2' -C "$pkgdir/"
  mkdir -p "$pkgdir/usr/bin"
  ln -sf '/opt/unityhub/unityhub' "$pkgdir/usr/bin/unityhub"

  install -Dm644 "$srcdir/license.txt" "$pkgdir/usr/share/licenses/$pkgname/license.txt"
  install -Dm644 "$srcdir/services-config.json" "$pkgdir/usr/share/unity3d/config/services-config.json"
}
