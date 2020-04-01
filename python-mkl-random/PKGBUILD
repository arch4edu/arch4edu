# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=python-mkl-random
_pkgname=mkl_random
pkgver=1.1.0
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL Random Number Generation functionality"
arch=('x86_64')
url="https://github.com/IntelPython/mkl_random"
license=('custom')
depends=('intel-mkl' 'python-numpy')
makedepends=('cython' 'git' 'intel-compiler-base' 'python-numpy' 'python-setuptools')
source=("git+$url#tag=v${pkgver}")
md5sums=('SKIP')

build() {
  cd "$srcdir/${_pkgname}"
  python setup.py build
}

package_python-mkl-random() {
  cd "$srcdir/${_pkgname}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
