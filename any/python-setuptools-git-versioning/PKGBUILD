_snake=setuptools_git_versioning
pkgname=python-setuptools-git-versioning
pkgver=2.1.0
pkgrel=2
pkgdesc='Use Git repo data for building a version number according to PEP 440.'
url='https://github.com/dolfinus/setuptools-git-versioning'
arch=('any')
license=('MIT')
depends=('python' 'python-setuptools')
makedepends=('python-build' 'python-installer' 'python-wheel')
provides=("$pkgname")
conflicts=("$pkgname")
source=("https://pypi.io/packages/source/s/$_snake/$_snake-$pkgver.tar.gz")
sha256sums=('6aef5b8bb1cfb953b6b343d27cbfc561d96cf2a2ee23c2e0dd3591042a059921')

build() {
  cd "$srcdir/$_snake-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/$_snake-$pkgver"
  python -m installer "--destdir=$pkgdir" "./dist/"*".whl"
  install -Dm644 "./LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
