# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>

pkgname=zoom
pkgver=6.2.6
_subver=2503
pkgrel=1
pkgdesc="Video Conferencing and Web Conferencing Service"
arch=('x86_64')
license=('LicenseRef-zoom')
url="https://zoom.us/"
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
sha512sums=('8f42230fc2d2843d10c7e22827f91818a2d6f1167b3a97c0a0cf2b249ba9b8378ac5e43625ac540419c83a6b13835f11d33183b53dd4e2109be89ccdb60dd0b6')

prepare() {
	sed -i 's/Zoom\.png/Zoom/g' "${srcdir}/usr/share/applications/Zoom.desktop"
	sed -i 's/StartupWMClass=Zoom/StartupWMClass=zoom/g' "${srcdir}/usr/share/applications/Zoom.desktop"
}

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
