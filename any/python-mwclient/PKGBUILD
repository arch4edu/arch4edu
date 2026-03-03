# Maintainer: Simon Legner <Simon.Legner@gmail.com>
pkgname='python-mwclient'
pkgdesc="A Python framework to interface with the MediaWiki API"
pkgver=0.11.0
pkgrel=1
arch=('any')
url="https://github.com/mwclient/mwclient"
license=('MIT')
depends=('python' 'python-requests-oauthlib')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
checkdepends=('python-pytest' 'python-pytest-cov' 'python-responses')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mwclient/mwclient/archive/v${pkgver}.tar.gz")
sha512sums=('ad62f32b720c8d994bcc05fef340f96afa122e2ada3ba15b322f0d97351174984549df51cf60595cf528d53e19de77da57e45c85bbb5d0a09d58cb55fccc5580')

build() {
  cd "$srcdir/mwclient-$pkgver"
  python -m build --wheel --no-isolation
}

check() {
  cd "$srcdir/mwclient-$pkgver"
  python -m pytest
}

package() {
  cd "$srcdir/mwclient-$pkgver"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
