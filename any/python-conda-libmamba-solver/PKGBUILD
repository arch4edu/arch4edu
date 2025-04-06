# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Brian Thompson <brianrobt@pm.me>

_name=conda-libmamba-solver
pkgname=python-$_name
pkgver=25.3.0
pkgrel=1
pkgdesc='The libmamba based solver for conda.'
arch=(any)
url="https://github.com/conda/$_name"
license=(BSD-3-Clause)
depends=(python-libmambapy python-boltons)
makedepends=(python-hatch-vcs python-build python-installer python-wheel)
_v=539f05b15aca43c50222cc98d6c6fd39368f7cd3
source=("$pkgname-$pkgver.tar.gz::$url/archive/$_v.tar.gz")
sha256sums=('deeb825cbf61131760f4fcf556e33d73e8eeba8354896d7a34ae6fd78a86683c')

build() {
	cd "$_name-$_v"
    export SETUPTOOLS_SCM_PRETEND_VERSION="${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "$_name-$_v"
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
