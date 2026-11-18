# Maintainer: SuperNinja_4965
# Contributor: FabioLolix
# Contributor: netroy

pkgname=arduino-ide-bin
pkgver=2.3.11
pkgrel=1
pkgdesc="Arduino prototyping platform IDE, rewrite based on the Theia IDE framework."
arch=(x86_64)
url="https://github.com/arduino/arduino-ide"
license=(AGPL3)
depends=(bash gcc-libs glib2 glibc libsecret libx11 libxkbfile python ripgrep libxkbfile libxss nss libsecret git)
optdepends=('libusb: Needed for some libraries or boards'
            'usbutils: Needed for stm32 boards using st-link'
            'libusb-compat: Needed for the `micronucleus` cli utility'
            'python-pyserial: Needed for esptool')
makedepends=(unzip)
provides=(arduino-ide)
conflicts=(arduino-ide)
replaces=(arduino-ide-beta-bin)
options=(!strip)
source=("https://github.com/arduino/arduino-ide/releases/download/${pkgver}/arduino-ide_${pkgver}_Linux_64bit.zip"
        "https://raw.githubusercontent.com/arduino/arduino-ide/155f0aebaf0e4e77a80f33a3422856ae5d3ad8e7/electron-app/resources/icons/512x512.png"
        "${pkgname}.sh")
sha256sums=('1e009f3c720092e6fae4e71809e0b755058e8c5d59eac7548b288d4f42b5e9b1'
            'bb8c484af1488c3596e0eb123a84766c84cf82328a1b3ec30c364203492157c9'
            'c02f0c40b92e50f46b09339d1ccfb0cb7cd7caa1e5d386ee9b85938810bfda34')
noextract=(arduino-ide_${pkgver}_Linux_64bit.zip)
            
prepare() {
	echo -e "[Desktop Entry]\nType=Application\nName=Arduino IDE v2\nGenericName=Arduino IDE v2\nComment=Open-source electronics prototyping platform\nExec=arduino-ide %U\nIcon=arduino-ide-v2\nTerminal=false\nMimeType=text/x-arduino;\nCategories=Development;IDE;Electronics;\nKeywords=embedded electronics;avr;microcontroller;\nStartupWMClass=Arduino IDE" > arduino-ide-v2.desktop
	
	mkdir -p "$srcdir/arduino-ide"
	unzip "$srcdir/arduino-ide_${pkgver}_Linux_64bit.zip" -d "$srcdir/arduino-ide"
}

package() {
	install -dm755 "$pkgdir/opt/"
	chmod -R 755 "arduino-ide"
	cp -r "$srcdir/arduino-ide/arduino-ide_${pkgver}_Linux_64bit/" "$pkgdir/opt/arduino-ide"
	install -dm755 "$pkgdir/usr/bin"
	install -Dm644 "$srcdir/arduino-ide-v2.desktop" "$pkgdir/usr/share/applications/arduino-ide-v2.desktop"
	install -Dm644 "$srcdir/512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/arduino-ide-v2.png"
	install -m755 "${srcdir}/${pkgname}.sh" "$pkgdir/usr/bin/arduino-ide"
}
