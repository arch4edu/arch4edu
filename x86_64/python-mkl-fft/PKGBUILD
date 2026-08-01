# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=python-mkl-fft
_pkgname=mkl_fft
pkgver=2.3.1
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL FFT functionality"
arch=('x86_64')
url="https://github.com/IntelPython/mkl_fft"
license=('BSD-2-Clause')
depends=('intel-oneapi-mkl' 'python-numpy')
makedepends=('meson' 'ninja' 'cython' 'python-numpy' 'cmake' 'git'
             'python-build' 'python-installer' 'meson-python')
source=("git+$url#tag=${pkgver}")
md5sums=('SKIP')

prepare() {
  cd "$srcdir/${_pkgname}"
  # Remove pip-only build deps; we use system MKL, cmake, and ninja
  sed -i '/"mkl-devel"/d; /"cmake"/d; /"ninja"/d' pyproject.toml
}

build() {
  cd "$srcdir/${_pkgname}"
  export CMAKE_PREFIX_PATH=/opt/intel/oneapi/mkl/latest/lib/cmake/mkl
  export MKLROOT=/opt/intel/oneapi/mkl/latest
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/${_pkgname}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
