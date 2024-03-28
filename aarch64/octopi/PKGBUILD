# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: MatMoul <matmoul at the google email domain which is .com>
pkgbase=octopi
pkgname=('octopi'
#         'octopi-notifier-qt5'
#         'octopi-notifier-frameworks'
)
pkgbase=octopi
pkgver=0.15.0
pkgrel=4
arch=('x86_64')
url="https://tintaescura.com/projects/octopi"
license=('GPL-2.0-or-later')
depends=('alpm-octopi-utils' 'qtermwidget')
#makedepends=('qt5-tools' 'knotifications5')
makedepends=('qt5-tools')
source=("${pkgbase}-${pkgver}.tar.gz::https://github.com/aarnt/octopi/archive/v${pkgver}.tar.gz")
sha256sums=('e94525d906d6ab4f5fc594cf1a267668ae5f1fa7f32e449ddfa84328dd738f30')

_subdirs=(
  helper
#  notifier
#  notifier-frameworks
  repoeditor
  cachecleaner
  sudo
)

prepare() {
  cd "${pkgbase}-${pkgver}"

  # copy notifier folder for building both qt5 & kstatus notifier backends
#  cp -rf notifier notifier-qt5
#  cp -rf notifier notifier-frameworks

  # enable building the kstatus alpm backend for notifier-frameworks
#  sed -i 's|#KSTATUS|KSTATUS|' "notifier-frameworks/${pkgbase}-notifier.pro"

  # why doesn't upstream just do this so we don't have to...
  cp -f "resources/images/${pkgbase}_green.png" "resources/images/${pkgbase}.png"
}

build() {
  cd "${pkgbase}-${pkgver}"
  qmake-qt5 \
    PREFIX=/usr \
    QMAKE_CFLAGS="${CFLAGS}" \
    QMAKE_CXXFLAGS="${CXXFLAGS}" \
    QMAKE_LFLAGS="${LDFLAGS}"
  make

  for _subdir in ${_subdirs[@]}; do
    pushd ${_subdir}
    qmake-qt5 \
    PREFIX=/usr \
    QMAKE_CFLAGS="${CFLAGS}" \
    QMAKE_CXXFLAGS="${CXXFLAGS}" \
    QMAKE_LFLAGS="${LDFLAGS}"
    make
    popd
  done
}

package_octopi() {
  pkgdesc="A powerful Pacman frontend using Qt libs"
  optdepends=('octopi-notifier-qt5: Notifier for Octopi using Qt5 libs'
              'octopi-notifier-frameworks: Notifier for Octopi with Knotifications support'
              'pacaur: for AUR support'
              'paru: for AUR support'
              'pikaur: for AUR support'
              'trizen: for AUR support'
              'yay: for AUR support'
              'pacmanlogviewer: to view pacman log files'
              'opendoas: privilege elevation'
              'sudo: privilege elevation')
  provides=('octopi-repoeditor' 'octopi-cachecleaner')

  cd "${pkgbase}-${pkgver}"
  make INSTALL_ROOT="${pkgdir}" install

  for folder in helper repoeditor cachecleaner sudo; do
    make -C ${folder} INSTALL_ROOT="${pkgdir}" install
  done
}

#package_octopi-notifier-qt5() {
#  pkgdesc="Notifier for Octopi using Qt5 libs"
#  depends=('octopi')
#  provides=('octopi-notifier')
#  conflicts=('octopi-notifier')
#  replaces=('octopi-qt5-notifier' 'octopi-notifier-qt4')

#  cd "${pkgbase}-${pkgver}"
#  make -C notifier INSTALL_ROOT="${pkgdir}" install
#}

#package_octopi-notifier-frameworks() {
#  pkgdesc="Notifier for Octopi with Knotifications support"
#  depends=('octopi' 'knotifications5')
#  provides=('octopi-notifier')
#  conflicts=('octopi-notifier')

#  cd "${pkgbase}-${pkgver}"
#  make -C notifier-frameworks INSTALL_ROOT="${pkgdir}" install
#}
