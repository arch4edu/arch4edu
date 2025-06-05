# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=hatchling
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=1.27.0
pkgrel=2
arch=(any)
url="https://github.com/pypa/${_base::5}"
license=(MIT)
depends=(pypy3-packaging pypy3-pathspec pypy3-pluggy pypy3-trove-classifiers)
makedepends=(pypy3-build pypy3-installer)
source=(${url}/archive/${_base}-v${pkgver}.tar.gz)
sha512sums=('d519428c4c7c21950df2484f38332b5c89525347f3557ff21a55a85811955c8466f6eb4f919d824ab7a576cd35d8a59e4a5e7827100f6ea1e38c10c0f1864a29')

build() {
  cd ${_base::5}-${_base}-v${pkgver}
  pypy3 -m build --wheel --no-isolation backend
}

package() {
  cd ${_base::5}-${_base}-v${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" backend/dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
