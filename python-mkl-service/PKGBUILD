# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=python-mkl-service
_pkgname=mkl-service
pkgver=2.3.0
pkgrel=1
pkgdesc="Python hooks for Intel(R) Math Kernel Library runtime control settings."
arch=('x86_64')
url="https://github.com/IntelPython/mkl-service"
license=('custom')
depends=('intel-mkl' 'python-numpy')
makedepends=('cython' 'git' 'intel-compiler-base' 'python-setuptools')
source=("git+$url#tag=v${pkgver}")
md5sums=('SKIP')

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
