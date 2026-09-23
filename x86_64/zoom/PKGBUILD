# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Maintainer: Christian Heusel <christian@heusel.eu>

pkgname=zoom
pkgver=7.2.1
_subver=5760
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
sha512sums=('12272ae2626e4de50683b4198bedb5c87940337e8586a6ec01d3078f7e7810537f1d8584531dcfc4840c2c3c0a034a2bf4005630e8d4211b489b3360effb7dd3')

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
