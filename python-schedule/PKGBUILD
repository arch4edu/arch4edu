# Maintainer: Donald Webster <fryfrog@gmail.com
# Contributor: Dylan Whichard <dylan@whichard.com>

pkgname=('python-schedule' 'python2-schedule')
_name=${pkgname#python-}
pkgver=1.0.0
pkgrel=2
pkgdesc='Python job scheduling for humans.'
arch=('any')
url="https://github.com/dbader/schedule"
license=('MIT')
makedepends=('python-setuptools'
             'python2-setuptools')
checkdepends=('python-pytest'
              'python-mock'
              'python2-pytest'
              'python2-mock')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('528e415382fed39749be1a375815a7475288c8bd6f77133a39e79fc9512e1032c99185a53140db4f7153f1479e6aab57ed05637a09aa92316683f310353c1b11')

prepare() {
  cp -a schedule-${pkgver}{,-py2}
}

package_python-schedule() {
  depends=('python')
  cd "${srcdir}/schedule-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}

package_python2-schedule() {
  depends=('python2')
  cd "${srcdir}/schedule-${pkgver}-py2"
  python2 setup.py install --root="${pkgdir}" --optimize=1
}
