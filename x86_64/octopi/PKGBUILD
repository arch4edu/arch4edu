# Maintainer:
# Contributor: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: MatMoul <matmoul at the google email domain which is .com>

: ${_commit_alpm=0ed2a8bd6b869f40683cf7a79727dc64d7da274e}

_pkgname="octopi"
pkgname="$_pkgname"
pkgver=0.19.0
pkgrel=2
pkgdesc="A powerful Pacman frontend using Qt libs"
url="https://github.com/aarnt/octopi"
license=('GPL-2.0-or-later')
arch=('x86_64')

depends=(
  'qt6-base'
  'qt6-multimedia'
  'qt6-svg'
  'qtermwidget'
)
makedepends=(
  'cmake'
  'git'
  'ninja'
  'qt6-5compat'
  'qt6-tools'
  'vala'
)
optdepends=(
  'inxi: for SysInfo log'
  'lsb-release: for SysInfo log'
  'mhwd: for SysInfo log'
  'systemd: for SysInfo log'
  'pacmanlogviewer: to view pacman log files'
  'pacaur: for AUR support'
  'paru: for AUR support'
  'pikaur: for AUR support'
  'trizen: for AUR support'
  'yay: for AUR support'
)

conflicts=('alpm_octopi_utils')

options=('!lto')

_pkgsrc_octopi="$_pkgname-$pkgver"
_pkgsrc_alpm_utils="alpm_octopi_utils"
_pkgext="tar.gz"

source=(
  "$_pkgsrc_octopi.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext"
  "$_pkgsrc_alpm_utils"::"git+https://github.com/aarnt/alpm_octopi_utils.git${_commit_alpm:+#commit=$_commit_alpm}"
)
sha256sums=(
  'bf2f6e2ab6208a020fd34fa6d88eaad5268132c4e38369818fd74267c0c54525'
  '25c8f9ce3f24f5f9bf271c1acbf4935ee3ed1ff12bd66e9f3115b9d40c53bebe'
)

if [ -z "$_commit_alpm" ]; then
  sha256sums[1]='SKIP'
fi

build() {
  local _cmake_common=(
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_INSTALL_PREFIX='/usr'
    -DCMAKE_SKIP_RPATH=ON
    -Wno-author
  )

  echo "Building alpm_utils..."
  local _cmake_alpm=(
    -B build_alpm
    -S "$_pkgsrc_alpm_utils"
  )

  cmake "${_cmake_common[@]}" "${_cmake_alpm[@]}"
  cmake --build build_alpm

  DESTDIR="fakeinstall" cmake --install build_alpm

  echo "Building octopi..."
  local _cmake_octopi=(
    -B build_octopi
    -S "$_pkgsrc_octopi"
    -Dalpm_octopi_utils_DIR="$srcdir/fakeinstall/usr/lib/cmake/alpm_octopi_utils/"
    -DUSE_KF6NOTIFICATIONS=OFF
  )

  cmake "${_cmake_common[@]}" "${_cmake_octopi[@]}"
  cmake --build build_octopi
}

package() {
  depends+=(
    'pacman'
    'pacman-contrib'
    'qt-sudo' # AUR
  )

  DESTDIR="$pkgdir" cmake --install build_octopi

  # library
  install -Dm644 "fakeinstall/usr/lib/libalpm_octopi_utils.so" -t "$pkgdir/usr/lib/"

  # fix svg path
  local _svg_path="usr/share/icons/hicolor/scalable/apps"
  mkdir -pm755 "$pkgdir/$_svg_path"
  mv "$pkgdir/usr/share/icons/hicolor/48x48/apps/octopi.svg" "$pkgdir/$_svg_path/"

  # not needed for standard licenses
  rm -rf "$pkgdir/usr/share/licenses/"
}
