# Maintainer: Josip Ponjavic <josipponjavic at gmail dot com>

pkgbase=python-pycryptodome
pkgname=('python-pycryptodome' 'python2-pycryptodome')
_name=pycryptodome
pkgver=3.6.0
pkgrel=1
license=('BSD')
arch=('x86_64')
url='http://www.pycryptodome.org/'
makedepends=('gmp' 'python-setuptools' 'python2-setuptools')
source=("${_name}-${pkgver}.tar.gz::https://github.com/Legrandin/${_name}/archive/v${pkgver}.tar.gz")
sha256sums=('14184ec53a736d59321008b132997f5dcf4eb48883f35a4d307ef33b5a0c4bfa')
sha512sums=('2212cc088e72fcd76ae9e4bdbbff4eebaaed6f874b374d6bcbbf87071b9397e871ccc2caa5a007314bb3291288e46185376dc0462016218cde0993bea5b01256')

prepare() {
  cp -a "pycryptodome-$pkgver"{,-python2}
}

build() {
  cd "$srcdir/pycryptodome-$pkgver"
  python setup.py build

  cd "$srcdir/pycryptodome-$pkgver-python2"
  python2 setup.py build
}

check() {
  cd "$srcdir/pycryptodome-$pkgver"
  python setup.py test

  cd "$srcdir/pycryptodome-$pkgver-python2"
  python2 setup.py test
}

package_python-pycryptodome() {
  pkgdesc="Collection of cryptographic algorithms and protocols, implemented for use from Python 3."
  depends=('python' 'gmp')
  conflicts=('python-crypto')
  provides=('python-crypto')

  cd "pycryptodome-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE.rst "$pkgdir/usr/share/licenses/$pkgname/LICENSE.rst"
}

package_python2-pycryptodome() {
  pkgdesc="Collection of cryptographic algorithms and protocols, implemented for use from Python 2."
  depends=('python2' 'gmp')
  conflicts=('python2-crypto')
  provides=('python2-crypto')

  cd "pycryptodome-$pkgver-python2"
  python2 setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE.rst "$pkgdir/usr/share/licenses/$pkgname/LICENSE.rst"
}
