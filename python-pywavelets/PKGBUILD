# Contributor: Francois Boulogne <fboulogne at april dot org>
# Maintainer: Francois Boulogne <fboulogne at april dot org>

pkgname=python-pywavelets
_pkgname=pywt
pkgver=0.5.0
pkgrel=1
pkgdesc="Discrete Wavelet Transforms in Python"
arch=('any')
url="https://github.com/PyWavelets/pywt"
license=('MIT')
depends=('python' 'python-numpy')
makedepends=('python-setuptools' 'cython')
source=(https://github.com/PyWavelets/pywt/archive/v$pkgver.tar.gz)
sha256sums=('99157c11df6c8fb37ca159ce644190a0b9d0c62c830f8a0e2dbe948819c093f3')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package(){
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:ts=2:sw=2:et:
