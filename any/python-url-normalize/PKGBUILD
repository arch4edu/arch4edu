# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jordan Cook <JCook83@gmail.com>
# Contributor: Benoit Pierre <benoit.pierre@gmail.com>
# Contributor: Marc Plano-Lesay <kernald@enoent.fr>
_base=url-normalize
pkgname=python-${_base}
pkgdesc="URL normalization for Python"
pkgver=2.1.0
pkgrel=1
arch=(any)
url="https://github.com/niksite/${_base}"
license=(MIT)
depends=(python-idna)
makedepends=(python-build python-installer python-setuptools python-wheel)
# checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('37545382ddfc08740ecb776f541bf0f75ee40b681b87f139dd4c4f7755f60c665a66d4d8e552a1dc566ab871b766e054c1e42da9dcd7df00622ea9f3793523cc')

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
