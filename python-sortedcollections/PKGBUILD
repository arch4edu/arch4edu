# Maintainer: Sam Whited <sam@samwhited.com>
# Contributor: Amos Onn <amosonn at gmail dot com>

pkgbase=python-sortedcollections
pkgname=('python-sortedcollections' 'python2-sortedcollections')
_name=${pkgbase#python-}
pkgver=1.1.2
pkgrel=2
pkgdesc="A python library for sorted collections."
arch=('any')
url="http://www.grantjenks.com/docs/sortedcollections/"
license=(Apache)
makedepends=('python-setuptools'
             'python2-setuptools'
             'python-sortedcontainers>=2.0.0'
             'python2-sortedcontainers>=2.0.0')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('b93e0decbd7f8f19e40c320709e70e4845b6c8b3a0e96c3c4f707b4b93e1d38a')

package_python-sortedcollections() {
  depends+=('python' 'python-sortedcontainers>=2.0.0')

  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}"
}

package_python2-sortedcollections() {
  depends+=('python2' 'python2-sortedcontainers>=2.0.0')

  cd "${srcdir}/${_name}-${pkgver}"
  python2 setup.py install --root="${pkgdir}"
}

# vim: ts=2 sw=2 et:
