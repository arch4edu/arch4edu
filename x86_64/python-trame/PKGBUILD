# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame
pkgname=python-${_base}
pkgdesc="Framework to build applications in plain Python"
pkgver=3.10.2
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(Apache-2.0)
depends=(python-trame-server python-trame-client python-trame-common python-wslink python-yaml)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
optdepends=('python-pywebview: for app support'
  'jupyterlab: for jupyter support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('1c8e2643b1075ad5c08dfe20d149b9833ef816391acb66566cd018a155ee298b49a396a7e1b50b32b2da2abb33b0dec0d261075ae814af66f80dbc2f0e22c4c3')

prepare() {
  sed -i 's/^include/#include/' ${_base}-${pkgver}/MANIFEST.in
}

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -d ${pkgdir}/usr/share/doc/${pkgname}
  mv examples "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm ${pkgdir}${site_packages}/trame/__init__.py
  rm ${pkgdir}${site_packages}/trame/modules/__init__.py
  rm ${pkgdir}${site_packages}/trame/ui/__init__.py
  rm ${pkgdir}${site_packages}/trame/widgets/__init__.py
}
