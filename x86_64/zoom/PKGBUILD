# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Maintainer: Christian Heusel <christian@heusel.eu>

pkgname=zoom
pkgver=6.7.2
_subver=6498
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
)
options=(!strip)
source=("${pkgname}-${pkgver}.${_subver}_orig_x86_64.pkg.tar.xz"::"https://zoom.us/client/${pkgver}.${_subver}/zoom_x86_64.pkg.tar.xz")
sha512sums=('b13a8a7c65588907e05ad08944577024920b1b81526c54a7ebfb885957a13c5fc9b0f4738a68f3fb3e134c4cd37a2eaf4879b5390681bc3ac8cb8df5fcff9e0a')

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
