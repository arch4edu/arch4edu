# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jordan Cook <JCook83@gmail.com>
# Contributor: Benoit Pierre <benoit.pierre@gmail.com>
# Contributor: Marc Plano-Lesay <kernald@enoent.fr>
_base=url-normalize
pkgname=python-${_base}
pkgdesc="URL normalization for Python"
pkgver=2.2.1
pkgrel=1
arch=(any)
url="https://github.com/niksite/${_base}"
license=(MIT)
depends=(python-idna)
makedepends=(python-build python-installer python-setuptools python-wheel)
# checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('51f57bf6d94863662789321b8965c0ca833d34d0c8095f2a39303a410f61c24f04a56e83258dafaa8a4250b0d1b44ad3c3a63430da2b04f4d906d84a71208f46')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

# check() {
#   cd ${_base}-${pkgver}
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -m pytest tests
# }

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
