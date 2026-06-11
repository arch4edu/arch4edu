# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=flit_core
pkgname=pypy3-${_base//_/-}
pkgver=4.0.0
pkgrel=1
pkgdesc="A PEP 517 build backend for packages using Flit"
arch=(any)
url="https://github.com/pypa/${_base::4}/tree/main/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
source=(${_base::4}-${pkgver}.tar.gz::https://github.com/pypa/${_base::4}/archive/${pkgver}.tar.gz)
sha512sums=('1de9358fa33d0924355679ab6bccf5933f2f154257a875dfec7bf88bb569fce487129ff2d7ea13df16287acaedf9da49ce5f9baccd160ebfb6fd33e831e9c9cb')

build() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 bootstrap_install.py --installdir "$pkgdir"/opt/pypy3/lib/pypy3.11/site-packages dist/${_base}-*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
