# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=installer
pkgname=pypy3-${_base}
pkgver=0.4.0
pkgrel=1
pkgdesc="A low-level library for installing from a Python wheel distribution"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-setuptools python-dephell)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('13537c479bc8ead8f8b45c8e5c5182e8b1b32c2889df8015be7f517f390a9efbea6fa167e0886dfade6621a8a2d822bfd662ee0238d3d86689619ca4d5483b26')

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
