# Maintainer: Michael Schubert <mschu.dev at gmail> github.com/mschubert/PKGBUILDs
# Contributor: Gaël Donval <gdonval+aur at google mail>
pkgname=python-multipledispatch
pkgver=0.6.0
pkgrel=3
pkgdesc='Multiple dispatch implementation in Python'
arch=('any')
url='https://github.com/mrocklin/multipledispatch'
license=('BSD')
makedepends=('python-setuptools')
depends=('python>=3.4' 'python-six')
source=("https://github.com/mrocklin/multipledispatch/archive/$pkgver.tar.gz")
sha256sums=('649f6e61b8a6ce581c75f32365c926b55495c01b8177135408b83aa03886cde0')

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
