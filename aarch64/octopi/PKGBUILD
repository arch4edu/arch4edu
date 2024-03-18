# Maintainer: MatMoul <matmoul at the google email domain which is .com>

_githubuser=aarnt
_githubrepo=octopi
_pkgtagname=v0.15.0

pkgname=octopi
pkgver=0.15.0
pkgrel=2
pkgdesc='This is Octopi, a powerful Pacman frontend using Qt libs'
arch=('any')
url="https://tintaescura.com/projects/octopi/"
license=('GPL2')
depends=('alpm_octopi_utils' 'qtermwidget' 'sudo')
makedepends=('qt5-tools')
optdepends=('octopi-notifier-qt5: Notifier for Octopi using Qt5 libs'
            'octopi-notifier-frameworks: Notifier for Octopi with Knotifications support'
            'pacaur: for AUR support'
            'paru: for AUR support'
            'pikaur: for AUR support'
            'trizen: for AUR support'
            'yay: for AUR support'
            'pacmanlogviewer: to view pacman log files')
provides=('octopi' 'octopi-repoeditor' 'octopi-cachecleaner')
source=("${_githubrepo}::https://github.com/${_githubuser}/${_githubrepo}/archive/refs/tags/${_pkgtagname}.tar.gz")
sha256sums=('e94525d906d6ab4f5fc594cf1a267668ae5f1fa7f32e449ddfa84328dd738f30')

_subdirs=(helper repoeditor cachecleaner sudo)

prepare() {
	cd "${_githubrepo}-${pkgver}"
	cp resources/images/octopi_green.png resources/images/octopi.png
}

build() {
	cd "${_githubrepo}-${pkgver}"
	echo "Starting build..."
	qmake-qt5 PREFIX=/usr QMAKE_CFLAGS="${CFLAGS}" QMAKE_CXXFLAGS="${CXXFLAGS}" QMAKE_LFLAGS="${LDFLAGS}" octopi.pro
	make
	for _subdir in ${_subdirs[@]}; do
		pushd $_subdir
		echo "Building octopi-$_subdir..."
		qmake-qt5 PREFIX=/usr QMAKE_CFLAGS="${CFLAGS}" QMAKE_CXXFLAGS="${CXXFLAGS}" QMAKE_LFLAGS="${LDFLAGS}" "octopi-$_subdir.pro"
		make
		popd
	done
}

package() {
	cd "${_githubrepo}-${pkgver}"
	make INSTALL_ROOT="${pkgdir}" install
	for _subdir in ${_subdirs[@]}; do
		pushd $_subdir
		make INSTALL_ROOT="${pkgdir}" install
		popd
	done
}
