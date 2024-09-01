# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=installer
pkgname=pypy3-${_base}
pkgver=0.2.3
pkgrel=2
pkgdesc="A low-level library for installing from a Python wheel distribution"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-setuptools python-dephell)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('daa80c11e734ffa520779c7e08df4779f41dec429ebf642f024d575cfd952da0bbd0cc78190ca1b50bbcff3adf5cf5d97c4f1f605714d5f8fd40a21a64fbe623')

prepare() {
  # https://gitlab.archlinux.org/archlinux/packaging/packages/python-installer/-/blob/0.2.3-2/PKGBUILD#L21
  cd ${_base}-${pkgver}
  dephell deps convert --from pyproject.toml --to setup.py
}

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
