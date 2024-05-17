# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-client
pkgname=python-${_base}
pkgdesc="Internal client of trame"
pkgver=3.0.3
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel nodejs npm)
checkdepends=(python-pytest-xprocess python-pillow python-pixelmatch python-seleniumbase)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('12f76f9721cab3fa81eafa4e66e590bf93fdcf36bd42843bcd09e689f8472c1c3c07016c8bd77a42c46f0f21eb528885a1ab4cf6ad321c6d09b5ae49bd9cf965')

prepare() {
  sed -i 's/^include/#include/' ${_base}-${pkgver}/MANIFEST.in
}

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
}
