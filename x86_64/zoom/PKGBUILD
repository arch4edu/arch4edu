# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Maintainer: Christian Heusel <christian@heusel.eu>

pkgname=zoom
pkgver=6.6.0
_subver=4410
pkgrel=1
pkgdesc="Video Conferencing and Web Conferencing Service"
arch=('x86_64')
license=('LicenseRef-zoom')
url="https://zoom.us/"
replaces=('zoom-libs-bin' 'zoom-libs')
depends=('fontconfig' 'glib2' 'libpulse' 'libsm' 'ttf-font' 'libx11' 'libxtst' 'libxcb'
	'libxcomposite' 'libxfixes' 'libxi' 'libxcursor' 'libxkbcommon-x11' 'libxrandr'
	'libxrender' 'libxshmfence' 'libxslt' 'mesa' 'nss' 'xcb-util-image'
	'xcb-util-keysyms' 'xcb-util-cursor' 'dbus' 'libdrm' 'gtk3' 'qt5-webengine' 'qt5-remoteobjects')
optdepends=('pulseaudio-alsa: audio via PulseAudio'
	'ibus: remote control'
	'picom: extra compositor needed by some window managers for screen sharing'
	'xcompmgr: extra compositor needed by some window managers for screen sharing')
options=(!strip)
source=("${pkgname}-${pkgver}.${_subver}_orig_x86_64.pkg.tar.xz"::"https://zoom.us/client/${pkgver}.${_subver}/zoom_x86_64.pkg.tar.xz")
sha512sums=('5c9e9b9dd5a7c42274364d5055230bb8e438db6b1b0eeae0f7025e3e235811090d0ef70e706f79dc68e37afab0e2789a4a81439daf1c68ffb8eca38aa56ff8ea')

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
