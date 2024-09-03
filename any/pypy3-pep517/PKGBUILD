# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyproject-hooks
pkgname=pypy3-pep517
pkgver=0.13.1
pkgrel=1
pkgdesc="Wrappers to build Python packages using PEP 517 hooks"
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3-tomli)
makedepends=(pypy3-setuptools python-dephell)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('4164f39ccd83c46153ac08e43ffe60c364e4dc121301aeb83a2c17d83c26e59bf560a6eab2dc89a1108ae0e168090b691cc0d34f5064d9dea3a130d3b9d573d8')

prepare() {
  cd ${_base}-${pkgver}
  # https://gitlab.archlinux.org/archlinux/packaging/packages/python-tomli/-/blob/1.0.4-1/PKGBUILD#L18
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
