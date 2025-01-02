# Maintainer:
# Contributor: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: MatMoul <matmoul at the google email domain which is .com>

_pkgname="octopi"
pkgname="$_pkgname"
pkgver=0.16.2
pkgrel=2
pkgdesc="A powerful Pacman frontend using Qt libs"
url="https://github.com/aarnt/octopi"
license=('GPL-2.0-or-later')
arch=('x86_64')

depends=(
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
  'pacaur: for AUR support'
  'pacmanlogviewer: to view pacman log files'
  'paru: for AUR support'
  'pikaur: for AUR support'
  'systemd: for SysInfo log'
  'trizen: for AUR support'
  'yay: for AUR support'
)

conflicts=('alpm_octopi_utils')

_pkgsrc_octopi="$_pkgname-$pkgver"
_pkgsrc_alpm_utils="alpm_octopi_utils"
_pkgext="tar.gz"
source=(
  "$_pkgsrc_octopi.$_pkgext"::"https://github.com/aarnt/octopi/archive/refs/tags/v$pkgver.$_pkgext"
  "$_pkgsrc_alpm_utils"::"git+https://github.com/aarnt/alpm_octopi_utils.git"
)
sha256sums=(
  '7a10e68c0eba817d3c5917a392034c9d92dd975f4f2eaf9343b3ae35701e2c93'
  'SKIP'
)

prepare() {
  cd "$_pkgsrc_octopi"

  # Don't hardcode qt-sudo path
  sed -i 's/usr\/local/usr/g' src/constants.h
}

_build_alpm_utils() (
  local _cmake_options=(
    -B build_alpm
    -S "$_pkgsrc_alpm_utils"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_INSTALL_PREFIX='/usr'
    -Wno-dev
  )

  cmake "${_cmake_options[@]}"
  cmake --build build_alpm

  DESTDIR="fakeinstall" cmake --install build_alpm
)

_build_octopi() (
  local _cmake_options=(
    -B build_octopi
    -S "$_pkgsrc_octopi"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_INSTALL_PREFIX='/usr'
    -Dalpm_octopi_utils_DIR="'$srcdir/fakeinstall/usr/lib/cmake/alpm_octopi_utils/'"
    -Wno-dev
  )

  cmake "${_cmake_options[@]}"
  cmake --build build_octopi

  DESTDIR="fakeinstall" cmake --install build_octopi
)

build() {
  _build_alpm_utils
  _build_octopi
}

package() {
  depends+=(
    'pacman'
    'pacman-contrib'
    'qt-sudo' # AUR
  )

  rm -rf "fakeinstall/usr/include/"
  rm -rf "fakeinstall/usr/lib/cmake/"
  rm -rf "fakeinstall/usr/lib/pkgconfig/"
  rm -rf "fakeinstall/usr/share/licenses/"
  rm -rf "fakeinstall/usr/share/vala/"

  cp --reflink=auto -a fakeinstall/* "$pkgdir/"
  chmod -R u+rwX,go+rX,go-w "$pkgdir/"
}
