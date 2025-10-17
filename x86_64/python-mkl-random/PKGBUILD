# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=mkl_random
pkgname=python-${_base/_/-}
pkgver=1.3.0
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL Random Number Generation functionality"
arch=(x86_64)
url="https://github.com/IntelPython/${_base}"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python-numpy)
makedepends=(python-build python-installer python-setuptools cython python-wheel intel-oneapi-mkl)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('b28fcaa70c08566a2faecb1e24fd30c988ad30737a828f5fec2ebfaa4109d449e10d40eb36da3dae39a961c3150e126039cf9be01cd0d44835d6ecc7eb7df0cf')

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
