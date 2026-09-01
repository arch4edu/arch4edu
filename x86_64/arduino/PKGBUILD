# Maintainer: Andreas Baumann <mail@andreasbauamnn.cc>
# Contributor: NicoHood <archlinux {cat} nicohood {dog} de>
# Contributor: Tomas Schertel <tschertel at gmail dot com>
# Contributor: Christopher Loen <christopherloen at gmail dot com>
# Contributor: Peter Reschenhofer <peter.reschenhofer@gmail.com>
# Contributor: Niels Martignène <niels.martignene@gmail.com>
# Contributor: PyroPeter <googlemail.com@abi1789>
# Contributor: darkapex <me@jailuthra.in>
# Contributor: tty0 <vt.tty0[d0t]gmail.com>
# Contributor: Andreas Baumann <mail@andreasbaumann.cc>

pkgname=arduino
pkgver=1.8.19
pkgrel=4
epoch=1
pkgdesc="Arduino prototyping platform SDK (Legacy 1.x.x)"
arch=('x86_64')
url="https://github.com/arduino/Arduino"
license=('GPL' 'LGPL')
depends=('gtk3' 'desktop-file-utils' 'shared-mime-info' 'java-runtime=8' 'arduino-builder')
#makedepends=('gtk2-compat' 'java-environment=8' 'ant' 'unzip' 'asciidoc')
makedepends=('java-environment=8' 'ant' 'unzip' 'asciidoc')
optdepends=('arduino-docs: Offline documentation for arduino'
            'arduino-avr-core: AVR core with upstream avr-gcc and avrdude')
options=(!strip)
conflicts=(arduino)
install="arduino.install"
source=("${pkgname}-${pkgver}.tar.xz::https://github.com/arduino/Arduino/releases/download/${pkgver}/arduino-${pkgver}.tar.xz"
        "${pkgname}-${pkgver}.tar.xz.asc::https://github.com/arduino/Arduino/releases/download/${pkgver}/arduino-${pkgver}.tar.xz.asc"
        # GPG signatures are not required as zip shasum is already provided by the buildfile
        # https://github.com/arduino/Arduino/issues/11522#issuecomment-840135044
        "https://github.com/arduino-libraries/WiFi101-FirmwareUpdater-Plugin/releases/download/v0.12.0/WiFi101-Updater-ArduinoIDE-Plugin-0.12.0.zip"
        "arduino-examples-1.9.1.zip::https://github.com/arduino/arduino-examples/archive/refs/tags/1.9.1.zip"
        "https://downloads.arduino.cc/libastylej-2.05.1-5.zip"
        "https://downloads.arduino.cc/libastylej-2.05.1-5.zip.asc"
        "https://downloads.arduino.cc/liblistSerials/liblistSerials-1.4.2-2.zip"
        "https://downloads.arduino.cc/liblistSerials/liblistSerials-1.4.2-2.zip.asc"
        "arduino.sh")
sha512sums=('a7ebc544c3fdc528763dee6f31b923c889aec65139c7ff8bd5309e034cad681d089a5f5fa7fecf3b00e553f812cbfb5ae330344edabdf2cbdaa34425e3ea06ba'
            'SKIP'
            '17e2d07fbdca491a8d80abb6f2ceb000c68af59b755da7db70dce2d5f781204340f43365c40e641acf0b084b2073b3b056f63d68990f405adefb76887f4c5b72'
            'c0e21dd374b2751a1e5f2b790202d4883879da2e26e9a23ccbaec478647e2b8160cbc085e76888deafc05b9b14b1aff4ce2a9b834a7b83e8226c3bc41801015c'
            '0678ed29caf8d80aeb852aa8a7f6fe545655314e75eaf6660a2a90505cda39863414ed05cfb8a3323f92d250601c8684021551606c40cea5ed81a1c322a0348c'
            'SKIP'
            '5ee4ca9c3137957b4130434cd0ee740fc1747ed1e015a94e5909e2392563c87ad7b60b156aed305510ec5f6cec495b2b478d8e355a9cdef6ca6bfb3ce97badf5'
            'SKIP'
            '78e2959daeb84828fe3a17b931831cf2581182ef14cc4afacdfba7c305967ebf461bf4098dbae3c07acab5a54d8ee64ba5245c8a75cd2064172bcfbf5dcc243d')
validpgpkeys=('326567C1C6B288DF32CB061A95FA6F43E21188C4') # Arduino Packages <support@arduino.cc>

build() {
    cd "arduino-${pkgver}/build"

    # Compile with java8
    export PATH=/usr/lib/jvm/default/bin/:"$PATH"

    # Do not include their avr-core + tools and no docs. We build them seperately
    ant clean dist -Dversion="${pkgver}" build -Dlight_bundle=true \
                                             -Dno_docs=true \
                                             -Dlocal_sources=true \
                                             -Dno_arduino_builder=true

    # Build man page
    a2x -f manpage shared/manpage.adoc
}

package() {
    cd "arduino-${pkgver}/build/linux/work"

    # Create directories
    install -dm755 "${pkgdir}/usr/share/"{doc,icons/hicolor,applications,mime/packages}

    # Copy the whole SDK
    cp -a . "${pkgdir}/usr/share/arduino"

    # Create wrapper for java8 + buider and documentation symlink
    install -Dm755 "${srcdir}/arduino.sh" "${pkgdir}/usr/bin/arduino"

    # Link arduino-builder, libastylej, libserialport and docs
    # TODO astyle libserialport do not work yet
    # TODO remove unzip dependency once all deps are resolved
    # https://github.com/arduino/ctags/issues/12
    # https://github.com/arduino/Arduino/issues/5538
    # https://github.com/arduino/listSerialPortsC/issues/9

    # Arduino-builder
    # https://bugs.archlinux.org/task/52377
    # https://github.com/arduino/arduino-builder/issues/209
    ln -s /usr/bin/arduino-builder "${pkgdir}/usr/share/arduino/arduino-builder"
    install -dm755 "${pkgdir}/usr/share/arduino/tools-builder"

    #rm "${pkgdir}/usr/share/arduino/lib/libastylej.so"
    #ln -s /usr/lib/libastyle-2.05.1.so "${pkgdir}/usr/share/arduino/lib/libastylej.so"
    #rm "${pkgdir}/usr/share/arduino/lib/liblistSerialsj.so"
    #ln -s /usr/lib/libserialport.so "${pkgdir}/usr/share/arduino/lib/liblistSerialsj.so"

    # Install desktop icons (keep a symlink for the arduino binary)
    cp -a lib/icons/* "${pkgdir}/usr/share/icons/hicolor"
    rm -rf "${pkgdir}/usr/share/arduino/lib/icons"
    ln -s /usr/share/icons/hicolor "${pkgdir}/usr/share/arduino/lib/icons"

    # Create desktop file using existing template
    sed "s,<BINARY_LOCATION>,arduino %U,g;s,<ICON_NAME>,arduino,g" "lib/desktop.template" \
    > "${pkgdir}/usr/share/applications/arduino.desktop"

    # Install Arduino mime type
    ln -s /usr/share/arduino/lib/arduino-arduinoide.xml "${pkgdir}/usr/share/mime/packages/arduino.xml"

    # Install manpage
    install -Dm644 "${srcdir}/arduino-${pkgver}/build/shared/arduino.1" "${pkgdir}/usr/share/man/man1/arduino.1"
}
