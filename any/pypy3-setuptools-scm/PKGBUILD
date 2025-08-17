# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=setuptools-scm
pkgname=pypy3-${_base}
pkgdesc="the blessed package to manage your versions by scm tags"
pkgver=9.2.0
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3-packaging pypy3-setuptools)
makedepends=(pypy3-build pypy3-installer)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('16a2788c58bb70fbb72b7232e2bd62d8d1bf0881815236674290e14abdbbb7ac2059e9791d50cc5f360e259a1982d05e56f2fa8c296aa71800d623b022c0ce74')

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
