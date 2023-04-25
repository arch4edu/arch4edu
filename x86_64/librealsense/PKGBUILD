# Maintainer: pingplug < aur at pingplug dot me >
# Contributr: Patrick José Pereira < positivcheg94 at gmail dot com >

_commit=23b0904ba126e87327bc2908c1a5f79342eae867  # tags=v2.53.1
_RS4XX_VER=5.14.0.0
_SR300_VER=3.26.1.0
_TM2_VER=0.2.0.951
_L51X_VER=1.5.8.1
_L53X_VER=3.5.5.1

pkgname=librealsense
pkgver=v2.53.1
pkgrel=2
pkgdesc="Intel® RealSense™ SDK 2.0 is a cross-platform library for Intel® RealSense™ depth cameras (D400 series and the SR300) and the T265 tracking camera."
arch=('x86_64')
url="https://github.com/IntelRealSense/librealsense"
license=('Apache')
makedepends=('cmake' 'git')
depends=('glfw-x11' 'gtk3' 'libusb')
source=("git+https://github.com/IntelRealSense/librealsense#commit=${_commit}"
    "https://librealsense.intel.com/Releases/RS4xx/FW/D4XX_FW_Image-${_RS4XX_VER}.bin"
    "https://librealsense.intel.com/Releases/SR300/FW/SR3XX_FW_Image-${_SR300_VER}.bin"
    "https://librealsense.intel.com/Releases/TM2/FW/target/${_TM2_VER}/target-${_TM2_VER}.mvcmd"
    "https://librealsense.intel.com/Releases/L5xx/FW/L51X_FW_Image-${_L51X_VER}.bin"
    "https://librealsense.intel.com/Releases/L5xx/FW/L53X_FW_Image-${_L53X_VER}.bin"
    "realsense-viewer.desktop")
sha256sums=('SKIP'
            'c956a583ee3fcea105c00164eb3a0aad28643f62d54c99ad80724dd7a6c038e8'
            'c4ac2144df13c3a64fca9d16c175595c903e6e45f02f0f238630a223b07c14d1'
            '0265fd111611908b822cdaf4a3fe5b631c50539b2805d2f364c498aa71c007c0'
            '87a9a91b613d9d807b2bfc424abe9cac63cad75dfc04718592c44777cb0b4452'
            'b837b2cff2b270b89eed3c0b212ab4108389a20b6e07c19dd5957918ff9ce7e0'
            '59281f91e7d471a7dde1cf7207eddd8624e05218cc4301ee52e4c453a0c8ab21')

pkgver() {
  cd "${srcdir}/${pkgname}"
  git describe --tags | sed 's/-/+/g'
}

prepare(){
  cd "${srcdir}/${pkgname}"
  sed -i 's|, GROUP:="plugdev"||g' "config/99-realsense-libusb.rules"
  sed -i 's|, GROUP="plugdev"||g' "config/99-realsense-libusb.rules"

  mkdir -p build/common/fw/
  cp "../D4XX_FW_Image-${_RS4XX_VER}.bin" build/common/fw/
  cp "../SR3XX_FW_Image-${_SR300_VER}.bin" build/common/fw/
  cp "../target-${_TM2_VER}.mvcmd" build/common/fw/
  cp "../L51X_FW_Image-${_L51X_VER}.bin" build/common/fw/
  cp "../L53X_FW_Image-${_L53X_VER}.bin" build/common/fw/
}

build() {
  cd "${srcdir}/${pkgname}"
  mkdir -p build && cd build
  CFLAGS="${CFLAGS} -Wformat -pthread" \
  CXXFLAGS="${CXXFLAGS} -Wformat -pthread" \
  unset HOME
  cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_INSTALL_SBINDIR=bin \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=on \
    -DBUILD_WITH_STATIC_CRT=off \
    -DBUILD_WITH_OPENMP=on \
    -DBUILD_EXAMPLES=true \
    -DBUILD_WITH_TM2=true
  make
}

package() {
  cd "${srcdir}/${pkgname}/build"
  DESTDIR="${pkgdir}" make install
  # why install config file to ${HOME} ?
  install -dm755 "${pkgdir}/usr/share"
  mv "${pkgdir}/Documents/librealsense2" "${pkgdir}/usr/share"
  rmdir "${pkgdir}/Documents"
  cd "${srcdir}"
  install -Dm644 realsense-viewer.desktop "${pkgdir}/usr/share/applications/realsense-viewer.desktop"
  cd "${srcdir}/${pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 config/99-realsense-libusb.rules "${pkgdir}/etc/udev/rules.d/99-realsense-libusb.rules"
  install -Dm644 common/res/icon_512.png "${pkgdir}"/usr/share/pixmaps/realsense-viewer.png
}
