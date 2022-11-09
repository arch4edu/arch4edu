# Maintainer: alienzj <alienchuj@gmail.com>
# Co-maintainer: PumpkinCheshire <me at pumpkincheshire dot com>

pkgname=python-pygraphviz
_name=pygraphviz
pkgver=1.9
pkgrel=2
pkgdesc="Python interface to Graphviz graph drawing package"
arch=('i686' 'x86_64')
url="https://pygraphviz.github.io/"
license=('BSD')
depends=(
  'python'
  'graphviz')
makedepends=(
  'python-build'
  'python-installer'
  'python-wheel'
  'python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.zip")
b2sums=('a399742ae5e8323eec0b6890858cc9158c2942c4f0adb8c74fbfb9745321ae013b93227540e5c328f5dd22d8fba2cf9217a9079f99a14feb983d7188e07084c9')

build() {
  cd "$srcdir/$_name-$pkgver"
  # python setup.py build
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/$_name-$pkgver"

  # python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build

  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/${pkgname}/LICENSE.txt"
  mv "$pkgdir/usr/share/doc/$_name-$pkgver" "$pkgdir/usr/share/doc/$pkgname-$pkgver"

}

# vim:set ts=2 sw=2 et:
