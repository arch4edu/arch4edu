# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=brackets
pkgver=1.13
pkgrel=2
_cef_ver=3.2785.1486
_node_ver=6.11.0
pkgdesc="An open source code editor for the web, written in JavaScript, HTML and CSS."
arch=('x86_64')
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
makedepends=('git' 'gtk2' 'python2' 'unzip')
install=${pkgname}.install
source=("git+https://github.com/adobe/brackets#tag=release-${pkgver//_/-}"
	#"git+https://github.com/adobe/brackets-shell#tag=release-${pkgver//_/-}"
	"git+https://github.com/adobe/brackets-shell#tag=release-1.12"
	"jslint::git+https://github.com/peterflynn/JSLint"
	"git+https://github.com/jrburke/requirejs"
	"mustache::git+https://github.com/janl/mustache.js"
	'https://patch-diff.githubusercontent.com/raw/adobe/brackets-shell/pull/648.patch'
	"http://s3.amazonaws.com/files.brackets.io/cef/cef_binary_${_cef_ver}_linux64_release.zip"
	"http://nodejs.org/dist/v${_node_ver}/node-v${_node_ver}-linux-x64.tar.gz"
	"https://github.com/adobe/brackets/releases/download/release-${pkgver}/Brackets.Release.${pkgver}.64-bit.deb"
)
noextract=("cef_binary_${_cef_ver}_linux64_release.zip" "node-v${_node_ver}-linux-x64.tar.gz")
md5sums=('SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         '4421e27e2e333a14b9f1dd3bea4248a6'
         '9b1364b60786a595076f9da789512685'
         'e6ade07945c32f82da184ebbcb5347dc'
         'b0a9869cf421970ecaeaf7aa180ec008')

prepare() {
	tar -xf data.tar.xz

	cd ${srcdir}/${pkgname}
	git config submodule.src/extensions/default/JSLint/thirdparty/jslint.url "$srcdir/jslint"
	for i in mustache requirejs
	do
		git config submodule.src/thirdparty/${i}.url "$srcdir/$i"
	done
	git submodule update --init --recursive

	cd ${srcdir}/brackets-shell
	sed 's/python/python2/' -i gyp/gyp
	sed 's/UnicodeString/icu::UnicodeString/g' -i appshell/appshell_extensions_platform.cpp
	sed '29i\#include <unicode/ucnv.h>' -i appshell/appshell_extensions_platform.h
	sed '29i\#include <unicode/unistr.h>' -i appshell/appshell_extensions_platform.h
	patch -Np1 < $srcdir/648.patch

	mkdir -p downloads
	ln -sf ${srcdir}/cef_binary_${_cef_ver}_linux64_release.zip downloads
	ln -sf ${srcdir}/node-v${_node_ver}-linux-x64.tar.gz downloads
}

build() {
	cd ${srcdir}/brackets-shell
	npm install
	rm -rf out
	node_modules/grunt-cli/bin/grunt cef node create-project

	# I hate static libs.
	sed 's|deps/icu/lib/\(.*\)\.a|/usr/lib/\1.so|g' -i Brackets.target.mk

	# Building
	cd ${srcdir}/brackets-shell
	make

	cd ${srcdir}/brackets
	npm install
	sed "/'npm-install',$/d" -i Gruntfile.js
	../brackets-shell/deps/node/bin/Brackets-node node_modules/grunt-cli/bin/grunt build
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
	cp ${srcdir}/opt/brackets/Brackets ${pkgdir}/opt/brackets/
	chmod 4755 ${pkgdir}/opt/brackets/chrome-sandbox

	cd ${srcdir}/${pkgname}
	cp -R "samples" "${pkgdir}/opt/brackets/samples"
	cp -R "dist" "${pkgdir}/opt/brackets/www"
	cp -R "node_modules" "${pkgdir}/opt/brackets/www"
}
