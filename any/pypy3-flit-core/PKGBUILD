# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=flit_core
pkgname=pypy3-${_base//_/-}
pkgver=4.0.2
pkgrel=1
pkgdesc="A PEP 517 build backend for packages using Flit"
arch=(any)
url="https://github.com/pypa/${_base::4}/tree/main/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
source=(${_base::4}-${pkgver}.tar.gz::https://github.com/pypa/${_base::4}/archive/${pkgver}.tar.gz)
sha512sums=('10086861c59047fad5b02b39b527f3e805bf93ea21d66879ce67743ab04fca4021b491963d89590821806c3747baccdc697f953a27ef50f0608eb0519f8a6909')

build() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 bootstrap_install.py --installdir "$pkgdir"/opt/pypy3/lib/pypy3.11/site-packages dist/${_base}-*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
