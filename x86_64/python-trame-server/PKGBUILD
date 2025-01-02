# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-server
pkgname=python-${_base}
pkgdesc="Internal server side implementation of trame"
pkgver=3.2.4
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(Apache-2.0)
depends=(python-wslink python-more-itertools python-msgpack)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  indentation-fix.patch::${url}/commit/bf20291072a5f1750e1cd885f494d48e55d8c10e.patch)
sha512sums=('a6a7ebd5df9f4b5696281279196ae3ff75bc4cb86b38266f55c511e81aeaa17577ae91d8895065d72922764555ad07a866267d08b2c7b123690e8937f7e7474d'
            '9a2bfd41aced41553d9661fcdde63c70a91073c7ab9166fbb1869e77bd85d2c936837304142d40dc632d3be5e6c5451b72210f52c8af152c4cd694fbb33ff019')

prepare() {
  sed -i 's/^include/#include/' ${_base}-${pkgver}/MANIFEST.in
  cd ${_base}-${pkgver}
  patch -p1 -i ../indentation-fix.patch
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
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
