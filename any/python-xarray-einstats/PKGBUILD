# Maintainer:  Anton Kudelin <kudelin at proton dot me>

_pyname=xarray-einstats
pkgname=python-$_pyname
pkgver=0.8.0
pkgrel=1
pkgdesc='Stats, linear algebra and einops for xarray'
arch=(any)
url='https://einstats.python.arviz.org'
license=(Apache)
depends=(python-scipy python-xarray)
makedepends=(python-poetry python-build python-installer python-flit-core)
optdepends=(python-dask)
checkdepends=(python-pytest python-numba python-einops)
source=($pkgname-$pkgver.tar.gz::https://github.com/arviz-devs/$_pyname/archive/refs/tags/v$pkgver.tar.gz)
sha256sums=('fdd1eccb9da7190a9e266faf4c590e8c51c65744b1377fa54d9fdfce8a4f86f6')

build() {
  cd "$srcdir/$_pyname-$pkgver"
  python -m build \
    --wheel \
    --no-isolation \
    --skip-dependency-check
}

check() {
  cd "$srcdir/$_pyname-$pkgver"

  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl

  test-env/bin/python -m pytest -v
}

package() {
  cd "$srcdir/$_pyname-$pkgver"
  python -m installer \
    --destdir="$pkgdir" \
    --compile-bytecode=2 \
    dist/*.whl
}
