# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=hatchling
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=1.30.1
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base::5}"
license=(MIT)
depends=(pypy3-packaging pypy3-pathspec pypy3-pluggy pypy3-trove-classifiers)
makedepends=(pypy3-build pypy3-installer)
source=(${url}/archive/${_base}-v${pkgver}.tar.gz)
sha512sums=('dfb57a076ec683d82228a453c2485153defd0b1d2f31a43041ae0b7ddd428b931ab1288b0b23393df80f5630bd09c78faa2852b28649af0db2e7f55bd915b942')

build() {
  cd ${_base::5}-${_base}-v${pkgver}
  pypy3 -m build --wheel --no-isolation backend
}

package() {
  cd ${_base::5}-${_base}-v${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" backend/dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
