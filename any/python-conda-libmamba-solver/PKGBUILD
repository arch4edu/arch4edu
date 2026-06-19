# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Brian Thompson <brianrobt@pm.me>

_name=conda-libmamba-solver
pkgname=python-$_name
pkgver=26.4.2
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
sha256sums=('d69a45db04785a1a48d29d98ee4ce6c19147be4703866a23c6b0da1de12b5378')

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
