# Maintainer: Philipp A. <flying-sheep@web.de>

_name=conda-libmamba-solver
pkgname=python-$_name
pkgver=24.11.1
pkgrel=1
pkgdesc='The libmamba based solver for conda.'
arch=(any)
url="https://github.com/conda/$_name"
license=(BSD-3-Clause)
depends=(python-libmambapy python-boltons)
makedepends=(python-hatch-vcs python-build python-installer python-wheel)
_v=6fe4cd9325f23074f781d8915cf5d4e0c725dbb1
source=("$pkgname-$pkgver.tar.gz::$url/archive/$_v.tar.gz")
sha256sums=('924f8bc472f5fd4052db11434704001d41314e23b0e87feeed1ba7649dca4bd0')

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
