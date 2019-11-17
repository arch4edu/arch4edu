# Maintainer: Donald Webster <fryfrog@gmail.com
# Contributor: Dylan Whichard <dylan@whichard.com>

pkgname=('python-schedule' 'python2-schedule')
_name=${pkgname#python-}
pkgver=0.6.0
pkgrel=1
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
sha512sums=('0a2704055c7f2b3bbf08582a7f099b5118b0e97e39cda0a299b66620ab17cedb63c44e7bda7d3480649c8b4d609f3e051f8111e7370c39210c305444c287ae93')

prepare() {
  cp -a schedule-${pkgver}{,-py2}
}

check() {
  cd "$srcdir"/schedule-${pkgver}
  python setup.py test

  cd "$srcdir"/schedule-${pkgver}-py2
  python2 setup.py test
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
