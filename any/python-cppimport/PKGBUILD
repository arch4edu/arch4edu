# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=cppimport
pkgname=python-${_base}
pkgdesc="Import C++ files directly from Python!"
pkgver=26.04.17
pkgrel=1
arch=(any)
url="https://github.com/tbenthompson/${_base}"
license=(MIT)
depends=(python-mako pybind11 python-filelock)
makedepends=(python-build python-installer python-setuptools-scm python-wheel)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('71888a3485a278e92a832c2aabbda7deec957f647ff4baad2c6c942c7f6367ca678ee613043f4f814ae4d7a55c1ba9059fc5295abf7c97b24e2f6ad5d7340fa5')

build() {
  cd ${_base}-${pkgver}
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
