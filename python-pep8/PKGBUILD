# Maintainer: Tim Rakowski <tim.rakowski@gmail.com>
pkgname=python-pep8
pkgver=1.7.1
pkgrel=1
pkgdesc="The final release of the pep8 package"
arch=('any')
url="https://github.com/PyCQA/pycodestyle"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
options=(!emptydirs)
source=("$pkgname-$pkgver.tar.gz::https://github.com/PyCQA/pycodestyle/archive/1.7.1.tar.gz")
md5sums=('29968b9f5563d32f5946fbefe7086ee0')

package() {
  cd "$srcdir/pycodestyle-1.7.1"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
