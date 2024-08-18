# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-libmamba
pkgver=1.5.8
_srcver=2024.03.25
_name=mamba-$_srcver
pkgrel=3
pkgdesc="The fast cross-platform package manager"
arch=('x86_64')
url="https://github.com/mamba-org/mamba"
license=('BSD-3-Clause')
depends=(
  'fmt'
  'libsolv'
  'python>=3.9'
  'reproc'
  'yaml-cpp>=0.8.0'
)
makedepends=(
  # header-only libs
  'cli11'
  'spdlog'
  'tl-expected'
  'nlohmann-json'
  # C++ build tools
  'ccache'
  'cmake>=3.18'
  'doctest'
  'ninja'
  'pybind11'
  # python build tools
  'python-build'
  'python-installer'
  'python-scikit-build>=0.13'
  'python-setuptools>=42'
  'python-wheel'
)
provides=('libmamba')
#options=(!emptydirs)
#backup=(etc/conda/condarc)
source=(
  $_name-$pkgver.tar.gz::$url/archive/refs/tags/$_srcver.tar.gz
)
sha512sums=('93263defae3a5ef0cd4ea16b1a9ac2bcdc63e0091043d6975fb2d4d9b5430eed224a33dcf4336e7967646b80204ce17f1190be31c2ca2b6725d424ee5f5c13bc')

prepare() {
  cd $srcdir/${_name}
}

build() {
  cd $srcdir/${_name}
  cmake -B build/ -G Ninja \
    -D CMAKE_C_COMPILER=gcc -D CMAKE_CXX_COMPILER=g++ \
    -D CMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -D BUILD_LIBMAMBA=ON \
    -D BUILD_LIBMAMBAPY=ON \
    -D BUILD_MICROMAMBA=OFF \
    -D BUILD_MAMBA_PACKAGE=OFF \
    --preset mamba-shared-debug
  cmake --build build/ --parallel

  cd $srcdir/${_name}/libmambapy
  python -m build --wheel --no-isolation
}

package() {
  cd $srcdir/${_name}
  cmake --install build/ --prefix "$pkgdir/usr"

  cd $srcdir/${_name}/libmambapy
  python -m installer --destdir="$pkgdir" dist/*.whl
 
  install -Dm 644 LICENSE $pkgdir/usr/share/licenses/${pkgname}/LICENSE.txt
}
