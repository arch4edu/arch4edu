# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyproject-hooks
pkgname=pypy3-pep517
pkgver=0.13.1
pkgrel=2
pkgdesc="Wrappers to build Python packages using PEP 517 hooks"
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3-tomli)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('4164f39ccd83c46153ac08e43ffe60c364e4dc121301aeb83a2c17d83c26e59bf560a6eab2dc89a1108ae0e168090b691cc0d34f5064d9dea3a130d3b9d573d8')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
