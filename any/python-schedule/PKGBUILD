# Maintainer: Donald Webster <fryfrog@gmail.com
# Contributor: Dylan Whichard <dylan@whichard.com>

pkgname='python-schedule'
_name=${pkgname#python-}
pkgver=1.2.0
pkgrel=1
pkgdesc='Python job scheduling for humans.'
arch=('any')
url="https://github.com/dbader/schedule"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
checkdepends=('python-pytest'
              'python-mock')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('b2a4d22d7d045d3ac765630b370169e5f80aae33cb40bb76e16afc55a62751e851cca5adc1651ee855108a4f849d107adef2fa146794d3445667937a1bf8278c')

package() {
  cd "${srcdir}/schedule-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}
