# Maintainer: Brian Thompson <brianrobt@pm.me>
# Contributor: Daniel Maslowski <info@orangecms.org>
# Contributor: Ke Liu <specter119@gmail.com>

pkgname=python-libmamba
pkgver=2.0.5
_srcver=2024.12.12
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
  'simdjson'
)
makedepends=(
  # header-only libs
  'cli11'
  'spdlog'
  'tl-expected'
  'nlohmann-json'
  # C++ build tools
  'ccache'
  'python-cmake>=3.18'
  'doctest'
  'python-ninja'
  'pybind11'
  # python build tools
  'python-build'
  'python-installer'
  'python-scikit-build>=0.13'
  'python-setuptools>=42'
  'python-wheel'
)
provides=("libmamba=$pkgver" "python-libmambapy=$pkgver")
conflicts=('micromamba')
#options=(!emptydirs)
#backup=(etc/conda/condarc)
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/$_srcver.tar.gz")
sha512sums=('57c139f40e0b769d3d6028c4690f66ac7eda74fbdab1683fe8396eb94301c140858096a7511b792a360dd07dd984847734561e37a21c198c9c896d849fcad6e7')

build() {
  cd "$srcdir/$_name"

  cmake -S. -Bbuild \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DBUILD_LIBMAMBA=ON \
    -DBUILD_LIBMAMBAPY=ON \
    -DBUILD_MICROMAMBA=OFF \
    -DBUILD_MAMBA_PACKAGE=OFF \
    -DBUILD_SHARED=ON
  cmake --build build --parallel 8
  cmake --install build --prefix install

  cd libmambapy
  export SKBUILD_CONFIGURE_OPTIONS="\
      -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
      -DBUILD_LIBMAMBA=ON \
      -DBUILD_LIBMAMBAPY=ON \
      -DBUILD_MICROMAMBA=OFF \
      -DBUILD_MAMBA_PACKAGE=OFF \
      -Dlibmamba_ROOT=$PWD/../install"
  python -m build -x --wheel --no-isolation
}

package() {
  cd "$srcdir/$_name"
  cmake --install build/ --prefix "$pkgdir/usr"

  cd "$srcdir/$_name/libmambapy"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm 644 LICENSE $pkgdir/usr/share/licenses/${pkgname}/LICENSE.txt
}
