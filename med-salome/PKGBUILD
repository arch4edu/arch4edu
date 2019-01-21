# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Michele Mocciola <mickele>
# Contributor: Brice Méalier <mealier_brice@yahoo.fr>
# Contributor: Philippe Miron <tuxication@gmail.com>
# Modified by: César Vecchio <cesar UNDERSTRIKE vecchio AT yahoo DOT com>
# Modified by: Martin Ortbauer <mortbauer@gmail.com>
     
pkgname=med-salome
_pkgname=med
pkgver=3.3.1
pkgrel=1
pkgdesc="MED stands for Modelisation et Echanges de Donnees, i.e. Data Modelization and Exchanges - This version is built to be linked against salome-med on x86_64"
url="http://www.code-aster.org/outils/med/"
license=('LGPL')
depends=('hdf5_18' 'python2')
makedepends=('gcc-fortran' 'coreutils' 'swig')
optdepends=('tk')
provides=("med=$pkgver")
conflicts=("med_fichier" "med")
replaces=("med_fichier" "med")
arch=('i686' 'x86_64')
source=("http://files.salome-platform.org/Salome/other/$_pkgname-$pkgver.tar.gz")
sha256sums=('dd631ef813838bc7413ff0dd6461d7a0d725bcfababdf772ece67610a8d22588')

prepare() {
    mkdir -p build

    sed -i '/CODE/s,${CMAKE_INSTALL_PREFIX},\\$ENV{DESTDIR}&,' $_pkgname-${pkgver}_SRC/config/cmake_files/medMacros.cmake
    sed -i '/CODE/s,${DESTDIR},\\$ENV{DESTDIR},' $_pkgname-${pkgver}_SRC/tools/mdump/CMakeLists.txt
}

build() {
    cd build

    cmake ../$_pkgname-${pkgver}_SRC \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DHDF5_NO_FIND_PACKAGE_CONFIG_FILE=ON \
        -DHDF5_C_COMPILER_EXECUTABLE=/usr/bin/h5cc_18 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DMEDFILE_BUILD_PYTHON=ON \
        -DMEDFILE_BUILD_TESTS=OFF

    make
}

package() {
    cd build

    make DESTDIR="$pkgdir" install
}
