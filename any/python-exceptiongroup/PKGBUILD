# Maintainer: Padraic Fanning <fanninpm AT miamioh DOT edu>

_name=exceptiongroup
pkgname=python-${_name}
pkgver=1.0.0rc8
pkgrel=1
pkgdesc="Backport of PEP 654 (exception groups)"
arch=('any')
url="https://github.com/agronholm/${_name}"
license=('MIT')
depends=('python')
makedepends=(
	'python-build'
	'python-flit-scm'
	'python-installer'
	'python-wheel'
)
checkdepends=('python-pytest')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('eea886105f6b88625ce391b2cba78334f6f20edb6c9a2b613eaaffbe9b2dcf96')


build() {
    cd "$_name-$pkgver"
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd "$_name-$pkgver"
    pytest
}

package() {
    cd "$_name-$pkgver"
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
