# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-client
pkgname=python-${_base}
pkgdesc="Internal client of trame"
pkgver=3.11.4
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(MIT)
depends=(python-trame-common)
makedepends=(python-build python-installer python-setuptools python-wheel nodejs npm)
checkdepends=(python-pytest-xprocess python-pillow python-pixelmatch python-playwright)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('4275c061e1122385d9a3544f172da0662d02bbbbb9100835e05152740bc237e3aaaac8be62004a82f0e489f8ef45059ce7831203bea1947055223f580eda150e')

build() {
  cd ${srcdir}/${_base}-${pkgver}/vue2-app
  npm install
  npm run build

  cd ${srcdir}/${_base}-${pkgver}/vue3-app
  npm install
  npm run build

  cd ${srcdir}/${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest tests/test_import.py
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # Fix https://aur.archlinux.org/packages/python-trame-server#comment-1027059
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -r "${pkgdir}${site_packages}/examples" "${pkgdir}${site_packages}/js-lib" "${pkgdir}${site_packages}/tests"
}
