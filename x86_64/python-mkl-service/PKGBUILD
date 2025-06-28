# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>
# Maintainer: Jingbei Li <i@jingbei.li>
_base=mkl-service
pkgname=python-mkl-service
pkgver=2.5.1
pkgrel=1
pkgdesc="Python hooks for Intel(R) Math Kernel Library runtime control settings"
arch=(x86_64)
url="https://github.com/IntelPython/mkl-service"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python)
makedepends=(python-build python-installer python-setuptools python-wheel cython procps-ng)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('43334b3ea0650347dd5c950958d3a33c3220eeccdc2d2d733243e3bd3a8e8cb3f4c27ab57099266054da1ef2e4fd99e105fb05dddddba5cef847bc20fac6ac8e')

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
