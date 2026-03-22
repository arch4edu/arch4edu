# Maintainer: Jason Go <jasongo@jasongo.net>
# Contributor: Core_UK <dev@coredev.uk>

pkgname=cider
pkgver=1.6.3.20260321034536
pkgrel=2
pkgdesc='An abandoned Apple Music player using a fork of Cider v1 from taoky/Cider'
arch=('x86_64')
url='https://github.com/taoky/Cider'
license=('AGPL-3.0-only')
depends=(
  'alsa-lib'
  'gtk3'
  'libxcrypt-compat'
  'nss'
)
makedepends=('git' 'nodejs' 'pnpm' 'python')
optdepends=(
  'libnotify: Send playback notifications'
  'gnome-shell-extension-appindicator: Show tray icon in GNOME'
)
options=(!buildflags !debug !makeflags !strip)
source=("git+$url.git#tag=${pkgver##*.}")
b2sums=('6896547b5cfcc9de8c12d90c32ec4edd9086dab2910d65e7070671f535842b08b5a61b16303901a98d94d73bc7d6c4c68a5a800cb6af3f6a0785eb6d1a3265d5')
install=cider.install

prepare() {
  cd Cider

  # Use TOKEN environment variable
  echo 'localStorage.setItem("lastToken", process.env.TOKEN);' >> ./src/preload/cider-preload.js
  sed -i "/var prompt = \`Cider is not responding/c\\var prompt = \`Your Apple Music TOKEN is expired or invalid. Edit /usr/share/applications/sh.cider.Cider.desktop and modify the TOKEN value in the Exec line then restart Cider. (Current value of TOKEN=\${lastToken}).\`;" ./src/renderer/main/events.js

  # Prevent weird "SyntaxError: Unexpected end of JSON input" as described here:
  # https://github.com/electron-userland/electron-builder/issues/9020#issuecomment-2989607912
  pnpm add -D electron-builder@26.0.0

  pnpm install
}

build() {
  cd Cider
  pnpm run build
  pnpm exec electron-builder --linux deb --publish=never

  # Extract the deb file
  bsdtar -xf ./dist/cider*_amd64.deb --include='data.tar*' -O | bsdtar -xf - -C "$srcdir"

  # Add TOKEN environment variable to .desktop file
  sed -i 's|Exec=/opt/Cider/sh.cider.Cider|Exec=env TOKEN=none CIDER_PORT=9000 /usr/bin/cider|' "$srcdir/usr/share/applications/sh.cider.Cider.desktop"

  # Modify apparmor-profile to include cider link
  sed -i 's|"/opt/Cider/sh.cider.Cider"|("/opt/Cider/sh.cider.Cider" "/usr/bin/cider")|' "$srcdir/opt/Cider/resources/apparmor-profile"
}

package() {
  # 1. CREATE BINARY LINK
  install -d "$pkgdir/usr/bin/"
  ln -sf /opt/Cider/sh.cider.Cider "$pkgdir/usr/bin/cider"

  # 2. COPY DEB FILES
  cp -dr --no-preserve=ownership ./{opt,usr} "$pkgdir"

  # 3. COPY LICENSE AND DOCS
  install -Dm644 -t "$pkgdir/usr/share/licenses/cider/" ./Cider/LICENSE
  install -Dm644 -t "$pkgdir/usr/share/doc/cider/" ./Cider/{CODE_OF_CONDUCT.md,README.md}

  # 4. COPY APPARMOR PROFILE
  install -Dm644 ./opt/Cider/resources/apparmor-profile "$pkgdir/etc/apparmor.d/cider"
}
