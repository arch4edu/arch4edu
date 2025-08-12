# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=setuptools-scm
pkgname=pypy3-${_base}
pkgdesc="the blessed package to manage your versions by scm tags"
pkgver=9.1.1
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3-packaging pypy3-setuptools)
makedepends=(pypy3-build pypy3-installer)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('19fc57b6c786443f217c1039e7a030a6025afaef7558d9595de014f5408c08c6aecfcc493dce739b2d88eb950e5df93503ba449a6cb8d3b74b154dfab8653ac5')

build() {
  cd ${_base}-${pkgver}
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
