# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>
# Maintainer: Jingbei Li <i@jingbei.li>
_base=mkl-service
pkgname=python-mkl-service
pkgver=2.5.0
pkgrel=1
pkgdesc="Python hooks for Intel(R) Math Kernel Library runtime control settings"
arch=(x86_64)
url="https://github.com/IntelPython/mkl-service"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python)
makedepends=(python-build python-installer python-setuptools python-wheel cython procps-ng)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('f7a6671cb597a58a0948f55b9f87b5d79ce444e597be468f7f92af16e29fa5fc9e4a6a869da137371ffd09afbca12f3cb6b6adfa067b3adc2d3680f259ff5099')

build() {
  source /opt/intel/oneapi/setvars.sh
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer ${_base}-${pkgver}/dist/*.whl
  test-env/bin/python -m pytest ${_base}-${pkgver}/mkl/tests
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
