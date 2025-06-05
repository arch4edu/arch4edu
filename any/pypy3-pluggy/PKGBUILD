# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pluggy
pkgname=pypy3-${_base}
pkgdesc="plugin and hook calling mechanisms for python"
pkgver=1.6.0
pkgrel=2
arch=(any)
url="https://github.com/pytest-dev/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('c32690cd2737605aff80d20db126d47cde6d7a48f6717c198b37aa8721f895351a684a15484499d76f93331829776e3d9157399a297f75495b681929742f572f')

build() {
  cd ${_base}-${pkgver}
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
