# Maintainer: Cyril Waechter <cyril[at]biminsight[dot]ch>
pkgname=(ifcopenshell bonsaiviewer)
_pkgver=0.9.0
pkgver=${_pkgver//-/_}
_vername=bonsai
pkgrel=2
pkgdesc="Open source IFC library and geometry engine. Provides static libraries, python3 wrapper and blender addon."
arch=('x86_64')
url="https://ifcopenshell.org/"
license=('LGPL-3.0-or-later' 'GPL-3.0-or-later')
depends=(
  'boost-libs'
  'hdf5'
  'hicolor-icon-theme'
  'libxml2-legacy'
  'mpfr'
  'opencascade'
  # 'opencollada' # dropped from extra
  'python'
  'python-numpy'
  'python-jinja'
  'python-pytz'
  'python-typing_extensions'
  'python-requests'
  'python-platformdirs'

)
makedepends=(
  'blender'
  'boost'
  'cgal'
  'cmake'
  'eigen'
  'git'
  'ninja'
  'nlohmann-json'
  'patchelf'
  'python-babel'
  'python-build'
  'python-installer'
  'python-wheel'
  'qt6-base'
  'qt6-svg'
  'swig'
  'sz'
  'zstd'
)
source=(
  "https://github.com/IfcOpenShell/IfcOpenShell/archive/refs/tags/${_vername}-${_pkgver}.tar.gz"
  "git+https://github.com/svgpp/svgpp.git"
  "bpypolyskel-1.1.3.tar.gz::https://github.com/prochitecture/bpypolyskel/archive/refs/tags/v1.1.3.tar.gz"
  "wgpu-linux-x86_64-release.zip::https://github.com/gfx-rs/wgpu-native/releases/download/v29.0.0.0/wgpu-linux-x86_64-release.zip"

  "001-Skip-installing-Python-source-modules.patch"
  "003-Use-SPDX-license-expressions.patch"
  "004-zstd-shared-target.patch"
  "007-fix-pyradiance-chmod.patch"
  "008-bonsaiviewer-ribbon-toolbar.patch"
  "009-bonsaiviewer-spatial-column-width.patch"
)
sha256sums=('7371c99a983e2f22fc716ffce34ec962ab68987fe66a158c0e2d3581554922d6'
            'SKIP'
            'c774454e31757796cf02078cc04d4f27b6180d718e1edab4148340879a6b64c5'
            'cf614af80f23c6364a13f6569e7ae4ca7367ebf6062e3d3d6e80e205264636b4'
            'cf7c9e904e3a9c9e2d50589c658e05719ca9938c333d81b6646ca10416f2f9ce'
            'eed549dd22dabb63812948b8dd797361ccf37ab25ccf284e03f16ed2b500a268'
            '8b7d6a8364071d49674f029d371c23e2f9ba8366d467df384b7d98c665209b41'
            '32f28c4f31877a871ea1ce182e78e1e84e05030db2ab609b10dd9de48d34f7c7'
            '3ae76ceca299f1d6f30eb87a636d92bc851cca1bf3a770baa6c074fa032a5a92'
            '21501e2ceec0a04968e488a1922b6cc681953c4668ea9dcb8b80313b2e792038')
noextract=("wgpu-linux-x86_64-release.zip")
options=("!lto")

_iosdir="IfcOpenShell-${_vername}-${_pkgver}"

_apply_patch() {
  cd "${srcdir}/${_iosdir}"
  for p in $srcdir/*.patch; do
    msg2 "Applying patch $p"
    patch -p1 -l <$p
  done

}
prepare() {
  mv bpypolyskel-1.1.3 bpypolyskel
  cp -ar svgpp/* ${_iosdir}/src/svgfill/3rdparty/svgpp
  install -d "$srcdir/wgpu-native"
  bsdtar -xf "$srcdir/wgpu-linux-x86_64-release.zip" -C "$srcdir/wgpu-native"
  (
    _apply_patch
  )

}
_build_pymodules() {

  pushd "${srcdir}/${_iosdir}"
  find src -name '*.py' -o -name '*.toml' | xargs sed -i "/version =/s/0.0.0/${_pkgver}/g"
  for _dir in src/*; do
    if [ ! -d ${_dir} ] || [[ ${_dir} == src/ifcsverchok ]]; then
      continue
    fi
    pushd ${_dir}
    if [ -f pyproject.toml ] || [ -f setup.py ]; then
      echo "Building python module in ${_dir}"
      python -m build --wheel --no-isolation
    fi
    popd
  done
  popd
}
build() {
  _build_pymodules
  install -d build

  local CMAKE_ARGS=(
    -S ${_iosdir}/cmake
    -B build
    -G Ninja
    -DEIGEN_DIR=/usr/include/eigen3
    -DOCC_INCLUDE_DIR=/usr/include/opencascade
    -DOCC_LIBRARY_DIR=/usr/lib
    -DHDF5_INCLUDE_DIR=/usr/include
    -DHDF5_LIBRARY_DIR=/usr/lib
    -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2
    -DLIBXML2_LIBRARIES="/usr/lib/libxml2.so.2"
    -DGMP_INCLUDE_DIR=/usr/include
    -DMPFR_INCLUDE_DIR=/usr/include
    -DJSON_INCLUDE_DIR=/usr/include
    # We do not use OpenCOLLADA but we have to include opencascade in  cmake INCLUDE_DIRECTORIES
    -DOPENCOLLADA_INCLUDE_DIRS=/usr/include/opencascade
    -DSWIG_EXECUTABLE="/usr/bin/swig"
    -DCMAKE_INSTALL_PREFIX=/usr
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_C_FLAGS="${CFLAGS} -ffile-prefix-map=$srcdir=."
    -DCMAKE_CXX_FLAGS="${CXXFLAGS} -ffile-prefix-map=$srcdir=."
    -DCMAKE_SKIP_BUILD_RPATH=ON
    -DBUILD_SHARED_LIBS=ON
    -DGLTF_SUPPORT=ON
    -DCOLLADA_SUPPORT=OFF
    -DBUILD_BONSAIVIEWER=ON
    -DFETCHCONTENT_SOURCE_DIR_WGPU_NATIVE="$srcdir/wgpu-native"
    -DIFCOPENSHELL_DEPLOY_QT_RUNTIME=OFF
  )
  cmake "${CMAKE_ARGS[@]}"

  ninja -C build -j 12
}

package_ifcopenshell() {
  pkgdesc="Open source IFC library and geometry engine. Provides static libraries, python3 wrapper and blender addon."
  optdepends=(
    'python-xsdata: bonsaï'
    'python-shapely: bonsaï'
    'python-svgwrite: bonsaï'
    'python-isodate: bonsaï'
    'python-pystache: bonsaï'
    'python-socketio: bonsaï'
    'python-natsort: bonsaï'
    'python-openpyxl: bonsaï'
    'python-odfpy: bonsaï'
    'python-xmlschema: bonsaï, bcf support'
    'python-deepdiff: ifcdiff'
    'python-tzfpy: bonsaï'
    'python-orderly-set: bonsaï'
    'python-gitpython: bonsaï'
    'python-networkx: bonsaï'
    'python-pyradiance: bonsaï'
    'python-aiohttp: bonsaï'
  )
  _blender_ver=$(blender --version | grep -Po 'Blender \K[0-9].[0-9]+')
  _python_ver=$(python --version | grep -Po 'Python \K[0-9].[0-9]+')
  cd "${srcdir}/build"
  DESTDIR="$pkgdir" ninja install
  echo "Installed main libs done"

  # Bonsai Viewer ships in the bonsaiviewer package
  rm -f "$pkgdir/usr/bin/BonsaiViewer" \
        "$pkgdir/usr/bin/IfcViewerMinimal" \
        "$pkgdir/usr/lib/libwgpu_native.so"

  # Install license file
  cd "${srcdir}/${_iosdir}"
  install -Dm644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm644 COPYING.LESSER -t "${pkgdir}/usr/share/licenses/${pkgname}"

  # Install python modules
  find src/*/dist -name '*.whl' -print0 | xargs -0 -I {} python -m installer --destdir="$pkgdir" {}
  echo "Installed python modules done"

  # extra modules that does not build whl
  cp -rf src/{ifc2ca,ifcsverchok} ${pkgdir}/usr/lib/python${_python_ver}/site-packages
  cp -rf "${srcdir}"/build/ifcwrap/{ifcopenshell_wrapper.py,*.so} ${pkgdir}/usr/lib/python${_python_ver}/site-packages/ifcopenshell

  # provides blender extension
  install -d "${pkgdir}/usr/share/blender/${_blender_ver}/extensions/system"
  ln -s /usr/lib/python${_python_ver}/site-packages/${_vername} "${pkgdir}/usr/share/blender/${_blender_ver}/extensions/system/${_vername}"

  # replace the upstream "os-arch" manifest placeholder, mirroring upstream Makefile
  sed -i "s/os-arch/linux-x64/" "${pkgdir}/usr/lib/python${_python_ver}/site-packages/${_vername}/blender_manifest.toml"

  # install desktop and wrappers
  cd "${srcdir}/${_iosdir}/src/${_vername}/${_vername}/libs/desktop"
  install -Dm755 ${_vername} -t ${pkgdir}/usr/bin
  install -Dm644 ${_vername}.png -t ${pkgdir}/usr/share/icons/hicolor/128x128/apps
  install -Dm644 ${_vername}.desktop -t ${pkgdir}/usr/share/applications
  install -Dm644 ${_vername}.xml -t ${pkgdir}/usr/share/mime/packages/
  install -Dm644 x-ifc_128x128.png ${pkgdir}/usr/share/icons/hicolor/128x128/mimetypes/x-ifc.png
  install -Dm644 x-ifc_512x512.png ${pkgdir}/usr/share/icons/hicolor/512x512/mimetypes/x-ifc.png

  # bpypolyskel blender extension
  cp -rf ${srcdir}/bpypolyskel ${pkgdir}/usr/lib/python${_python_ver}/site-packages
  ln -s /usr/lib/python${_python_ver}/site-packages/bpypolyskel "${pkgdir}/usr/share/blender/${_blender_ver}/extensions/system/bpypolyskel"
}

package_bonsaiviewer() {
  pkgdesc="Native Qt6 and WebGPU IFC model viewer (part of IfcOpenShell)"
  depends=('ifcopenshell' 'qt6-base' 'qt6-svg' 'zstd')
  license=('GPL-3.0-or-later')

  install -Dm755 "${srcdir}/build/bonsaiviewer/BonsaiViewer" \
    "$pkgdir/usr/bin/BonsaiViewer"
  install -Dm644 "${srcdir}/wgpu-native/lib/libwgpu_native.so" \
    "$pkgdir/usr/lib/libwgpu_native.so"
  install -Dm644 "${srcdir}/${_iosdir}/COPYING" \
    "$pkgdir/usr/share/licenses/${pkgname}/COPYING"

  # Launcher working around the missing Wayland surface in the wgpu backend
  # (upstream stub, src/ifcviewer/ViewportWindow.cpp) by falling back to the
  # implemented X11/XWayland path. Drop this once upstream supports Wayland.
  install -d "$pkgdir/usr/bin"
  cat > "$pkgdir/usr/bin/bonsaiviewer" <<'EOF'
#!/bin/sh
# The wgpu backend does not implement a Wayland surface yet (upstream stub:
# "Wayland wgpu surface creation not yet wired"). Under a Wayland session,
# use the implemented X11/XWayland path when it is available.
if [ -z "${QT_QPA_PLATFORM:-}" ] && [ -n "${WAYLAND_DISPLAY:-}" ] && [ -n "${DISPLAY:-}" ]; then
    export QT_QPA_PLATFORM=xcb
fi
exec /usr/bin/BonsaiViewer "$@"
EOF
  chmod 755 "$pkgdir/usr/bin/bonsaiviewer"

  # Menu entry + icon. Exec uses the wrapper above so Wayland sessions take the
  # implemented X11/XWayland path. No %F/MimeType: the binary does not accept a
  # file argument yet.
  install -Dm644 "${srcdir}/${_iosdir}/src/bonsaiviewer/docs/_static/bonsaiviewer.svg" \
    "$pkgdir/usr/share/icons/hicolor/scalable/apps/bonsaiviewer.svg"

  install -d "$pkgdir/usr/share/applications"
  cat > "$pkgdir/usr/share/applications/bonsaiviewer.desktop" <<'EOF'
[Desktop Entry]
Type=Application
Name=Bonsai Viewer
GenericName=IFC Model Viewer
Comment=View IFC models
Exec=bonsaiviewer
Icon=bonsaiviewer
Terminal=false
Categories=Graphics;3DGraphics;Engineering;
Keywords=IFC;BIM;viewer;IfcOpenShell;Bonsai;
StartupNotify=true
StartupWMClass=BonsaiViewer
EOF
  chmod 644 "$pkgdir/usr/share/applications/bonsaiviewer.desktop"
}
