# Maintainer: Guilhem Saurel <guilhem.saurel@laas.fr>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: Benjamin Chretien <chretien dot b +aur at gmail dot com>

pkgname=casadi
pkgver=3.8.0
pkgrel=1
pkgdesc="Symbolic framework for automatic differentiation and numeric optimization"
arch=('i686' 'x86_64')
url="https://github.com/${pkgname}/${pkgname}"
license=('LGPL-3.0-only')
depends=('python' 'gcc-fortran' 'lapack' 'tinyxml' 'tinyxml2' 'swig' 'ipython'
         'python-numpy' 'python-scipy' 'python-matplotlib' 'coin-or-ipopt' 'dsdp'
         'osqp' 'proxsuite' 'coin-or-qpoases')
makedepends=('cmake' 'eigen' 'simde' 'python-setuptools')
source=("${pkgname}-${pkgver}.tar.gz"::"${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c1daf1d4400f094ee775a792b1820deb8c8ca92b2db7d66c0d1005f86cce92dd')

build() {
    cmake -B "build-$pkgver" -S "$pkgbase-$pkgver" \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DFORTRAN_REQUIRED=ON \
        -DWITH_PYTHON=ON \
        -DINSTALL_INTERNAL_HEADERS=ON \
        -DENABLE_EXPORT_ALL=ON \
        -DWITH_OPENMP=ON \
        -DWITH_THREAD=ON \
        -DWITH_BUILD_REQUIRED=OFF \
        -DWITH_SUNDIALS=OFF \
        -DWITH_OSQP=ON \
        -DWITH_PROXQP=ON \
        -DWITH_BUILD_TINYXML=OFF \
        -DWITH_QPOASES=ON \
        -DWITH_LAPACK=ON \
        -DWITH_BUILD_LAPACK=OFF \
        -DWITH_IPOPT=ON \
        -DWITH_TINYXML=ON \
        -DWITH_BUILD_TINYXML=OFF \
        -DWITH_DSDP=ON \
        -DWITH_BUILD_DSDP=OFF \
        -Wno-dev
    cmake --build "build-$pkgver"
}

package() {
    DESTDIR="$pkgdir/" cmake --install "build-$pkgver"
    install -Dm644 "$pkgbase-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
