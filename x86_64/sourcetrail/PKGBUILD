# Maintainer:
# Contributor: Javier Tiá <javier dot tia at gmail dot com>

# options
: ${_ver_clang=}
: ${_ver_jdk:=21}

: ${_install_path:=usr/lib}

: ${_commit:=59503c7449e9557fa43490f2fa8a0183d05480a2} # 2025.4.1

_pkgname="sourcetrail"
pkgname="$_pkgname"
pkgver=2025.4.1
pkgrel=1
pkgdesc='Interactive source explorer for C/C++ and Java'
url='https://github.com/xiota/sourcetrail'
license=('GPL-3.0-only')
arch=('x86_64')

depends=(
  "clang${_ver_clang:-}"
  "llvm${_ver_clang:-}-libs"

  'libboost_chrono.so'          # boost-libs
  'libboost_filesystem.so'      # boost-libs
  'libboost_program_options.so' # boost-libs
  'libboost_thread.so'          # boost-libs
  'qt6-5compat'
  'qt6-base'
  'qt6-svg'
  'sqlite'
  'tinyxml'
)
makedepends=(
  "java-environment=${_ver_jdk:?}"
  "lld${_ver_clang:-}"
  "llvm${_ver_clang:-}"

  'boost'
  'cmake'
  'git'
  'maven'
  'ninja'

  'imagemagick'
  'patchelf'
)
optdepends=(
  'java-runtime'
)

_source_main() {
  _pkgsrc="$_pkgname"
  source=("$_pkgsrc"::"git+$url.git#commit=$_commit")
  sha256sums=('SKIP')
}

_source_main

prepare() {
  magick "$_pkgsrc/bin/app/data/gui/icon/logo_1024_1024.png" -resize 256x256 "$_pkgname.png"

  # prevent failure from checkVersionRange
  sed 's/FATAL_ERROR/WARNING/' -i "$_pkgsrc"/cmake/Sourcetrail.cmake
}

build() (
  export CC=clang
  export CXX=clang++

  local _ldflags=($LDFLAGS)
  export LDFLAGS="${_ldflags[@]//*fuse-ld*/} -fuse-ld=lld"

  export PATH="/usr/lib/llvm${_ver_clang:-}/bin:$PATH"
  export LD_LIBRARY_PATH="/usr/lib/llvm${_ver_clang:-}/lib"

  export Clang_DIR="/usr/lib/llvm${_ver_clang:-}/cmake/clang"
  export LLVM_DIR="/usr/lib/llvm${_ver_clang:-}/cmake/llvm"

  export JAVA_HOME="/usr/lib/jvm/java-${_ver_jdk}-openjdk"

  local _cmake_options=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DBUILD_CXX_LANGUAGE_PACKAGE=ON
    -DBUILD_JAVA_LANGUAGE_PACKAGE=ON
    -DBUILD_PYTHON_LANGUAGE_PACKAGE=ON
    -DBUILD_UNIT_TESTS_PACKAGE=OFF
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    -DCMAKE_VERBOSE_MAKEFILE=OFF
    -Wno-dev
  )

  cmake "${_cmake_options[@]}"
  cmake --build build
)

package() {
  # binaries
  install -Dm755 "build/app/Sourcetrail" "$pkgdir/$_install_path/$_pkgname/$_pkgname"
  patchelf --add-rpath '$ORIGIN' "$pkgdir/$_install_path/$_pkgname/$_pkgname"

  install -Dm755 "build/app/sourcetrail_indexer" -t "$pkgdir/$_install_path/$_pkgname/"
  patchelf --add-rpath '$ORIGIN' "$pkgdir/$_install_path/$_pkgname"/sourcetrail_indexer

  # data
  local _path="$pkgdir/$_install_path/$_pkgname"
  install -dm755 "$_path"
  cp --reflink=auto -a "$_pkgsrc/bin/app"/{data,user} "$_path/"
  cp --reflink=auto -a "build/app/data"/{cxx,java} "$_path/data/"

  # icon
  install -Dm644 "$_pkgname.png" "$pkgdir/usr/share/pixmaps/$_pkgname.png"

  # launcher
  install -Dm644 /dev/stdin "$pkgdir/usr/share/applications/$_pkgname.desktop" << END
[Desktop Entry]
Type=Application
Name=${_pkgname^}
Comment=$pkgdesc
Exec=$_pkgname
Icon=$_pkgname
Terminal=false
StartupNotify=true
StartupWMClass=Sourcetrail
MimeType=application/x-sourcetrail;
Categories=Development;
END

  # script
  install -Dm755 /dev/stdin "$pkgdir/usr/bin/$_pkgname" << END
#!/usr/bin/env bash
SOURCETRAIL_PATH=/$_install_path/$_pkgname

export QT_XKB_CONFIG_ROOT="/usr/share/X11/xkb:\$QT_XKB_CONFIG_ROOT"
export QT_QPA_FONTDIR="\$SOURCETRAIL_PATH/data/fonts:\$QT_QPA_FONTDIR"
export SOURCETRAIL_VIA_SCRIPT=1
export OPENSSL_CONF=/etc/ssl/

exec \$SOURCETRAIL_PATH/$_pkgname "\$@"
END

  # permissions
  chmod -R u+rwX,go+rX,go-w "$pkgdir/"
}
