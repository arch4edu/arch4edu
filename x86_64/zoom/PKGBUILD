# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Maintainer: Christian Heusel <christian@heusel.eu>

pkgname=zoom
pkgver=7.1.5
_subver=4332
pkgrel=1
pkgdesc="Video Conferencing and Web Conferencing Service"
arch=('x86_64')
license=('LicenseRef-zoom')
url="https://zoom.us/"
replaces=('zoom-libs-bin' 'zoom-libs')
depends=('fontconfig' 'glib2' 'libpulse' 'libsm' 'ttf-font' 'libx11' 'libxtst' 'libxcb'
	'libxcomposite' 'libxfixes' 'libxi' 'libxcursor' 'libxkbcommon-x11' 'libxrandr'
	'libxrender' 'libxshmfence' 'libxslt' 'mesa' 'nss' 'xcb-util-image'
	'xcb-util-keysyms' 'xcb-util-cursor' 'dbus' 'libdrm' 'gtk3' 'xcb-util-wm')
optdepends=('pulseaudio-alsa: audio via PulseAudio'
	'ibus: remote control'
	'picom: extra compositor needed by some window managers for screen sharing'
	'xcompmgr: extra compositor needed by some window managers for screen sharing'
	'qt5-webengine: fallback for bundled qt'
	'qt5-remoteobjects: fallback for bundled qt'
	'noto-fonts-emoji: emojis'
)
options=(!strip)
source=("${pkgname}-${pkgver}.${_subver}_orig_x86_64.pkg.tar.xz"::"https://zoom.us/client/${pkgver}.${_subver}/zoom_x86_64.pkg.tar.xz")
sha512sums=('d5ca18a754565c569825606646488f9b51b757685fb5788b2b327356a00489812f66582c6f6d8d4ea8d03ca1c6f036b271f74f1b97f3dc2dcc54a115e13aa484')

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
