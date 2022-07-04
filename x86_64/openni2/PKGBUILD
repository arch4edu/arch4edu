# Maintainer: acxz<akashpatel2008 at yahoo dot com>
# Contributor: Christian Bühler <christian.buehler@ipoplan.de>

pkgname=openni2
pkgver=2.2.0
_srcname=OpenNI2-${pkgver}-debian
pkgrel=2
pkgdesc='Framework for sensor-based Natural Interaction'
arch=('i686' 'x86_64')
url='https://github.com/occipital/OpenNI2/'
license=('Apache-2.0')
depends=('freeglut' 'glu' 'libusb' 'systemd' 'java-environment' 'libjpeg-turbo')
makedepends=('python' 'doxygen' 'graphviz')
source=("https://github.com/occipital/OpenNI2/archive/v${pkgver}-debian.tar.gz"
        '0002-Change-path-of-config-files-to-etc-openni2.patch'
        '0003-Use-system-wide-libjpeg.patch'
        '0005-change-default-ni-drivers-path.patch'
        '0013-Fix-GCC6-compilation.patch'
        '0014-fix-format-overflow-for-GCC7.patch'
        '0015-Initialize-variable-for-gcc7.patch'
        'libopenni2.pc')
sha256sums=('08f6842f20d1098ab2ebafadaac0130ffae5abd34cdf464bb6100cbe01ed95a8'
            '368c0b41a26a65377359ce22a914cb8b6f4020e2972f67f151f2b9bdbf1a5a50'
            '1ca20e60ac10a193cbf0ca4759230ba7930479baa7d237476583359e7b62f604'
            '635c762230a2dc57977c7f42cc7d1c25438d3864baca7632360466e8c031e3b5'
            '0fd53b2c41a48cb4b28e67c6cfcedf4d17ffbe675bd2eb21793a683bbb0d85bb'
            '05e95ab2375294a37354dab5ed746ff5c6de6e5ed1792ad398f489d6d35af93e'
            '196128c92803cbfaa67643703e043247475b6c718af8cd9b4333806d2e04d762'
            '57c9236c77133437a533d3cac6775da4749a070dd468e88e29b07d7a83aaaab1')

prepare() {
    cd "$_srcname"

    # fix building documentation with java 8
    # https://github.com/OpenNI/OpenNI2/issues/87
    local _javaver
    _javaver="$(archlinux-java get | grep -o '^[^-]*.[0-9]*')"
    if [ "$(vercmp "$_javaver" java-8)" -ge '0' ]
    then
        sed -i "s/cmd = \[javaDocExe, '-d', 'java'\]/cmd = [javaDocExe, '-d', 'java', '-Xdoclint:none']/" Source/Documentation/Runme.py
    fi

    # apply patches
    patch -Np1 -i "${srcdir}/0002-Change-path-of-config-files-to-etc-openni2.patch"
    patch -Np1 -i "${srcdir}/0003-Use-system-wide-libjpeg.patch"
    patch -Np1 -i "${srcdir}/0005-change-default-ni-drivers-path.patch"
    patch -Np1 -i "${srcdir}/0013-Fix-GCC6-compilation.patch"
    patch -Np1 -i "${srcdir}/0014-fix-format-overflow-for-GCC7.patch"
    patch -Np1 -i "${srcdir}/0015-Initialize-variable-for-gcc7.patch"
}

build() {
    cd "$_srcname"
    make
    make doc
}

package() {
    [ "$CARCH" = 'x86_64' ] && local _architecture='x64'
    [ "$CARCH" = 'i686'   ] && local _architecture='x86'

    # directories creation
    mkdir -p "${pkgdir}/usr/"{bin,include/openni2/{Driver,Linux-Arm,Linux-x86}}
    mkdir -p "${pkgdir}/usr/lib/"{OpenNI2/Drivers,pkgconfig}
    mkdir -p "${pkgdir}/usr/share/"{doc/"${pkgname}",licenses/"${pkgname}"}
    mkdir -p "${pkgdir}/usr/lib/udev/rules.d" # usb rules (udev rules)
    mkdir -p "${pkgdir}/etc/openni2/Drivers"  # config

    # binaries and libraries
    cd "${_srcname}/Bin/${_architecture}-Release"
    install    -m755 NiViewer             "${pkgdir}/usr/bin/NiViewer2"
    install -D -m755 ClosestPointViewer   "${pkgdir}/usr/bin"
    install -D -m755 EventBasedRead       "${pkgdir}/usr/bin"
    install -D -m755 Multi*               "${pkgdir}/usr/bin"
    install -D -m755 MWClosestPointApp    "${pkgdir}/usr/bin"
    install -D -m755 PS*                  "${pkgdir}/usr/bin"
    install -D -m755 Simple*              "${pkgdir}/usr/bin"
    install -D -m755 *.so                 "${pkgdir}/usr/lib"
    install -D -m755 OpenNI2/Drivers/*.so "${pkgdir}/usr/lib/OpenNI2/Drivers"

    # includes
    cd "${srcdir}/${_srcname}/Include"
    install -D -m644 *.h         "${pkgdir}/usr/include/openni2"
    install -D -m644 Driver/*    "${pkgdir}/usr/include/openni2/Driver"
    install -D -m644 Linux-Arm/* "${pkgdir}/usr/include/openni2/Linux-Arm"
    install -D -m644 Linux-x86/* "${pkgdir}/usr/include/openni2/Linux-x86"

    # udev rules
    cd "${srcdir}/${_srcname}/Packaging/Linux"
    install -m644 primesense-usb.rules "${pkgdir}/usr/lib/udev/rules.d/60-openni2-usb.rules"

    # config
    cd "${srcdir}/${_srcname}/Config"
    install -D -m644 *.ini             "${pkgdir}/etc/openni2"
    install -D -m644 OpenNI2/Drivers/* "${pkgdir}/etc/openni2/Drivers"

    # documentation
    cd "${srcdir}/${_srcname}/Source/Documentation/html"
    install -D -m644 * "${pkgdir}/usr/share/doc/${pkgname}"

    # pkg-config file
    cd "$srcdir"
    install -D -m644 libopenni2.pc "${pkgdir}/usr/lib/pkgconfig"

    # license
    cd "$_srcname"
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 NOTICE  "${pkgdir}/usr/share/licenses/${pkgname}"
}
