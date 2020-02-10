# Maintainer: Alex Brinister <alex_brinister at yahoo dot com>

pkgbase=python-cheetah3
pkgname=('python-cheetah3' 'python2-cheetah3')
_name=Cheetah3
pkgver=3.2.4
pkgrel=4
pkgdesc="A Python powered template engine and code generator"
arch=(any)
url="http://www.cheetahtemplate.org"
license=(MIT)
makedepends=('python-setuptools'
             'python2-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('f991865d384cbc7fe287c5d89d9990bfdde205df64f2c9cf8df17427ce865701e4fb2c35e7d52753b40ac170a56b8d071e7ae8bff83cbefe8ec662099fbe1340')

prepare() {
  cp -a Cheetah3-${pkgver}{,-py2}
}

package_python-cheetah3() {
  optdepends=('python-markdown')

  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-cheetah3() {
  optdepends=('python2-markdown')

  cd "${srcdir}/${_name}-${pkgver}-py2"
  python2 setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Avoid conflict with python-cheetah3
  for name in cheetah cheetah-analyze cheetah-compile; do
    mv "${pkgdir}/usr/bin/${name}"{,2}
  done
}
