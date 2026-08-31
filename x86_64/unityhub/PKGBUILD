# Maintainer: Nobbele <realnobbele@gmail.com>
# Contributor: Oscar Morante <oscar@mooistudios.com>
# Contributor: sinasio <synasius@gmail.com>
# Contributor: Marius Glo <marius@mgl.dev>
# Contributor: Léo <aur@salut-c-leo.fr>

pkgname=unityhub
pkgver=3.21.0
pkgrel=1
pkgdesc="The Unity Hub is a standalone application that streamlines the way you find, download, and manage your Unity Projects and installations."
url="https://unity.com/"
arch=('x86_64')
license=('custom')
depends=('gtk3' 'libnotify' 'nss' 'libxss' 'libxtst' 'libdrm' 'xdg-utils' 'libxcb' 'at-spi2-core' 'util-linux-libs' 'libsecret' 'zip' 'unzip' 'tar' 'cpio')
source=(
  "$pkgname-$pkgver.deb::https://hub.unity3d.com/linux/repos/deb/pool/main/u/unity/unityhub_amd64/unityhub_${pkgver}_amd64.deb"
  'license.txt'
  'services-config.json'
)
sha256sums=(
  'b90d3e38ecfac7b3cc5954b298cc8beec915250a4cb0038bb50781ee1fce0e25'
  '6f50dbc9b2fbe70693aefcbcdb4d7be249ab8dcadf6f7f41458681989ead7a0e'
  '557964a3528219723750a7eabeb2e31a2d3e1b2c4a4b2e201b32d4035200562e'
)
conflicts=('unityhub-beta')
options=(!strip)
install='unityhub.install'

package() {
  tar -xf 'data.tar.zst' -C "$pkgdir/"
  mkdir -p "$pkgdir/usr/bin"
  ln -sf "/usr/lib/unityhub/unityhub" "$pkgdir/usr/bin/unityhub"

  install -Dm644 "$srcdir/license.txt" "$pkgdir/usr/share/licenses/$pkgname/license.txt"
  install -Dm644 "$srcdir/services-config.json" "$pkgdir/usr/share/unity3d/config/services-config.json"
}
