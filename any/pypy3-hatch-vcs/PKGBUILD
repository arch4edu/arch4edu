# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=hatch-vcs
pkgname=pypy3-${_base}
pkgdesc="Hatch plugin for versioning with your preferred VCS"
pkgver=0.5.0
pkgrel=1
arch=(any)
url="https://github.com/ofek/${_base}"
license=(MIT)
depends=(pypy3-hatchling pypy3-setuptools-scm)
makedepends=(pypy3-build pypy3-installer)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('ed2b81df3f0b51f9ebca28c023bbf1e66088971e76439ab864838012dc28ec140eadf4f07a4b7aca66b0f5c52fd3ccc001602e6c91dcc8d6241c0b56193cba54')

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
