# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Sander Boom <sanderboom@gmail.com>
# Contributor: realitygaps <realitygaps at yahoo dot com>

pkgname=sublime-text-dev
pkgver=4.4196
pkgrel=1
pkgdesc='Sophisticated text editor for code, html and prose - dev build'
arch=('x86_64' 'aarch64')
url='https://www.sublimetext.com/dev'
license=('custom')
depends=('libpng' 'gtk3')
conflicts=('sublime-text')
provides=('sublime-text')
install=${pkgname}.install

source=("${pkgname}.sh")
source_x86_64=("${pkgname//-/_}_${pkgver/./_}_${pkgrel}_x64.tar.xz::https://download.sublimetext.com/sublime_text_build_${pkgver:2}_x64.tar.xz")
source_aarch64=("${pkgname//-/_}_${pkgver/./_}_${pkgrel}_arm64.tar.xz::https://download.sublimetext.com/sublime_text_build_${pkgver:2}_arm64.tar.xz")

sha512sums=('ac56e9b7dddaebb3d222795cfc644109c93cc3f79695b8f9ee56022c74fe04a1134dd54cab07c74ff1f96b783cb3dbc026c16095552f1d2dd83115ea274dc2e9')
sha512sums_x86_64=('dc85c20e26f4c6da577d44ab7c50fdaf476bbe648f286fe9be2b465fd69b14deef1478d103678708f29ae0b1e0a8212b1389ec906fd431f1e4e74ffbad27b42d')
sha512sums_aarch64=('ac9e9bcb639c5b12d46784af239c2ed662829e039d08a864fbe8db54b7e23effdffaf4db36321ed40e2d297aad41d53bedf02824ade4aa833986d9f7605fff42')

prepare() {
	sed -i -e "s|@ST_PATH@|/opt/sublime_text|g" "${pkgname}.sh"
	sed -i -e 's#/opt/sublime_text/sublime_text#/usr/bin/subl#g' 'sublime_text/sublime_text.desktop'
	sed -i -e '\#^StartupNotify=#a StartupWMClass=subl' 'sublime_text/sublime_text.desktop'
}

package() {
	install -dm755 "${pkgdir}/opt"
	cp --preserve=mode -r 'sublime_text' "${pkgdir}/opt/sublime_text"
	rm -f "${pkgdir}/opt/sublime_text/sublime_text.desktop"

	for res in 128x128 16x16 256x256 32x32 48x48; do
		install -dm755 "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
		ln -s "/opt/sublime_text/Icon/${res}/sublime-text.png" "${pkgdir}/usr/share/icons/hicolor/${res}/apps/sublime-text.png"
	done

	install -dm755 "${pkgdir}/usr/share/applications"
	install -Dm644 'sublime_text/sublime_text.desktop' "${pkgdir}/usr/share/applications/sublime_text.desktop"

	install -dm755 "${pkgdir}/usr/bin"
	install -Dm755 "${pkgname}.sh" "${pkgdir}/usr/bin/subl"
}
