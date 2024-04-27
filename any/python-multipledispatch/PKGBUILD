# Maintainer: Michael Schubert <mschu.dev at gmail> github.com/mschubert/PKGBUILDs
# Contributor: Gaël Donval <gdonval+aur at google mail>
pkgname=python-multipledispatch
pkgver=1.0.0
pkgrel=2
pkgdesc='Multiple dispatch implementation in Python'
arch=('any')
url='https://github.com/mrocklin/multipledispatch'
license=('BSD')
makedepends=('python-setuptools')
depends=('python>=3.4' 'python-six')
source=(multipledispatch-$pkgver.tar.gz::https://github.com/mrocklin/multipledispatch/archive/$pkgver.tar.gz)
sha256sums=('a9eb21390e5051ce28b2ee7acd02bb21885b9e2a4ce6e5fdbb1f338b48b54203')

build() {
  cd "$srcdir"/multipledispatch-$pkgver
  python setup.py build
}

package() {
  cd "$srcdir"/multipledispatch-$pkgver
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
  install -D -m644 LICENSE* "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
  install -D -m644 README* "$pkgdir"/usr/share/doc/$pkgname/README
}
