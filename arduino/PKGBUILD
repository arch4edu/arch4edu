# Maintainer: NicoHood <aur {at} nicohood {dot} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161
# Contributor: Tomas Schertel <tschertel at gmail dot com>
# Contributor: Christopher Loen <christopherloen at gmail dot com>
# Contributor: Peter Reschenhofer <peter.reschenhofer@gmail.com>
# Contributor: Niels Martignène <niels.martignene@gmail.com>
# Contributor: PyroPeter <googlemail.com@abi1789>
# Contributor: darkapex <me@jailuthra.in>
# Contributor: tty0 <vt.tty0[d0t]gmail.com>

pkgname=arduino
pkgver=1.6.12
pkgrel=4
epoch=1
pkgdesc="Arduino prototyping platform SDK"
arch=('i686' 'x86_64')
url="https://github.com/arduino/Arduino"
license=('GPL' 'LGPL')
depends=('gtk2' 'desktop-file-utils' 'shared-mime-info' 'java-runtime=8' 'arduino-builder')
makedepends=('java-environment=8' 'apache-ant' 'unzip') # TODO remove unzip once all deps are resolved
optdepends=('arduino-docs: Offline documentation for arduino'
            'arduino-avr-core: AVR core with upstream avr-gcc and avrdude'
            'python2: Intel Galileo Board installation')
options=(!strip)
install="arduino.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/arduino/Arduino/archive/${pkgver}.tar.gz"
        "https://github.com/arduino-libraries/WiFi101-FirmwareUpdater-Plugin/releases/download/v0.8.0/WiFi101-Updater-ArduinoIDE-Plugin-0.8.0.zip"
        "https://downloads.arduino.cc/libastylej-2.05.1-3.zip"
        "https://downloads.arduino.cc/liblistSerials/liblistSerials-1.1.4.zip"
        "arduino.sh"
        "build.patch")
source_i686=("https://downloads.arduino.cc/tools/arduino-builder-linux32-1.3.21_r1.tar.bz2")
source_x86_64=("https://downloads.arduino.cc/tools/arduino-builder-linux64-1.3.21_r1.tar.bz2")
sha512sums=('2d386ddf26babc920767db9062304b75bf0b6b12ac469a33597b9b8abcc306a1ea6c18dd8b59f51fa2ecd7ffd66f36e80ade1953fd104cf29f0d74b5ab9da2d9'
            'b4ef0f253c56529eef52fad353f8e448f1756714a7fcd61370d7fabab61d4d09867b82301b2d30e4698f2c5b70b202e7536fa16a98e5fab0210c2c7d8f977e78'
            '7f82d64e34ef2d85a6b037caeecfa338b72f8edfc57a9903af3ab89b1d42cf7dfd9a6170abe8131ae3e6506850d82ed5092c3b08983a16d9c80319cd24c14555'
            'db605a53bbe8ce9da2387e991da2401054bf25f6172c4ffc72cba1fff8c44d819ed967f7f0e666e38ce967359573f6e3c544774832dd446f8107849ee76aaaba'
            '6dae08b8687e897ed370cc51cfeeba9020bb749356acfd367c796bf34fb43b763888340501be6a577859c19c37fe857be2b8fb52f1295769403b8e826c4e3f28'
            '71d36dcc21b399a9ebe70801f5738687d8c309ef0410bfb8b7f540d12d5df1771c09ecef8a271cdff492523b5a15e2ffb1b51b62cfccd6761eae28d0ffabcc02')
sha512sums_i686=('a0df7ba3d7f313aeac4c32365b9aaf32feb374c18e0b82516d61e51be10db897f368e46b6ff4e1574fec8b78fe584c39a76215974b32b440e85e27a1434e3d12')
sha512sums_x86_64=('223b81ae4cdb14962e3e6b271f78a88c055185785991d0ff32b3dbb3db9a4861cec495e5e726718df484e8c9901f5d3f0650d4d1e3b8d7bdb8f197c23222e748')

prepare()
{
    # Patch arduino build process. See PR: https://github.com/arduino/Arduino/pull/5438
    cd "${srcdir}/Arduino-${pkgver}"
    patch -Np1 -i "${srcdir}/build.patch"

    # echo -e "\n# By default, don't notify the user of a new upstream version." \
    #         "\n# https://bugzilla.redhat.com/show_bug.cgi?id=773519" \
    #         "\nupdate.check=false" \
    #     >> build/shared/lib/preferences.txt
}

build() {
    cd "Arduino-${pkgver}/build"

    # Compile with java8
    export PATH=/usr/lib/jvm/java-8-openjdk/jre/bin/:$PATH

    # Do not include their avr-core + tools and no docs. We build them seperately
    ant clean dist -Dversion=${pkgver} build -Dlight_bundle=true -Dno_docs=true -Dlocal_sources=true
}

package() {
    cd "Arduino-${pkgver}/build/linux/work"

    # Create directories
    install -dm755 "${pkgdir}/usr/share/"{doc,icons/hicolor,applications,mime/packages}

    # Copy the whole SDK
    cp -a . "${pkgdir}/usr/share/arduino"

    # Create wrapper for java8 + buider and documentation symlink
    install -Dm755 "${srcdir}/arduino.sh" "${pkgdir}/usr/bin/arduino"

    # Link arduino-builder, ctags, libastylej, libserialport and docs
    # TODO ctags, astyle libserialport do not work yet
    # https://github.com/arduino/ctags/issues/12
    # https://github.com/arduino/Arduino/issues/5538
    # https://github.com/arduino/listSerialPortsC/issues/9
    rm "${pkgdir}/usr/share/arduino/arduino-builder"
    ln -s /usr/bin/arduino-builder "${pkgdir}/usr/share/arduino/arduino-builder"
    # ctags TODO -> patch platform.txt and not the binary ln
    #rm "${pkgdir}/usr/share/arduino/tools-builder/ctags/5.8-arduino10/ctags"
    #ln -s /usr/bin/ctags "${pkgdir}/usr/share/arduino/tools-builder/ctags/5.8-arduino10/ctags"
    #rm "${pkgdir}/usr/share/arduino/lib/libastylej.so"
    #ln -s /usr/lib/libastyle-2.05.1.so "${pkgdir}/usr/share/arduino/lib/libastylej.so"
    #rm "${pkgdir}/usr/share/arduino/lib/liblistSerialsj.so"
    #ln -s /usr/lib/libserialport.so "${pkgdir}/usr/share/arduino/lib/liblistSerialsj.so"
    rm -r "${pkgdir}/usr/share/arduino/reference"
    ln -s /usr/share/doc/arduino "${pkgdir}/usr/share/arduino/reference"

    # Install desktop icons (keep a symlink for the arduino binary)
    cp -a lib/icons/* "${pkgdir}/usr/share/icons/hicolor"
    rm -rf "${pkgdir}/usr/share/arduino/lib/icons"
    ln -s /usr/share/icons/hicolor "${pkgdir}/usr/share/arduino/lib/icons"

    # Create desktop file using existing template
    sed "s,<BINARY_LOCATION>,arduino %U,g;s,<ICON_NAME>,arduino,g" "lib/desktop.template" \
    > "${pkgdir}/usr/share/applications/arduino.desktop"

    # Install Arduino mime type
    ln -s /usr/share/arduino/lib/arduino-arduinoide.xml "${pkgdir}/usr/share/mime/packages/arduino.xml"
}
