# Maintainer:  a.kudelin <kudelin at protonmail dot com>
# Contributor: vsilv <vsilv@posteo.eu>

_pkgname=quandl
pkgname=python-$_pkgname
pkgver=3.7.0
pkgrel=1
pkgdesc="Quandl's Python Package"
arch=('any')
url="https://github.com/quandl/quandl-python"
license=('MIT')
depends=('python-numpy' 'python-more-itertools' 'python-inflection')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('038c820f813bae12a0a3169cdca40d2a77e1c0b7103b3fa70dc0f620fe036cc3')

build() {
  cd "$srcdir/$_pkgname-python-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-python-$pkgver"
  python setup.py install --prefix=/usr --root="$pkgdir" -O1 --skip-build
  install -Dm755 LICENSE.txt -t \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
