# Maintainer: Jordan Cook <JCook83@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=requests-ratelimiter
pkgname=python-${_base}
pkgdesc="Rate-limiting for the requests library"
pkgver=0.8.0
pkgrel=1
arch=(any)
url="https://github.com/JWCook/${_base}"
license=(MIT)
depends=(python-requests python-pyrate-limiter)
makedepends=(python-build python-installer python-hatchling)
#checkdepends=(python-pytest python-requests-mock)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('900616d4e035475224e619080bc8674f95842177a39538946dbedcf009b37cc12f88e7aa88a50cfa307b0ffada9e9f003ee4557dbe4469ce20511f90a41071ef')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

#check() {
# cd ${_base}-${pkgver}
# python -m venv --system-site-packages test-env
#  test-env/bin/python -m installer dist/*.whl
#  test-env/bin/python -m pytest test
#}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
