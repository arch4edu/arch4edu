# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=installer
pkgname=pypy3-${_base}
pkgver=0.5.0
pkgrel=1
pkgdesc="A low-level library for installing from a Python wheel distribution"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-setuptools python-dephell)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('8731bbf8a51b1094dc87f84575eec07a650988bdeddf205d04cf80a5088eac0d8b2927022864f4011a9562fcaae9f511747e5672f94ec3cce1dccdfa833c4fce')

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
