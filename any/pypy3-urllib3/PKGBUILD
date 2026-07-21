# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=urllib3
pkgname=pypy3-${_base}
pkgdesc="HTTP library with thread-safe connection pooling, file post, and more"
pkgver=2.7.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('5bcfcde51cf28ab5d999ec863de9eed794df84530bdcc957259376ee8c677fe9aaee609dc643324b99c43610553914366164d99407334d8eb6ca2c60eba12f49')

build() {
  cd ${_base}-${pkgver}
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
