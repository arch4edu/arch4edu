# Maintainer: NicoHood <archlinux {at} nicohood {dot} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161
# Contributor: Tomas Schertel <tschertel at gmail dot com>
# Contributor: Christopher Loen <christopherloen at gmail dot com>
# Contributor: Peter Reschenhofer <peter.reschenhofer@gmail.com>
# Contributor: Niels Martignène <niels.martignene@gmail.com>
# Contributor: PyroPeter <googlemail.com@abi1789>
# Contributor: darkapex <me@jailuthra.in>
# Contributor: tty0 <vt.tty0[d0t]gmail.com>

pkgname=arduino
pkgver=1.6.13
pkgrel=1
epoch=1
pkgdesc="Arduino prototyping platform SDK"
arch=('i686' 'x86_64')
url="https://github.com/arduino/Arduino"
license=('GPL' 'LGPL')
depends=('gtk2' 'desktop-file-utils' 'shared-mime-info' 'java-runtime=8' 'arduino-builder')
makedepends=('java-environment=8' 'apache-ant' 'unzip')
optdepends=('arduino-docs: Offline documentation for arduino'
            'arduino-avr-core: AVR core with upstream avr-gcc and avrdude'
            'python2: Intel Galileo Board installation')
options=(!strip)
install="arduino.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/arduino/Arduino/archive/${pkgver}.tar.gz"
        "https://github.com/arduino-libraries/WiFi101-FirmwareUpdater-Plugin/releases/download/v0.8.3/WiFi101-Updater-ArduinoIDE-Plugin-0.8.3.zip"
        "https://downloads.arduino.cc/libastylej-2.05.1-3.zip"
        "https://downloads.arduino.cc/liblistSerials/liblistSerials-1.2.0.zip"
        "arduino.sh"
        "build.patch")
source_i686=("https://downloads.arduino.cc/tools/arduino-builder-linux32-1.3.21_r1.tar.bz2")
source_x86_64=("https://downloads.arduino.cc/tools/arduino-builder-linux64-1.3.21_r1.tar.bz2")
sha512sums=('54643199a56fd01ac9e031fc03f174c38a2cc7b0b13953e1c543aae58f2d0987ad127abe224e3863eb6ec9c81022288073613f86b75543babfc9d186f75a15f9'
            'fb2c5f77ea047c060e67705886d106379ac4a297f3a7d1f7d6d0b2410c4592f09cece4578aeeaed867c03a2efe5fe8d124ccc36c4189ee5c875cd16473a6faab'
            '7f82d64e34ef2d85a6b037caeecfa338b72f8edfc57a9903af3ab89b1d42cf7dfd9a6170abe8131ae3e6506850d82ed5092c3b08983a16d9c80319cd24c14555'
            '79f2eaf75c5f948c8388b6d89d3ce1f14518390ee2df111e1603eafb490f54a5c071af61b228cae3bfa8c20bc0a5450b1131f2328c419241ba0d127837b97292'
            'd97e73a6764232c5fbcdbd46d98f1dfde1d95d8256f578fb05480694423842ec864c49d572a325c7d00b026619d84dc114f1e3e0d2f8219b94871dce1718f05a'
            '8f0186a6554a54c3067bcf71b8891a6e51b2613fd9135f4b0a10e6e24f4797757ca968ee1195f5bcac01f0aa22b73005b273939346a3aea9aee391e8d31a3588')
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
    # TODO remove unzip dependency once all deps are resolved
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
