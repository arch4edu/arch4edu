# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=dateutil
pkgname=pypy3-${_base}
pkgdesc="Extensions to the standard Python datetime module"
pkgver=3.0.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(Apache-2.0 BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('d2e97ec2f2f4488230a6c6e2376a05746dcec006ab800e8e846cb1450822141495df85de8bfd96f7174159662e343756c468fc8840d51253bc761d9583c24c16')

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
