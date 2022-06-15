# Maintainer: Donald Webster <fryfrog@gmail.com
# Contributor: Dylan Whichard <dylan@whichard.com>

pkgname='python-schedule'
_name=${pkgname#python-}
pkgver=1.1.0
pkgrel=3
pkgdesc='Python job scheduling for humans.'
arch=('any')
url="https://github.com/dbader/schedule"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
checkdepends=('python-pytest'
              'python-mock')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('bcfb6202659eba0a0613f68d8b06b9f2ffffce0444e231533932f72b01316b72674208a80418de54630d9b25bb80f1c202061672f7c40ca38020b19a0a51fc3f')

package() {
  cd "${srcdir}/schedule-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}
