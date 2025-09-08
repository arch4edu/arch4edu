# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>

pkgbase=zoom
pkgname=(zoom zoom-libs-bin zoom-libs)
pkgver=6.5.11
_subver=4015
pkgrel=2
pkgdesc="Video Conferencing and Web Conferencing Service"
arch=('x86_64')
license=('LicenseRef-zoom')
url="https://zoom.us/"
makedepends=(patchelf binutils)
options=(!strip emptydirs)
source=("${pkgname}-${pkgver}.${_subver}_orig_x86_64.pkg.tar.xz"::"https://zoom.us/client/${pkgver}.${_subver}/zoom_x86_64.pkg.tar.xz")
sha512sums=('c150fa1469b9f1bec922a2b47a89a9ebab322427303d37936b364c8b21f2f281debbaa265f52458ea8642df16f49790f8d82fbcbb7c7e947a331f8f91a85e302')
noextract=(${source[0]%::*}) # Do not fail makepkg on small BUILDDIR

prepare() {
  tar -tf "${noextract[0]}" --wildcards \
    opt/zoom/Qt opt/zoom/qt.conf opt/zoom/translations opt/zoom/libOpenCL.so* opt/zoom/libmpg123.so* opt/zoom/libquazip.so \
    opt/zoom/libavcodec.so* opt/zoom/libavformat.so* opt/zoom/libavutil.so* opt/zoom/libswresample.so* \
    opt/zoom/cef/libsqlite3.so* opt/zoom/cef/libvulkan.so* \
    > nativelibs.txt
}

package_zoom() {
  depends+=(zoom-libs-bin) # Let upstream libs default
  cd "$pkgdir"
  tar -xf "${srcdir}/${noextract[0]}" -X "${srcdir}/nativelibs.txt" --exclude .*
  # Remove insecure RUNPATH, mod for native libs (should be minimal)
  cd opt/zoom
  for b in zoom zopen Zoom{Launcher,WebviewHost} aomhost libaomagent.so
    do patchelf --remove-rpath $b $(nm -D "$b" | grep -E '(_Z|__cx).*@Qt_5$' | sed 's/@Qt_5.*//;s/^\s*U/--clear-symbol-version/'|tr '\n' ' ')
  done
}

package_zoom-libs-bin() {
  pkgdesc="Official runtimes for Zoom Workspace client"
  depends=('fontconfig' 'glib2' 'libpulse' 'libsm' 'ttf-font' 'libx11' 'libxtst' 'libxcb'
    'libxcomposite' 'libxfixes' 'libxi' 'libxcursor' 'libxkbcommon-x11' 'libxrandr'
    'libxrender' 'libxshmfence' 'libxslt' 'mesa' 'nss' 'xcb-util-image'
    'xcb-util-keysyms' 'xcb-util-cursor' 'dbus' 'libdrm' 'gtk3' 'qt5-webengine' 'qt5-remoteobjects'
  # libcef.so dependencies is missing according to namcap.
  )
  optdepends=(
    'picom: extra compositor needed by some window managers for screen sharing'
    'ibus: remote control'
  )
  bsdtar -xf "${srcdir}/${noextract[0]}" -T nativelibs.txt -C "$pkgdir"
}

package_zoom-libs() {
  pkgdesc="Native runtimes for Zoom Workspace client"
  depends=(ocl-icd mpg123 libxtst sqlite
  quazip-qt5 qt5-{base,graphicaleffects,quickcontrols,quickcontrols2,svg,declarative})
  optdepends=(
    'qt5-webengine: SSO login'
    qt5-{wayland,3d,x11extras,multimedia,imageformats,remoteobjects} ffmpeg
    vulkan-icd-loader
  )
  conflicts=(zoom-libs-bin) 
  provides=(zoom-libs-bin)

  install -d "$pkgdir"/opt/zoom
  ln -sf /usr/lib/libquazip1-qt5.so "$pkgdir"/opt/zoom/libquazip.so
}
