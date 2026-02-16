# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=python-mkl-fft
_pkgname=mkl_fft
pkgver=2.1.2
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL FFT functionality"
arch=('x86_64')
url="https://github.com/IntelPython/mkl_fft"
license=('custom')
depends=('intel-mkl' 'python-numpy')
makedepends=('cython' 'git' 'python-setuptools')
source=("git+$url#tag=${pkgver}")
md5sums=('f8953fde609b8ac42ec45ac989b484f9')

build() {
  cd "$srcdir/${_pkgname}"
  python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
