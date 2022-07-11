# Maintainer: acxz <akashpatel2008@yahoo.com>
# Contributor: K. Morton <pryre.dev@outlook.com>
# Contributor: Anselmo L. S. Melo <anselmo.melo@intel.com>
pkgname=qgroundcontrol
pkgver=4.2.3
pkgrel=1
pkgdesc="Micro air vehicle ground control station."
arch=('x86_64')
url="https://github.com/mavlink/qgroundcontrol"
license=('GPL3')

# Git commit hash for version-specific submodules
pkgver_gps='6fcf06894973240d45dc49d3b31565917dc8f2f6' # src/GPS/Drivers
pkgver_eigen='0fd6b4f71dd85b2009ee4d1aeb296e2c11fc9d68' # libs/eigen
pkgver_libevents='b3df80adf5e9a1ffd3520a699d751acddd07763c' # libs/libevents/libevents
pkgver_nlohmann='391786c6c3abdd3eeb993a3154f1f2a4cfe137a0' # libs/libevents/libevents/libs/cpp/parse/nlohmann_json
pkgver_mavlink='0b8597ce3ec0f294dcf5e15dbbcd6068ef03eaa2' # libs/mavlink/include/mavlink/v2.0
pkgver_aossl='3aaff1bd9e35047abdb363239bb3e3c114d07ea1' # libs/OpenSSL/android_openssl
pkgver_qengine='bcae73281fd29ab8e7a41fc3246223b15d44d0df' # libs/qmdnsengine
pkgver_gst='9d782fad9dc0384ba86ecae64511c193f6149f93' # libs/qmlglsink/gst-plugins-good
pkgver_xz='090e6a054d6283b144d20f5783852b95eade90ee' # libs/xz-embedded

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

source=("qgroundcontrol-${pkgver}.tar.gz::https://github.com/mavlink/qgroundcontrol/archive/v${pkgver}.tar.gz"
        "gps-drivers-qgc${pkgver}.tar.gz::https://github.com/PX4/GpsDrivers/archive/${pkgver_gps}.tar.gz"
        "eigen-${pkgver}.tar.gz::https://gitlab.com/libeigen/eigen/-/archive/${pkgver_eigen}/eigen-${pkgver_eigen}.tar.gz"
        "libevents-qgc${pkgver}.tar.gz::https://github.com/mavlink/libevents/archive/${pkgver_libevents}.tar.gz"
        "nlohmann-qgc${pkgver}.tar.gz::https://github.com/ArthurSonzogni/nlohmann_json_cmake_fetchcontent/archive/${pkgver_nlohmann}.tar.gz"
        "mavlink-v2.0-qgc${pkgver}.tar.gz::https://github.com/mavlink/c_library_v2/archive/${pkgver_mavlink}.tar.gz"
        "aossl-qgc${pkgver}.tar.gz::https://github.com/Auterion/android_openssl/archive/${pkgver_aossl}.tar.gz"
        "qengine-qgc${pkgver}.tar.gz::https://github.com/patrickelectric/qmdnsengine/archive/${pkgver_qengine}.tar.gz"
        "gst-plugins-good-qgc${pkgver}.tar.gz::https://github.com/GStreamer/gst-plugins-good/archive/${pkgver_gst}.tar.gz"
        "xz-qgc${pkgver}.tar.gz::https://github.com/Auterion/xz-embedded/archive/${pkgver_xz}.tar.gz"
        "gst-volatile.patch::https://patch-diff.githubusercontent.com/raw/mavlink/gst-plugins-good/pull/1.patch"
)

sha256sums=('bafbedc67fda6314108fa1217528ac183739cd7f620de93884791b6624120169'
            '30e7924bf96724e0854dc461df131f24ce2221f4aa22c69e43ace34e2699b2d2'
            '0fa24d921e5ead2d5fe405fff2ac9bb167b155cd767ba42a9f613ddb44d7e4ae'
            'afb3090975a7da881ff0c8577d13777de5703f71859a5cf8b05387f790bc0748'
            '614ffcc9812aa2d2cbe0d602e258c2fe7d06eddd68dec0c51039f3f210a33ac6'
            '56349916eb2707597439db7d37f1700f2d5a1819872b5bb414557e8559a94a67'
            '93598e63fbbd86fec5e15f2596bba8b1f1654c854a99222099516933fd22a118'
            'e709edd7142cfc738e306808b588a8836d9d795856d6d3cd57bd5ac8666516a6'
            'd5aad13c8eff7f3cce75c8cf3bbf6ac592ac82455e666dccd17cf006deec3e55'
            '7a6d606198c94c0c84a18c690bcfdf0fc5ba1a3f61a9c8ebc2c51523f0884084'
            'SKIP'
)

prepare() {
  gpsdir="PX4-GPSDrivers-${pkgver_gps}"
  eigendir="eigen-${pkgver_eigen}"
  libeventsdir="libevents-${pkgver_libevents}"
  nlohmanndir="nlohmann_json_cmake_fetchcontent-${pkgver_nlohmann}"
  mavlinkdir="c_library_v2-${pkgver_mavlink}"
  aossldir="android_openssl-${pkgver_aossl}"
  qenginedir="qmdnsengine-${pkgver_qengine}"
  gstdir="gst-plugins-good-${pkgver_gst}"
  xzdir="xz-embedded-${pkgver_xz}"

  # Copy in the GPS source
  rm -r "${srcdir}/${pkgname}-${pkgver}/src/GPS/Drivers"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/src/GPS"
  cp -R "${srcdir}/${gpsdir}" "${srcdir}/${pkgname}-${pkgver}/src/GPS/Drivers"

  # Copy in the eigen source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/eigen"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs"
  cp -R "${srcdir}/${eigendir}" "${srcdir}/${pkgname}-${pkgver}/libs/eigen"

  # Copy in the libevents source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/libevents/libevents"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs/libevents"
  cp -R "${srcdir}/${libeventsdir}" "${srcdir}/${pkgname}-${pkgver}/libs/libevents/libevents"

  # Copy in the nlohmann source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/libevents/libevents/libs/cpp/parse/nlohmann_json"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs/libevents/libevents/libs/cpp/parse"
  cp -R "${srcdir}/${nlohmanndir}" "${srcdir}/${pkgname}-${pkgver}/libs/libevents/libevents/libs/cpp/parse/nlohmann_json"

  # Copy in the mavlink source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/mavlink/include/mavlink/v2.0"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs/mavlink/include/mavlink"
  cp -R "${srcdir}/${mavlinkdir}" "${srcdir}/${pkgname}-${pkgver}/libs/mavlink/include/mavlink/v2.0"

  # Copy in the android openssl source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/OpenSSL/android_openssl"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs/OpenSSL"
  cp -R "${srcdir}/${aossldir}" "${srcdir}/${pkgname}-${pkgver}/libs/OpenSSL/android_openssl"

  # Copy in the qmdnsengine source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/qmdnsengine"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs"
  cp -R "${srcdir}/${qenginedir}" "${srcdir}/${pkgname}-${pkgver}/libs/qmdnsengine"

  # Copy in the GST source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/qmlglsink/gst-plugins-good"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs"
  cp -R "${srcdir}/${gstdir}" "${srcdir}/${pkgname}-${pkgver}/libs/qmlglsink/gst-plugins-good"

  # Copy in the xz source
  rm -r "${srcdir}/${pkgname}-${pkgver}/libs/xz-embedded"
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/libs"
  cp -R "${srcdir}/${xzdir}" "${srcdir}/${pkgname}-${pkgver}/libs/xz-embedded"

  cd "${srcdir}/${pkgname}-${pkgver}/libs/qmlglsink/gst-plugins-good"
  patch --strip=1 < "${srcdir}/gst-volatile.patch"
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
