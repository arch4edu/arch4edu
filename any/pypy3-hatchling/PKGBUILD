# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=hatchling
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=1.31.0
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base::5}"
license=(MIT)
depends=(pypy3-packaging pypy3-pathspec pypy3-pluggy pypy3-trove-classifiers)
makedepends=(pypy3-build pypy3-installer)
source=(${url}/archive/${_base}-v${pkgver}.tar.gz)
sha512sums=('707efa1d72bde3e80bb5210602e9f0389f1659dfe65bac6ab33ecfa0e9b433a42c3dac1e92a86398c72dbcb72a69e9dc1db9466c2a9de38993025c52578db2f1')

build() {
  cd ${_base::5}-${_base}-v${pkgver}
  pypy3 -m build --wheel --no-isolation backend
}

package() {
  cd ${_base::5}-${_base}-v${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" backend/dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
