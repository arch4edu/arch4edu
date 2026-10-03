# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>
# Maintainer: Jingbei Li <i@jingbei.li>
_base=mkl-service
pkgname=python-mkl-service
pkgver=2.9.0
pkgrel=1
pkgdesc="Python hooks for Intel(R) Math Kernel Library runtime control settings"
arch=(x86_64)
url="https://github.com/IntelPython/mkl-service"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python)
makedepends=(python-build python-installer meson-python ninja cmake cython procps-ng)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('15c3ec8d4fddc990926b24f8c43571ec2509a10543771ba2b0259e1a52a499580bee07bb22d47628a3800251aac570c389e6ce89e530e289de26bb51397e59ad')

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
