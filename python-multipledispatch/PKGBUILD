# Maintainer: Gaël Donval <gdonval+aur at google mail>
# Contributor: Gaël Donval <gdonval+aur at google mail>

pkgbase='python-multipledispatch'
pkgname=('python-multipledispatch')
pkgver=0.6.0
pkgrel=1
pkgdesc='Multiple dispatch implementation in Python'
arch=('any')
url='https://github.com/mrocklin/multipledispatch'
license=('BSD')
makedepends=('python-setuptools')
depends=('python>=3.4')
source=("https://github.com/mrocklin/multipledispatch/archive/$pkgver.tar.gz")
sha1sums=('c09f2e533dc7e3954e9587d1ea62967d980b1a33')
md5sums=('f91173ac478c03d46d4e4731b4f13e93')

build() {
  cd "${srcdir}"/multipledispatch-$pkgver
  python setup.py build
}

package_python-multipledispatch() {
  cd "${srcdir}"/multipledispatch-$pkgver
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
  install -D -m644 LICENSE* "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -D -m644 README* "${pkgdir}/usr/share/doc/${pkgname}/README"
}
