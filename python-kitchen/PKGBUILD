#Maintainer: John Jenkins twodopeshaggy@gmail.com
#Maintainer: Sean Anderson seanga2@gmail.com

pkgname=python-kitchen
pkgver=1.2.5
pkgrel=2
pkgdesc="Useful snippets of python code"
url="https://github.com/fedora-infra/kitchen"
depends=('python' )
makedepends=('python' 'python-setuptools')
conflicts=('python3-kitchen')
license=('LGPLv2+')
arch=('any')
source=(https://github.com/fedora-infra/kitchen/archive/v$pkgver.tar.gz)
md5sums=('35490785ed23c91bad1c083c7adbc39e')

build() {
    cd $srcdir/kitchen-$pkgver
    python setup.py build
}

package() {
    cd $srcdir/kitchen-$pkgver
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
