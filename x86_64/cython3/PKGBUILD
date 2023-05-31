# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Igor Scabini <furester @ gmail.com>

pkgname=cython3
pkgver=3.0.0b3
pkgrel=1
pkgdesc="C-Extensions for Python"
arch=(x86_64)
url="https://cython.org"
license=(APACHE)
depends=('python')
makedepends=(python-setuptools)
provides=('cython')
conflicts=('cython')
source=($pkgname-$pkgver.tar.gz::"https://github.com/cython/cython/archive/$pkgver.tar.gz")
sha256sums=('06fb018a0c380cf247d8be2ec4ae1f06978ea905bbecafd9efd67744b7b7a97e')

build() {
  cd "cython-$pkgver"
  python setup.py build
}

package() {
  cd "cython-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
