# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=flit_core
pkgname=pypy3-${_base//_/-}
pkgver=4.1.0
pkgrel=1
pkgdesc="A PEP 517 build backend for packages using Flit"
arch=(any)
url="https://github.com/pypa/${_base::4}/tree/main/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
source=(${_base::4}-${pkgver}.tar.gz::https://github.com/pypa/${_base::4}/archive/${pkgver}.tar.gz)
sha512sums=('e31f86cb595f6749867da1173f56b9c2563fcb9c3c38cdbc637a511992e7b462f7627571aad3ef1da5cc6c6574448dc69cfeb9a37d3ed7a6ce5537e90dcb5fb9')

build() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 bootstrap_install.py --installdir "$pkgdir"/opt/pypy3/lib/pypy3.11/site-packages dist/${_base}-*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
