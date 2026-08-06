# Maintainer: Christopher Arndt <aur at chrisarndt dot de>

_name=colorzero
pkgname="python-${_name}"
pkgver=2.0
pkgrel=2
pkgdesc="A simple to use and pythonic color manipulation library"
arch=('any')
url="https://${_name}.readthedocs.org/"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('e7d5a5c26cd0dc37b164ebefc609f388de24f8593b659191e12d85f8f9d5eb58')


build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package_python-colorzero() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="$pkgdir" --skip-build --optimize=1

  # license
  install -Dm644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

# vim:set ts=2 sw=2 et:
