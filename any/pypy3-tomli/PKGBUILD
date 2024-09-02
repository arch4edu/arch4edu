# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=tomli
pkgname=pypy3-${_base}
pkgver=2.0.1
pkgrel=1
pkgdesc="A lil' TOML parser"
arch=(any)
url="https://github.com/hukkin/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-setuptools python-dephell)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz
  typerror.patch::${url}/commit/5646e6923d895725aad7ecfa32be19861812d1fc.patch)
sha512sums=('a467f8d48cdbd7213bd9b6f85fd48ba142ab7c9656c40bb30785e1c4b37a9e29eaed420f183458ad20112baee8413ebbec87755332795c8f02235d1018c3aa5c'
  '11a30c171767414d0f8e8fbe4bb880ceb6c4604fddbd674a6b9016ad2f8273954e278219a8cae2598b609ac6f51ddaba67a1324b55d00f1dcc10568c1511469d')

prepare() {
  cd ${_base}-${pkgver}
  # https://github.com/hukkin/tomli/issues/223
  patch -p1 -i ../typerror.patch
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
