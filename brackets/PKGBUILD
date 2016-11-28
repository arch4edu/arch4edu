# Maintainer: 4javier <4javiereg4 _ at _ gmail _ dot _com>

pkgname=brackets
pkgver=1.8
pkgrel=1
pkgdesc="An open source code editor for the web, written in JavaScript, HTML and CSS. Stable git Tags."
arch=('i686' 'x86_64')
url="http://brackets.io"
license=('MIT')
depends=(alsa-lib nodejs npm desktop-file-utils gconf libgcrypt15 libudev0)
optdepends=(
	"google-chrome: to enable Live Preview"
	"gnuplot: to enable node benchmarking"
	"gtk2: to enable native UI"
	"ruby: to enable LiveDevelopment Inspector"
	"hicolor-icon-theme: for hicolor theme hierarchy"
)
conflicts=("brackets-git" "brackets-bin")
makedepends=('git' 'unzip' 'gyp-git')
install=${pkgname}.install
source=("brackets-shell::git+https://github.com/adobe/brackets-shell.git#branch=linux-1547"
		#"brackets-shell::git+https://github.com/adobe/brackets-shell.git#tag=release-${pkgver}"
        "${pkgname}::git+https://github.com/adobe/brackets.git#tag=release-${pkgver}")
md5sums=('SKIP' 'SKIP')


prepare() {
  cd ${srcdir}/${pkgname}
  git submodule update --init --recursive
}

build() {
  cd ${srcdir}/brackets-shell
  npm install
  ##### environment cleaning due to branch switch ####
  rm -rf out
  node_modules/grunt-cli/bin/grunt cef-clean
  ####################################################
  node_modules/grunt-cli/bin/grunt setup
  make
}

package() {
  cd ${srcdir}/brackets-shell
  
  install -dm755 "${pkgdir}/opt/brackets"
  cp -R out/Release/lib "${pkgdir}/opt/brackets/lib"
  cp -R out/Release/locales "${pkgdir}/opt/brackets/locales"
  cp -R out/Release/node-core "${pkgdir}/opt/brackets/node-core"
  install -Dm644 out/Release/cef.pak "${pkgdir}/opt/brackets/cef.pak"
  install -Dm644 out/Release/devtools_resources.pak "${pkgdir}/opt/brackets/devtools_resources.pak"
  install -Dm755 out/Release/Brackets "${pkgdir}/opt/brackets/Brackets"
  install -Dm755 out/Release/Brackets-node "${pkgdir}/opt/brackets/Brackets-node"
  install -Dm755 installer/linux/debian/brackets "${pkgdir}/opt/brackets/brackets"
  for size in 32 48 128 256; do
    install -Dm644 "out/Release/appshell${size}.png" "${pkgdir}/opt/brackets/appshell${size}.png"
  done

  install -dm755 "${pkgdir}/usr/bin"
  ln -s /opt/brackets/brackets "$pkgdir/usr/bin/brackets"

  install -dm755 "${pkgdir}/usr/share"
  install -Dm644 installer/linux/debian/brackets.desktop "${pkgdir}/usr/share/applications/brackets.desktop"
  install -Dm644 installer/linux/debian/package-root/usr/share/icons/hicolor/scalable/apps/brackets.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/brackets.svg"
  for size in 32 48 128 256; do
    install -Dm644 "out/Release/appshell${size}.png" "${pkgdir}/usr/share/icons/hicolor/${size}x${size}/apps/brackets.png"
  done
  
  cd ${srcdir}/${pkgname}
  # Copy samples
  cp -R "samples" "${pkgdir}/opt/brackets/samples"
  # Copy www
  cp -R "src" "${pkgdir}/opt/brackets/www"
}
