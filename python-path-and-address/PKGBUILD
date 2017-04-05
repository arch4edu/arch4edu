# Maintainer: Mikkel Oscar Lyderik <mikkeloscar at gmail dot com>
# Contributer: XZS <d dot f dot fischer at web dot de>

_gitname=path-and-address

pkgver=2.0.1
pkgname=python-$_gitname
pkgrel=1
pkgdesc="Functions for server CLI applications used by humans."
arch=('any')
url="https://github.com/joeyespo/path-and-address"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
options=(!emptydirs)
source=("https://github.com/joeyespo/$_gitname/archive/v${pkgver}.tar.gz")
md5sums=('bddf6c075c6a28c1c2ad9d8ab089ee30')

package() {
  cd "$srcdir/$_gitname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}
