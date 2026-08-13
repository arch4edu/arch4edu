# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Brian Thompson <brianrobt@pm.me>

_name=conda-libmamba-solver
pkgname=python-$_name
pkgver=26.7.0
pkgrel=1
pkgdesc='The libmamba based solver for conda.'
arch=(any)
url="https://github.com/conda/$_name"
license=(BSD-3-Clause)
depends=(
	python-libmambapy
	python-boltons
	python-msgpack
	python-requests
	python-zstandard
)
makedepends=(
	python-hatch-vcs
	python-build
	python-installer
	python-wheel
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('785d6035eedf511c6755d53a5ff34634a56427be49fd337bb6433c2270b4fdb6')

build() {
	cd "$_name-$pkgver"
	export SETUPTOOLS_SCM_PRETEND_VERSION="${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "$_name-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
