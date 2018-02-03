# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=brackets
pkgver=1.12
pkgrel=1
pkgdesc="An open source code editor for the web, written in JavaScript, HTML and CSS."
arch=('i686' 'x86_64')
url="http://brackets.io"
license=('MIT')
depends=(alsa-lib desktop-file-utils gconf libgcrypt15 libudev0-shim libxss libxtst nodejs npm nss pango)
optdepends=(
	"google-chrome: to enable Live Preview"
	"gnuplot: to enable node benchmarking"
	"gtk2: to enable native UI"
	"ruby: to enable LiveDevelopment Inspector"
	"hicolor-icon-theme: for hicolor theme hierarchy"
)
conflicts=("brackets-git" "brackets-bin")
makedepends=('gcc5' 'git' 'gtk2' 'python2' 'unzip')
install=${pkgname}.install
source=("git+https://github.com/adobe/brackets#tag=release-${pkgver}"
	"git+https://github.com/adobe/brackets-shell#tag=release-${pkgver}"
	#"git+https://github.com/adobe/brackets-shell#branch=linux-1547"
)
md5sums=('SKIP' 'SKIP')

prepare() {
	cd ${srcdir}/${pkgname}
	git submodule update --init --recursive
}

build() {
	#`npm install package` fails with https://registry.npmjs.org/
	npm_registry=$(npm config get registry)
	cd ${srcdir}/brackets
	npm config set registry "https://registry.npm.taobao.org"
	npm install package
	npm config set registry "$npm_registry"

	cd ${srcdir}/brackets
	npm install
	sed "/'npm-install',$/d" -i Gruntfile.js
	node_modules/grunt-cli/bin/grunt build

	cd ${srcdir}/brackets-shell
	sed -i 's/python/python2/' gyp/gyp
	npm install
	#environment cleaning due to branch switch
	rm -rf out
	node_modules/grunt-cli/bin/grunt cef icu node create-project
	#use g++-5 to solve icu ABI issue
	LINK=g++-5 make
}

package() {
	cd ${srcdir}/brackets-shell
	install -Dm755 installer/linux/debian/brackets "${pkgdir}/opt/brackets/brackets"
	install -dm755 "${pkgdir}/usr/bin"
	ln -s /opt/brackets/brackets "$pkgdir/usr/bin/brackets"

	install -dm755 "${pkgdir}/usr/share"
	install -Dm644 installer/linux/debian/brackets.desktop "${pkgdir}/usr/share/applications/brackets.desktop"
	install -Dm644 installer/linux/debian/package-root/usr/share/icons/hicolor/scalable/apps/brackets.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/brackets.svg"
	for size in 32 48 128 256; do
		install -Dm644 "out/Release/files/appshell${size}.png" "${pkgdir}/usr/share/icons/hicolor/${size}x${size}/apps/brackets.png"
	done

	cd out/Release
	install -dm755 "${pkgdir}/opt/brackets"
	cp -R {files,locales,node-core} "${pkgdir}/opt/brackets/"
	find . -maxdepth 1 -type f -exec \
	cp {} ${pkgdir}/opt/brackets/{} \;
	chmod 4755 ${pkgdir}/opt/brackets/chrome-sandbox

	cd ${srcdir}/${pkgname}
	cp -R "samples" "${pkgdir}/opt/brackets/samples"
	cp -R "dist" "${pkgdir}/opt/brackets/www"
}
