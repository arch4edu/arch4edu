# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Brian Thompson <brianrobt@pm.me>

_name=conda-libmamba-solver
pkgname=python-$_name
pkgver=25.4.0
pkgrel=1
pkgdesc='The libmamba based solver for conda.'
arch=(any)
url="https://github.com/conda/$_name"
license=(BSD-3-Clause)
depends=(
	micromamba
	python-boltons
)
makedepends=(
	python-hatch-vcs
	python-build
	python-installer
	python-wheel
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('a00bd98681607b1db5783f680e3375931ad990b7d19ae1ebf6987c20330bbfa9')

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
