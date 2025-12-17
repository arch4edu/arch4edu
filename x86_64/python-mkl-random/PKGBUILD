# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=mkl_random
pkgname=python-${_base/_/-}
pkgver=1.3.1
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL Random Number Generation functionality"
arch=(x86_64)
url="https://github.com/IntelPython/${_base}"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python-numpy)
makedepends=(python-build python-installer python-setuptools cython python-wheel intel-oneapi-mkl)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('058cb9a40626f034421d1a08a2a7b11935bc2de6d054ded87db8cd1070e83776f307d721312ec9c13ac949a6c3384c5ef7800745015e4c63b483c5af366f6f96')

build() {
  cd ${_base}-${pkgver}
  CFLAGS='-I /opt/intel/mkl/include -L/opt/intel/mkl/lib/intel64' \
    python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python examples/*.py
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
