# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=fonttools
pkgname=pypy3-${_base}
pkgdesc="Tools to manipulate font files"
pkgver=4.58.4
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-cython)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('746eb64dee02e77321ca60752e1dd77ff0eb4411bf907968c5118de36618f4bc857d5782c289768fee8c43f9e410f225061736509f6a5c25a829a8ee30a0995b')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
