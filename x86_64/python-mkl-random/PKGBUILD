# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=mkl_random
pkgname=python-${_base/_/-}
pkgver=1.2.11
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL Random Number Generation functionality"
arch=(x86_64)
url="https://github.com/IntelPython/${_base}"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python-numpy)
makedepends=(python-build python-installer python-setuptools cython python-wheel intel-oneapi-mkl)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('65e8c6b22dd5675c5279c785b43c675bac8e9a5b9336460b06b7643aa733909684ff732a0c08acdccb4fe841fce45613b1d36f67e7e13674e3a85986b95be786')

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
