# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=mkl_random
pkgname=python-${_base/_/-}
pkgver=1.2.5
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL Random Number Generation functionality"
arch=(x86_64)
url="https://github.com/IntelPython/${_base}"
license=('custom:BSD-3-clause')
depends=(intel-oneapi-mkl python-numpy)
makedepends=(python-build python-installer python-setuptools cython python-wheel)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('929448a5fa1565386b1406bff66f75b4b83aef0cd3b90c92019ce52f850b8a7aef361c3479f6ccdc53177f7b86ce5683fdd25c04a0a5e8214a79ceff1b9b2fcb')

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
