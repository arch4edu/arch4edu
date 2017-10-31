# Maintainer: Anthony25 <Anthony Ruhier>
#
# Thanks to Jeremy "Ichimonji10" Audet <ichimonji10 at gmail dot com> for
# his PKGBUILD that served as a base for this one

pkgbase=python-graphviz
_pkgbase="${pkgbase#python-}"
pkgname=(python-graphviz python2-graphviz)
pkgver=0.8.1
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
sha256sums=('19fa90669493b86df0d4adb9ee55147de92329f143480218d1c4eb91fa877cfa')

package_python-graphviz() {
  cd "${srcdir}/${_pkgbase}-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-graphviz() {
  cd "${srcdir}/${_pkgbase}-${pkgver}"
  python2 setup.py install --root="${pkgdir}/" --optimize=1
  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
