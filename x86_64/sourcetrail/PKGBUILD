# Maintainer:
# Contributor: Javier Tiá <javier dot tia at gmail dot com>

# options
#: ${_pkgtype:=git}
: ${_clang_version:=15}

# basic info
_pkgname=sourcetrail
pkgname="$_pkgname${_pkgtype:+-$_pkgtype}"
pkgver=2023.11
pkgrel=2
pkgdesc='Interactive source explorer for C/C++ and Java'
url='https://github.com/petermost/Sourcetrail'
license=('GPL3')
arch=('x86_64')

# main package
_main_package() {
  depends=(
    "clang${_clang_version:?}"
    "llvm${_clang_version:?}-libs"

    'boost-libs'
    'java-runtime'
    'qt5-svg'
    'sqlite'
    'tinyxml'
  )
  makedepends=(
    "llvm${_clang_version:?}"

    'boost'
    'catch2'
    'cmake'
    'jdk-openjdk'
    'maven'
    'ninja'
    'qt5-base'

    'gendesk'
    'imagemagick'

    # AUR
    #'vcpkg'
  )

  if [ x"$pkgname" == x"$_pkgname" ] ; then
    _main_stable
  else
    _main_git
  fi
}

# stable package
_main_stable() {
  _pkgsrc="Sourcetrail-${pkgver%%.r*}"
  _pkgext="tar.gz"
  source+=(
    "$_pkgname-${pkgver%%.r*}.$_pkgext"::"$url/archive/refs/tags/${pkgver%%r.*}.tar.gz"
  )
  sha256sums+=(
    'SKIP'
  )

  pkgver() {
    local _pkgver="${pkgver%%.r*}"
    echo "${_pkgver:?}"
  }
}

# git package
_main_git() {
  makedepends+=('git')

  provides=("$_pkgname=${pkgver%%.r*}")
  conflicts=("$_pkgname")

  _pkgsrc="$_pkgname"
  source+=("$_pkgsrc"::"git+$url.git")
  sha256sums+=('SKIP')

  pkgver() (
    cd "$_pkgsrc"
    git describe --long --tags --exclude='*[a-zA-Z][a-zA-Z]*' \
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

  convert "${_pkgsrc:?}/bin/app/data/gui/icon/logo_1024_1024.png" -resize 256x256 "$_pkgname.png"
}

build() {
  export Clang_DIR="/usr/lib/llvm${_clang_version:?}/lib/cmake/clang/"

  local _cmake_options=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE="Release"
    -DCMAKE_INSTALL_PREFIX='/usr'
    -DBUILD_TESTING="OFF"

    -DBUILD_CXX_LANGUAGE_PACKAGE="ON"
    -DBUILD_JAVA_LANGUAGE_PACKAGE="ON"
    -DCMAKE_EXPORT_COMPILE_COMMANDS="TRUE"
    -DCMAKE_VERBOSE_MAKEFILE="TRUE"

    #--preset system-ninja-release
    -Wno-dev
  )

  cmake "${_cmake_options[@]}"
  cmake --build build
}

package() {
  # binaries
  install -Dm755 "build/app/Sourcetrail" "${pkgdir:?}/opt/$_pkgname/bin/$_pkgname"
  install -Dm755 "build/app/sourcetrail_indexer" -t "${pkgdir:?}/opt/$_pkgname/bin/"

  # scripts
  install -Dm755 "${_pkgsrc:?}/setup/Linux/data/package/resetPreferences.sh" -t "${pkgdir:?}/opt/$_pkgname/"
  install -Dm755 "${_pkgsrc:?}/setup/Linux/data/package/Sourcetrail.sh" -t "${pkgdir:?}/opt/$_pkgname/"

  # symlink
  install -dm755 "${pkgdir:?}/usr/bin"
  ln -s "/opt/$_pkgname/Sourcetrail.sh" "${pkgdir:?}/usr/bin/$_pkgname"

  # icon
  install -Dm644 "$_pkgname.png" "${pkgdir:?}/usr/share/pixmaps/$_pkgname.png"

  # desktop file
  install -Dm644 "${srcdir:?}/$_pkgname.desktop" -t "${pkgdir:?}/usr/share/applications/"

  # share/data
  install -dm755 "${pkgdir:?}/opt/$_pkgname/share/data"
  cp -r "${_pkgsrc:?}/bin/app/data/color_schemes" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/cxx" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/fallback" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/fonts" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/gui" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/install" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/java" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/license" "${pkgdir:?}/opt/$_pkgname/share/data/"
  cp -r "${_pkgsrc:?}/bin/app/data/syntax_highlighting_rules" "${pkgdir:?}/opt/$_pkgname/share/data/"
}

# execute
_main_package
