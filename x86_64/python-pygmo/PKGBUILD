# Maintainer: acxz <akashpatel2008 at yahoo dot com>; fanyujun <dlutfyj at outlook dot com>

pkgname=python-pygmo
pkgver=2.19.7
pkgrel=1
pkgdesc="Perform parallel computations of optimisation tasks (global and local) via the asynchronous generalized island model (Python version)"
arch=('i686' 'x86_64')
url="https://esa.github.io/pygmo2/"
license=('GPLv3')
depends=('python' 'boost' 'pagmo' 'python-numpy' 'python-cloudpickle')
optdepends=('python-matplotlib' 'python-dill')
makedepends=('cmake' 'python' 'pybind11' 'pagmo' 'boost')
_name=pygmo2
source=(https://github.com/esa/${_name}/archive/v${pkgver}.tar.gz)
sha256sums=('cfc49bb5b4ec9e96287895db9dcb322122f14c397ec466091aa635dbb31a5c9f')

_buildtype="Release"

build() {

    cd "${srcdir}/${_name}-${pkgver}"

    msg "Starting CMake (build type: ${_buildtype})"

    # Create a build directory
    mkdir -p "${srcdir}/${_name}-${pkgver}-build"
    cd "${srcdir}/${_name}-${pkgver}-build"

    cmake \
        -DCMAKE_BUILD_TYPE="${buildtype}" \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        "${srcdir}/${_name}-${pkgver}"

    msg "Building the project"
    make
}

package() {
    cd "${srcdir}/${_name}-${pkgver}-build"

    msg "Installing files"
    make DESTDIR="${pkgdir}/" install
}
