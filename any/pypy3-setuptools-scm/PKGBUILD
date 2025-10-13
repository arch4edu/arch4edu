# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=setuptools-scm
pkgname=pypy3-${_base}
pkgdesc="the blessed package to manage your versions by scm tags"
pkgver=9.2.1
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3-packaging pypy3-setuptools)
makedepends=(pypy3-build pypy3-installer)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('0f2d0d0acfa5ca033de8a4a07c1a1a0138c25236cef4b283db61e556894af80f2392fbed952899d3098160d16a5c81e30d11bb8dcc53d01ac39aca009fa16c22')

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
