# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=fonttools
pkgname=pypy3-${_base}
pkgdesc="Tools to manipulate font files"
pkgver=4.69.1
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-cython)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('a1ac25893a4d83229d973b035cb71db5a95b46c4aabb2e7aa98dff3e731a5679e2634b70a8ae7f68cdbe6ad2f73c6ec54d2b33f5af964a12dbc7c63107ce5d3b')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
