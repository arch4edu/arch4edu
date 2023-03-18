# Maintainer: acxz <akashpatel2008@yahoo.com>
# Contributor: K. Morton <pryre.dev@outlook.com>
# Contributor: Anselmo L. S. Melo <anselmo.melo@intel.com>
pkgname=qgroundcontrol
pkgver=4.2.5
pkgrel=1
pkgdesc="Micro air vehicle ground control station."
arch=('x86_64')
url="https://github.com/mavlink/qgroundcontrol"
license=('GPL3')

depends=('bzip2'
         'dbus'
         'flac'
         'gst-plugins-base-libs'
         'libasyncns'
         'libffi'
         'libgcrypt'
         'libgpg-error'
         'libogg'
         'libsndfile'
         'libsystemd'
         'libunwind'
         'libx11'
         'libxau'
         'libxcb'
         'libxdmcp'
         'libxext'
         'lz4'
         'orc'
         'pcre'
         'sdl2'
         'xz'
         'zlib'
         'icu'
         'qt5-speech'
         'qt5-multimedia'
         'qt5-serialport'
         'qt5-charts'
         'qt5-quickcontrols'
         'qt5-quickcontrols2'
         'qt5-location'
         'qt5-svg'
         'qt5-graphicaleffects'
         'qt5-tools'
         'qt5-wayland'
         'qt5-x11extras'
)

makedepends=('git' 'qt5-base' 'patchelf')

source=("${pkgname}-${pkgver}::git+https://github.com/mavlink/qgroundcontrol.git#tag=v${pkgver}"
        "${pkgname}-GpsDrivers::git+https://github.com/PX4/GpsDrivers.git"
        "${pkgname}-c_library_v2::git+https://github.com/mavlink/c_library_v2.git"
        "${pkgname}-android_openssl::git+https://github.com/Auterion/android_openssl.git"
        "${pkgname}-gst-plugins-good::git+https://github.com/mavlink/gst-plugins-good.git"
        "${pkgname}-xz-embedded::git+https://github.com/Auterion/xz-embedded.git"
        "${pkgname}-libevents::git+https://github.com/mavlink/libevents.git"
        "${pkgname}-eigen::git+https://gitlab.com/libeigen/eigen.git"
        "${pkgname}-qmdnsengine::git+https://github.com/patrickelectric/qmdnsengine.git"
)

sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
)

prepare() {
  cd "$srcdir/${pkgname}-${pkgver}"

  git submodule init

  git config submodule."src/GPS/Drivers".url "${srcdir}/${pkgname}"-GpsDrivers
  git config submodule."libs/mavlink/include/mavlink/v2.0".url "${srcdir}/${pkgname}"-c_library_v2
  git config submodule."libs/OpenSSL/android_openssl".url "${srcdir}/${pkgname}"-android_openssl
  git config submodule."libs/qmlglsink/gst-plugins-good".url "${srcdir}/${pkgname}"-gst-plugins-good
  git config submodule."libs/xz-embedded".url "${srcdir}/${pkgname}"-xz-embedded
  git config submodule."libs/libevents/libevents".url "${srcdir}/${pkgname}"-libevents
  git config submodule."libs/eigen".url "${srcdir}/${pkgname}"-eigen
  git config submodule."libs/qmdnsengine".url "${srcdir}/${pkgname}"-qmdnsengine

  git -c protocol.file.allow=always submodule update --init --recursive
}

build() {
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/build"
  cd "$srcdir/${pkgname}-${pkgver}/build"
  qmake ..
  make
}

package() {
  mkdir -p "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/applications"
  cp -r "${srcdir}/${pkgname}-${pkgver}/build/staging" "${pkgdir}/opt/${pkgname}"
  cp "${srcdir}/${pkgname}-${pkgver}/resources/icons/qgroundcontrol.png" "${pkgdir}/opt/${pkgname}"
  cp "${srcdir}/${pkgname}-${pkgver}/deploy/qgroundcontrol-start.sh" "${pkgdir}/opt/${pkgname}"

  # Use our own desktop file and remove the default one

  echo "[Desktop Entry]
Type=Application
Name=QGroundControl Release
Comment=Ground control for unmanned vehicles
Path=/opt/${pkgname}/
Exec=/usr/bin/${pkgname}
Icon=/opt/${pkgname}/qgroundcontrol.png
Terminal=false
Categories=Qt;Utility;" > "$srcdir/${pkgname}.desktop"

  rm "${pkgdir}/opt/${pkgname}/${pkgname}.desktop"
  cp "${srcdir}/${pkgname}.desktop" "${pkgdir}/opt/${pkgname}"

  ln -s "/opt/${pkgname}/QGroundControl" "${pkgdir}/usr/bin/${pkgname}"
  ln -s "/opt/${pkgname}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}

# vim:set ts=2 sw=2 et:
