# Maintainer: Wil Thomason <wbthomason@cs.cornell.edu>
# Former maintainer: Sven Schneider <archlinux.sandmann@googlemail.com>

pkgname=ompl
pkgver=1.4.2
pkgrel=3
pkgdesc="The Open Motion Planning Library (OMPL) consists of many state-of-the-art sampling-based motion planning algorithms"
arch=('i686' 'x86_64')
url="http://ompl.kavrakilab.org/"
license=('BSD')
conflicts=('ros-melodic-ompl' 'ompl-git')
replaces=('ros-melodic-ompl' 'ompl-git')
depends=('boost-libs' 'python' 'python-matplotlib')
makedepends=('boost' 'cmake')
optdepends=('py++: Python binding'
            'ode: Plan using the Open Dynamics Engine'
            'eigen: For an informed sampling technique')
source=(https://github.com/ompl/ompl/archive/${pkgver}.tar.gz "boost-fix.patch")
sha512sums=(67cd99ee80b2c74a35eb54ce1ed4faf19fafc58843d9a9eaf29d28ef0707623517ccf9571af4af094455309950ea8f38d56f5c04d963f5e7a2410a7638e6e5fa
5f61e2a4410b8bfd77eb90c85a600c46c201a770957c4cd815e37c8ccd5ae033e9d453d3e1a38d4f0c227e93024ba5c1c1ea86e5d50c6614a83f66705f90b64a)

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  patch -uN demos/PlannerData.cpp ../../boost-fix.patch || return 1

  rm -rf build
  mkdir build
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DPYTHON_EXEC=/usr/bin/python \
    -DCMAKE_CXX_FLAGS=-D_POSIX_VERSION \
    -DOMPL_REGISTRATION=Off ..
  make
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make test
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  cd build
  make DESTDIR=${pkgdir} install
}
