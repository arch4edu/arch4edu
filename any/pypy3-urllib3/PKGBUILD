# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=urllib3
pkgname=pypy3-${_base}
pkgdesc="HTTP library with thread-safe connection pooling, file post, and more"
pkgver=2.6.1
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('a5935e42cfa843688f68e2c71de3eff4c505907bd155f41a6f3406000cfaa060db0184a18448e269192c3f69861f5630a112fe207874da45bf475bebbdeb2b83')

build() {
  cd ${_base}-${pkgver}
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
