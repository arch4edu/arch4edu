# Maintainer: Donald Webster <fryfrog@gmail.com
# Contributor: Dylan Whichard <dylan@whichard.com>

pkgname='python-schedule'
_name=${pkgname#python-}
pkgver=1.2.1
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
sha512sums=('f2802bb7c49afd649f3e4650366bcd03c64db0301e929c981e1888323b6debac1280d668dad0e2fd7149534cfccefc46eaaafc0a009828ba11606c6a2cfbcc81')

package() {
  cd "${srcdir}/schedule-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}
