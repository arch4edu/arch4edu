# Maintainer: Amos Onn <amosonn at gmail dot com>
pkgname=python-zict
pkgver=0.1.3
pkgrel=2
pkgdesc="A python library for Mutable Mapping interfaces."
arch=('any')
url="http://zict.readthedocs.io/en/stable/"
license=('BSD-3-clause')
makedepends=('python-setuptools')
depends=('python>=3.5' 'python-heapdict')
source=("zict-$pkgver.tar.gz::https://codeload.github.com/dask/zict/tar.gz/$pkgver")
sha256sums=('06117907a5aa29f1d37dc6fe719c4cc2c3845002cc4ba507f9376c4a7a1cdc59')
package() {
  cd $srcdir/zict-$pkgver
  python setup.py install --root=$pkgdir || return 1
  install -d $pkgdir/usr/share/licenses/$pkgname
  install LICENSE.txt $pkgdir/usr/share/licenses/$pkgname/COPYING
}
