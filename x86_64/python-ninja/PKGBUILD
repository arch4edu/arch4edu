# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ninja-python-distributions
pkgname=python-${_base%%-*}
pkgdesc="Ninja is a small build system with a focus on speed"
pkgver=1.11.1
pkgrel=1
arch=(any)
url="https://github.com/scikit-build/${_base}"
license=(Apache)
depends=(python)
makedepends=(python-build python-installer python-scikit-build)
provides=(${_base%%-*})
conflicts=(${_base%%-*})
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('f6193ba9d1d55da11a437d17b96ef7c0574fd0033c05b1f2d2a4c652241a460a1066f2044bbbe9f134e2af3c8ff185304053da5dd7a10e337cdf60f910a11062')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl

  # Symlink license file
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  install -d ${pkgdir}/usr/share/licenses/${pkgname}
  ln -s "${site_packages}/${_base%%-*}-${pkgver}.dist-info/LICENSE_Apache_20" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
