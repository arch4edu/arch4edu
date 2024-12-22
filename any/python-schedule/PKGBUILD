# Maintainer: Donald Webster <fryfrog@gmail.com
# Contributor: Dylan Whichard <dylan@whichard.com>

pkgname='python-schedule'
_name=${pkgname#python-}
pkgver=1.2.2
pkgrel=2
pkgdesc='Python job scheduling for humans.'
arch=('any')
url="https://github.com/dbader/schedule"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
checkdepends=('python-pytest'
              'python-mock')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('e0720e84c6517821f074c0d37a3ec6bc923eb729e19223b7efdd8250dda4ed83347e3b0d5efd07bb67b1716bc3fd992547ca4b57b33aaaa6e70262f0ea8fcf97')

package() {
  cd "${srcdir}/schedule-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}
