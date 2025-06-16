# Maintainer: Maks Verver <maks@verver.ch>

pkgname=pypy3-numpy
pkgver=2.3.0
pkgrel=1
pkgdesc="Scientific tools for Python"
arch=('x86_64')
license=('custom')
url="https://www.numpy.org/"
depends=('cblas' 'lapack' 'pypy3')
optdepends=('blas-openblas: faster linear algebra')
makedepends=('pypy3-build' 'pypy3-cython' 'pypy3-installer' 'meson-pypy3' 'cmake' 'gcc-fortran')
source=("https://github.com/numpy/numpy/releases/download/v$pkgver/numpy-$pkgver.tar.gz")
md5sums=('19a5470a37d066bd3e9385918d7760e7')
sha256sums=('581f87f9e9e9db2cba2141400e160e9dd644ee248788d6f90636eeb8fd9260a6')

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
