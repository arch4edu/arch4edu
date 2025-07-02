# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>
# Maintainer: Jingbei Li <i@jingbei.li>
_base=mkl-service
pkgname=python-mkl-service
pkgver=2.5.2
pkgrel=1
pkgdesc="Python hooks for Intel(R) Math Kernel Library runtime control settings"
arch=(x86_64)
url="https://github.com/IntelPython/mkl-service"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python)
makedepends=(python-build python-installer python-setuptools python-wheel cython procps-ng)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('ddd5412960c5f318b83ca4d8f2f416da0cd34ae430e7e960449c059ce12934622c5601c695a48c9dd6291ec4d7b45f0d738848640a1b106eee4e2ec667708c9c')

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
