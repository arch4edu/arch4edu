# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=urllib3
pkgname=pypy3-${_base}
pkgdesc="HTTP library with thread-safe connection pooling, file post, and more"
pkgver=2.6.3
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('554cedfd97d411fffa9a8ba46f592eab9e58c5fa8822ecd5a73ab45d6adfc188a6b9c4e238d02a4fbd3a1067a25a1de841a33d398d0641e22a32ea414876b615')

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
