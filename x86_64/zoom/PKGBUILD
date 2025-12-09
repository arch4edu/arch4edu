# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Maintainer: Christian Heusel <christian@heusel.eu>

pkgname=zoom
pkgver=6.6.11
_subver=6052
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
sha512sums=('e36d84498b5ef938df2732041035732a34abe9dd787c2e4df7e0ec87ce65859ef359e0e2b27508ad356d4539238090a7d82cbf5004606719c4e2b820f4a08ec0')

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
