# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=hatchling
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=1.28.0
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base::5}"
license=(MIT)
depends=(pypy3-packaging pypy3-pathspec pypy3-pluggy pypy3-trove-classifiers)
makedepends=(pypy3-build pypy3-installer)
source=(${url}/archive/${_base}-v${pkgver}.tar.gz)
sha512sums=('cbf29be0d0e2e0053c39034a697b4bebce4754205713c9dc35c9f3c9ea9be2652924664c0d11b90869443995c6f9f06ce20ca06afe10a2ac174a0e9dc2e737a2')

build() {
  cd ${_base::5}-${_base}-v${pkgver}
  pypy3 -m build --wheel --no-isolation backend
}

package() {
  cd ${_base::5}-${_base}-v${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" backend/dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
