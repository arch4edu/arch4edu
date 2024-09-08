# Maintainer: Brian Thompson <brianrobt@pm.me>
# Contributor: Daniel Maslowski <info@orangecms.org>
# Contributor: Ke Liu <specter119@gmail.com>

pkgname=python-libmamba
pkgver=1.5.9
_srcver=2024.08.31
_name=mamba-$_srcver
pkgrel=1
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
sha512sums=('7b3b8891acae69bd7fa62b304c8d91fcb02bc6c653e7d25d4cc73b97fa1ed4bf85aa21a71dbb5fd608b233eb9647665f5bd0c956fc430e769b151a7e424cedd2')

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
