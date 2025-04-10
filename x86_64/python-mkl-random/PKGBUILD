# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=mkl_random
pkgname=python-${_base/_/-}
pkgver=1.2.10
pkgrel=1
pkgdesc="NumPy-based Python interface to Intel (R) MKL Random Number Generation functionality"
arch=(x86_64)
url="https://github.com/IntelPython/${_base}"
license=(BSD-3-Clause)
depends=(intel-oneapi-mkl python-numpy)
makedepends=(python-build python-installer python-setuptools cython python-wheel intel-oneapi-mkl)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('187678ae12d81ed5a975d9e452adcdc167e99276e391d2171188e82276e620ecb0a6044457777e241e25aa9a5a91f5d388901372a0dadc8322a181bf34668130')

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
