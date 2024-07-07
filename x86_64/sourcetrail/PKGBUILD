# Maintainer:
# Contributor: Javier Tiá <javier dot tia at gmail dot com>

# options
: ${_commit:=929d9dc65a5a62dc77486db6b52ae47cef6f7602} # 2024.7.3.r23

: ${_install_path:=usr/lib}

# basic info
_pkgname="sourcetrail"
pkgname="$_pkgname"
pkgver=2024.7.3
pkgrel=2
pkgdesc='Interactive source explorer for C/C++ and Java'
url='https://github.com/xiota/sourcetrail'
license=('GPL-3.0-only')
arch=('x86_64')

depends=(
  "clang"
  "llvm-libs"
  'boost-libs'
  'qt6-5compat'
  'qt6-base'
  'qt6-svg'
  'sqlite'
  'tinyxml'
)
makedepends=(
  "llvm"
  "lld"

  'boost'
  'cmake'
  'git'
  'jdk-openjdk'
  'maven'
  'ninja'

  'imagemagick'
  'patchelf'
)
optdepends=(
  'java-runtime'
  'python'
)

_pkgsrc="$_pkgname"
source=("$_pkgsrc"::"git+$url.git#commit=$_commit")
sha256sums=('SKIP')

prepare() {
  magick "$_pkgsrc/bin/app/data/gui/icon/logo_1024_1024.png" -resize 256x256 "$_pkgname.png"
}

build() {
  export CC=clang
  export CXX=clang++
  export LDFLAGS+=" -fuse-ld=lld"

  #export Clang_DIR="/usr/lib/cmake/clang"
  #export LLVM_DIR="/usr/lib/cmake/llvm"

  local _cmake_options=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE="Release"
    -DCMAKE_INSTALL_PREFIX='/usr'

    -DBUILD_CXX_LANGUAGE_PACKAGE=ON
    -DBUILD_JAVA_LANGUAGE_PACKAGE=ON
    -DBUILD_PYTHON_LANGUAGE_PACKAGE=ON
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    -DCMAKE_VERBOSE_MAKEFILE=OFF
    -Wno-dev
  )

  cmake "${_cmake_options[@]}"
  cmake --build build
}

package() {
  # binaries
  install -Dm755 "build/app/sourcetrail_indexer" -t "$pkgdir/$_install_path/$_pkgname/"
  install -Dm755 "build/app/Sourcetrail" "$pkgdir/$_install_path/$_pkgname/$_pkgname"
  patchelf --add-rpath "/$_install_path/sourcetrail" "$pkgdir/$_install_path/$_pkgname/$_pkgname"

  # data
  local _data_path="$pkgdir/$_install_path/$_pkgname/data"
  install -dm755 "$_data_path"
  for i in color_schemes fallback fonts gui java license syntax_highlighting_rules; do
    cp -a "$_pkgsrc/bin/app/data/$i" "$_data_path/"
  done

  # languages
  for i in cxx java python; do
    cp -a "build/app/data/$i" "$_data_path/"
  done

  # examples
  cp -a "$_pkgsrc"/bin/app/user/projects "$_data_path/fallback/"

  # icon
  install -Dm644 "$_pkgname.png" "$pkgdir/usr/share/pixmaps/$_pkgname.png"

  # desktop file
  install -Dm644 /dev/stdin "$pkgdir/usr/share/applications/$_pkgname.desktop" << END
[Desktop Entry]
Type=Application
Name=${_pkgname^}
Comment=$pkgdesc
Exec=$_pkgname
Icon=$_pkgname
Terminal=false
StartupNotify=true
Categories=Development;
MimeType=application/x-sourcetrail;
END

  # script
  install -Dm755 /dev/stdin "$pkgdir/usr/bin/$_pkgname" << END
#!/usr/bin/env bash
: \${XDG_CONFIG_HOME:=\$HOME/.config}

SOURCETRAIL_PATH=/$_install_path/$_pkgname
CONFIG_PATH="\$XDG_CONFIG_HOME/Sourcetrail"

if [ ! -e "\$CONFIG_PATH" ]; then
  mkdir -p "\$CONFIG_PATH"
  cp --reflink=auto -r "\$SOURCETRAIL_PATH/data/fallback"/* "\$CONFIG_PATH/"
fi

export QT_XKB_CONFIG_ROOT="/usr/share/X11/xkb:\$QT_XKB_CONFIG_ROOT"
export QT_QPA_FONTDIR="\$SOURCETRAIL_PATH/data/fonts:\$QT_QPA_FONTDIR"
export SOURCETRAIL_VIA_SCRIPT=1
export OPENSSL_CONF=/etc/ssl/

exec \$SOURCETRAIL_PATH/$_pkgname "\$@"
END

  # fix permissions
  chmod -R u+rwX,go+rX,go-w "$pkgdir/"
}
