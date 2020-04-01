# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=python-mkl-fft
_pkgname=mkl_fft
pkgver=1.0.14
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL FFT functionality"
arch=('x86_64')
url="https://github.com/IntelPython/mkl_fft"
license=('custom')
depends=('intel-mkl')
makedepends=('cython' 'git' 'intel-compiler-base' 'python-numpy' 'python-setuptools')
source=("git+$url#tag=v${pkgver}")
md5sums=('SKIP')

build() {
  cd "$srcdir/${_pkgname}"
  python setup.py build
}

package_python-mkl-fft() {
  depends+=('python-numpy')
  cd "$srcdir/${_pkgname}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
