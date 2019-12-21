# Maintainer: Anthony25 <Anthony Ruhier>
#
# Thanks to Jeremy "Ichimonji10" Audet <ichimonji10 at gmail dot com> for
# his PKGBUILD that served as a base for this one

pkgbase=python-graphviz
_pkgbase="${pkgbase#python-}"
pkgname=(python-graphviz python2-graphviz)
pkgver=0.13.2
pkgrel=1
pkgdesc='Simple Python interface for Graphviz.'
arch=(any)
url='https://github.com/xflr6/graphviz'
license=(MIT)
depends=('graphviz')
makedepends=(
  'python-setuptools'
  'python2-setuptools'
)
options=(!emptydirs)
source=("https://github.com/xflr6/${_pkgbase}/archive/${pkgver}.tar.gz")
sha256sums=('bb932d6833e7c62ac6b53624b6d55bfd81f40e861f55642e1221ac4f4d8421b4')

package_python-graphviz() {
  cd "${srcdir}/${_pkgbase}-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
  install -Dm 644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-graphviz() {
  cd "${srcdir}/${_pkgbase}-${pkgver}"
  python2 setup.py install --root="${pkgdir}/" --optimize=1
  install -Dm 644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
