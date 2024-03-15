# Maintainer:
# Contributor: Javier Tiá <javier dot tia at gmail dot com>

# options
: ${_clang_version:=14}

: ${_build_git:=false}

unset _pkgtype
[[ "${_build_git::1}" == "t" ]] && _pkgtype+="-git"

# basic info
_pkgname=sourcetrail
pkgname="$_pkgname${_pkgtype:-}"
pkgver=2023.11
pkgrel=3
pkgdesc='Interactive source explorer for C/C++ and Java'
url='https://github.com/petermost/Sourcetrail'
license=('GPL-3.0-only')
arch=('x86_64')

# main package
_main_package() {
  depends=(
    "clang${_clang_version:-}"
    "llvm${_clang_version:-}-libs"

    'boost-libs'
    'java-runtime'
    'qt5-svg'
    'sqlite'
    'tinyxml'
  )
  makedepends=(
    "llvm${_clang_version:-}"
    "lld"

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

  if [ "${_build_git::1}" != "t" ] ; then
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
    '73c783ed6bffd8be0a706e9417ba03937687fd368992e22c5f7a2e72e2ece806'
  )

  _prepare() {
    cd "$_pkgsrc"
    local src
    for src in "${source[@]}"; do
      src="${src%%::*}"
      src="${src##*/}"
      src="${src%.zst}"
      [[ $src = *.patch ]] || continue
      echo
      echo "Applying patch $src..."
      filterdiff -p1 -x 'vcpkg' "../$src" | patch -Np1 -F100
    done
  }

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

  _prepare() {
    :
  }

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

  convert "$_pkgsrc/bin/app/data/gui/icon/logo_1024_1024.png" -resize 256x256 "$_pkgname.png"

  _prepare
}

build() {
  if [ -n "${_clang_version}" ] ; then
    export CC="/usr/lib/llvm${_clang_version:-}/bin/clang"
    export CXX="/usr/lib/llvm${_clang_version:-}/bin/clang++"
    export LDFLAGS+=" -fuse-ld=lld"

    export Clang_DIR="/usr/lib/llvm${_clang_version:-}/lib/cmake/clang"
    export LLVM_DIR="/usr/lib/llvm${_clang_version:-}/lib/cmake/llvm"
  else
    export CC=clang
    export CXX=clang++
    export LDFLAGS+=" -fuse-ld=lld"

    #export Clang_DIR="/usr/lib/cmake/clang"
    #export LLVM_DIR="/usr/lib/cmake/llvm"
  fi

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
  install -Dm755 "build/app/Sourcetrail" "$pkgdir/opt/$_pkgname/bin/$_pkgname"
  install -Dm755 "build/app/sourcetrail_indexer" -t "$pkgdir/opt/$_pkgname/bin/"

  # scripts
  install -Dm755 "$_pkgsrc/setup/Linux/data/package/resetPreferences.sh" -t "$pkgdir/opt/$_pkgname/"
  install -Dm755 "$_pkgsrc/setup/Linux/data/package/Sourcetrail.sh" -t "$pkgdir/opt/$_pkgname/"

  # symlink
  install -dm755 "$pkgdir/usr/bin"
  ln -s "/opt/$_pkgname/Sourcetrail.sh" "$pkgdir/usr/bin/$_pkgname"

  # icon
  install -Dm644 "$_pkgname.png" "$pkgdir/usr/share/pixmaps/$_pkgname.png"

  # desktop file
  install -Dm644 "$srcdir/$_pkgname.desktop" -t "$pkgdir/usr/share/applications/"

  # share/data
  install -dm755 "$pkgdir/opt/$_pkgname/share/data"
  cp -r "$_pkgsrc/bin/app/data/color_schemes" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/cxx" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/fallback" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/fonts" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/gui" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/install" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/java" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/license" "$pkgdir/opt/$_pkgname/share/data/"
  cp -r "$_pkgsrc/bin/app/data/syntax_highlighting_rules" "$pkgdir/opt/$_pkgname/share/data/"
}

# execute
_main_package
