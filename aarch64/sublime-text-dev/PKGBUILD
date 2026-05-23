# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Sander Boom <sanderboom@gmail.com>
# Contributor: realitygaps <realitygaps at yahoo dot com>

pkgname=sublime-text-dev
pkgver=4.4205
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
sha512sums_x86_64=('ba7288d08d094a8745d30a191ba5f2b3f6d9d0fbc2a15ec3936bc13c4ebd9dba6aaf152660f3c209173b40ac56a221c9de607f0e2b93021c9129f1f8b97857a0')
sha512sums_aarch64=('8556d613694f844b6721c4dfd3da556075b1b38cabfdc1839912d70ad1b5686357c0f4f526a5c87464ed376f784e95c646bd2e706018561d0157933cd317ccb8')

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
