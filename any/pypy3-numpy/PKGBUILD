# Maintainer: Maks Verver <maks@verver.ch>

pkgname=pypy3-numpy
pkgver=2.3.2
pkgrel=1
pkgdesc="Scientific tools for Python"
arch=('x86_64')
license=('custom')
url="https://www.numpy.org/"
depends=('cblas' 'lapack' 'pypy3')
optdepends=('blas-openblas: faster linear algebra')
makedepends=('pypy3-build' 'pypy3-cython' 'pypy3-installer' 'meson-pypy3' 'cmake' 'gcc-fortran')
source=("https://github.com/numpy/numpy/releases/download/v$pkgver/numpy-$pkgver.tar.gz")
md5sums=('f8d3d3b3ecd2b6e98889e88f6bbdc1a3')
sha256sums=('e0486a11ec30cdecb53f184d496d1c6a20786c81e55e41640270130056f8ee48')

build() {
  cd numpy-$pkgver
  CYTHON=/opt/pypy3/bin/cython \
  CFLAGS+=" -ffat-lto-objects" \
  CXXFLAGS+=" -ffat-lto-objects" \
  pypy3 -m build --wheel --no-isolation --skip-dependency-check \
    -Csetup-args="-Dblas=cblas" \
    -Csetup-args="-Dlapack=lapack"
}

package() {
  cd numpy-$pkgver
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl

  # Symlink license file
  local site_packages=$(pypy3 -c "import site; print(site.getsitepackages()[0])")
  install -d "$pkgdir"/usr/share/licenses/$pkgname
  ln -s "$site_packages"/numpy-$pkgver.dist-info/LICENSE.txt \
    "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt

  # Symlink f2py
  mkdir -p "$pkgdir"/usr/bin
  ln -s /opt/pypy3/bin/f2py "$pkgdir"/usr/bin/f2py-pypy3
}
