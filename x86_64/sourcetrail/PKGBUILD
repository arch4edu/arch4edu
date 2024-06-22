# Maintainer:
# Contributor: Javier Tiá <javier dot tia at gmail dot com>

# options
: ${_build_git:=false}

unset _pkgtype
[[ "${_build_git::1}" == "t" ]] && _pkgtype+="-git"

# basic info
_pkgname=sourcetrail
pkgname="$_pkgname${_pkgtype:-}"
pkgver=2024.6.1
pkgrel=1
pkgdesc='Interactive source explorer for C/C++ and Java'
url='https://github.com/xiota/sourcetrail'
license=('GPL-3.0-only')
arch=('x86_64')

# main package
_main_package() {
  depends=(
    "clang"
    "llvm-libs"

    'boost-libs'
    'java-runtime'
    'qt6-5compat'
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
    'qt6-base'

    'gendesk'
    'imagemagick'
    'patchelf'
  )

  if [ "${_build_git::1}" != "t" ]; then
    _main_stable
  else
    _main_git
  fi
}

# stable package
_main_stable() {
  _commit='6a9036068d79175cafe3ba35a647a40fc3aefb4e'

  _pkgsrc="$_pkgname"
  source=("$_pkgsrc"::"git+$url.git#commit=$_commit")
  sha256sums=('SKIP')

  pkgver() {
    local _pkgver="${pkgver%%.r*}"
    echo "${_pkgver:?}"
  }
}

# git package
_main_git() {
  provides=("$_pkgname=${pkgver%%.r*}")
  conflicts=("$_pkgname")

  _pkgsrc="$_pkgname"
  source=("$_pkgsrc"::"git+$url.git")
  sha256sums=('SKIP')

  pkgver() (
    cd "$_pkgsrc"
    git describe --long --tags --abbrev=7 --exclude='*[a-zA-Z][a-zA-Z]*' \
      | sed -E 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
  )
}

# common functions
prepare() {
  local _gendesk_options=(
    -q -f -n
    --pkgname="${_pkgname}"
    --pkgdesc="$pkgdesc"
    --name="Sourcetrail"
    --exec="${_pkgname}"
    --categories="Development"
    --startupnotify=true
    --mimetypes="application/x-sourcetrail"
  )

  gendesk "${_gendesk_options[@]}"

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
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    -DCMAKE_VERBOSE_MAKEFILE=OFF
    -Wno-dev
  )

  cmake "${_cmake_options[@]}"
  cmake --build build
}

package() {
  # binaries
  install -Dm755 "build/app/sourcetrail_indexer" -t "$pkgdir/opt/$_pkgname/"
  install -Dm755 "build/app/Sourcetrail" "$pkgdir/opt/$_pkgname/$_pkgname"
  patchelf --add-rpath '/opt/sourcetrail' "$pkgdir/opt/$_pkgname/$_pkgname"

  # script
  install -Dm755 /dev/stdin "$pkgdir/usr/bin/$_pkgname" << END
#!/usr/bin/env sh
SOURCETRAIL_PATH=/opt/$_pkgname

export QT_XKB_CONFIG_ROOT="/usr/share/X11/xkb:\$QT_XKB_CONFIG_ROOT"
export QT_QPA_FONTDIR="\$SOURCETRAIL_PATH/data/fonts:\$QT_QPA_FONTDIR"
export SOURCETRAIL_VIA_SCRIPT=1
export OPENSSL_CONF=/etc/ssl/

exec \$SOURCETRAIL_PATH/$_pkgname "\$@"
END

  # icon
  install -Dm644 "$_pkgname.png" "$pkgdir/usr/share/pixmaps/$_pkgname.png"

  # desktop file
  install -Dm644 "$srcdir/$_pkgname.desktop" -t "$pkgdir/usr/share/applications/"

  # data
  install -dm755 "$pkgdir/opt/$_pkgname/data"
  cp -a "$_pkgsrc/bin/app/data/color_schemes" "$pkgdir/opt/$_pkgname/data/"
  cp -a "$_pkgsrc/bin/app/data/fallback" "$pkgdir/opt/$_pkgname/data/"
  cp -a "$_pkgsrc/bin/app/data/fonts" "$pkgdir/opt/$_pkgname/data/"
  cp -a "$_pkgsrc/bin/app/data/gui" "$pkgdir/opt/$_pkgname/data/"
  cp -a "$_pkgsrc/bin/app/data/java" "$pkgdir/opt/$_pkgname/data/"
  cp -a "$_pkgsrc/bin/app/data/license" "$pkgdir/opt/$_pkgname/data/"
  cp -a "$_pkgsrc/bin/app/data/syntax_highlighting_rules" "$pkgdir/opt/$_pkgname/data/"

  cp -a "build/app/data/cxx" "$pkgdir/opt/$_pkgname/data/"

  # user
  install -dm755 "$pkgdir/opt/$_pkgname/user"
  cp -a "$_pkgsrc"/bin/app/user/* "$pkgdir/opt/$_pkgname/user/"

  # fix permissions
  chmod -R u+rwX,go+rX,go-w "$pkgdir/"
}

# execute
_main_package
