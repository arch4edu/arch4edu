# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-server
pkgname=python-${_base}
pkgdesc="Internal server side implementation of trame"
pkgver=3.9.0
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(Apache-2.0)
depends=(python-wslink python-more-itertools)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest-asyncio)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('e0da44627a51efbfa2682ed520bc956f22aacfe2ae768de0b1f83467d076a8e1376600e4413622d7262b7d820a3d7d9ce5f8451af88faa7aabf1e099397dc8a6')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest \
    tests/test_controller.py tests/test_state.py tests/test_translator.py
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # Fix https://aur.archlinux.org/packages/python-trame-server#comment-1027059
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -r "${pkgdir}${site_packages}/docs" "${pkgdir}${site_packages}/examples" "${pkgdir}${site_packages}/tests"
}
