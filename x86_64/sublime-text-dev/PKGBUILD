# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Sander Boom <sanderboom@gmail.com>
# Contributor: realitygaps <realitygaps at yahoo dot com>

pkgname=sublime-text-dev
pkgver=4.4148
pkgrel=1
pkgdesc='Sophisticated text editor for code, html and prose - dev build'
arch=('x86_64' 'aarch64')
url='https://www.sublimetext.com/dev'
license=('custom')
depends=('libpng' 'gtk3')
conflicts=('sublime-text')
provides=('sublime-text')
install=${pkgname}.install

source_x86_64=("https://download.sublimetext.com/sublime_text_build_${pkgver:2}_x64.tar.xz")
source_aarch64=("https://download.sublimetext.com/sublime_text_build_${pkgver:2}_arm64.tar.xz")

sha256sums_x86_64=('cbb09509e4d67d58c4f790d649daae2cc47d6efa5ba76ac709f3a3eb713e595f')
sha256sums_aarch64=('8ec5827077891a37dfa88395d830c7f051d37a5e9cb3cd0b2073c162f00a2629')

package() {
	cd "${srcdir}"

	install -dm755 "${pkgdir}/opt"
	cp --preserve=mode -r 'sublime_text' "${pkgdir}/opt/sublime_text"
	rm -f "${pkgdir}/opt/sublime_text/sublime_text.desktop"

	for res in 128x128 16x16 256x256 32x32 48x48; do
		install -dm755 "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
		ln -s "/opt/sublime_text/Icon/${res}/sublime-text.png" "${pkgdir}/usr/share/icons/hicolor/${res}/apps/sublime-text.png"
	done

	sed -i 's#/opt/sublime_text/sublime_text#/usr/bin/subl#g' 'sublime_text/sublime_text.desktop'
	sed -i '\#^StartupNotify=#a StartupWMClass=subl' 'sublime_text/sublime_text.desktop'

	install -dm755 "${pkgdir}/usr/share/applications"
	install -Dm644 'sublime_text/sublime_text.desktop' "${pkgdir}/usr/share/applications/sublime_text.desktop"

	install -dm755 "${pkgdir}/usr/bin"
	ln -s '/opt/sublime_text/sublime_text' "${pkgdir}/usr/bin/subl"
}
