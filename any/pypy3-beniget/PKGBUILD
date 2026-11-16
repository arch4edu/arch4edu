# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=beniget
pkgname=pypy3-${_base}
pkgver=0.5.1
pkgrel=1
pkgdesc="A static analyzer for Python code"
arch=(any)
url="https://github.com/serge-sans-paille/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-gast)
makedepends=(pypy3-setuptools)
source=(https://pypi.io/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('58c0ceb50c83861a3f29e90865597af9a795cfa01dd3f8260af2b6cf01b512a3f95045b0ae439853ffa038fe3b8dd5450583794ee41eb45a94e43a495286a300')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
