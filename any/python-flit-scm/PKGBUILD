# Maintainer: Padraic Fanning <fanninpm AT miamioh DOT edu>

_name='flit_scm'
pkgname=python-${_name//_/-}
pkgver=1.7.0
pkgrel=1
pkgdesc="A PEP 518 build backend that uses setuptools_scm to generate a version file from your version control system, then flit to build the package."
arch=('any')
url="https://gitlab.com/WillDaSilva/flit_scm"
license=('MIT')
depends=(
	'python'
	'python-flit-core'
	'python-setuptools-scm'
	'python-tomli'
)
makedepends=(
	'python-build'
	'python-installer'
	'python-wheel'
)
source=("$pkgname-$pkgver.tar.gz::$url/-/archive/$pkgver/$_name-$pkgver.tar.gz")
sha256sums=('05a267d77f6f8ca50a053786fe3c1a74f7222f2955292f2e6c03d2d064a141dc')

build() {
    cd "$_name-$pkgver"
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
