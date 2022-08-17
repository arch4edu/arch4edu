# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=pydotplus
pkgname=python-${_base}
pkgver=2.0.2
pkgrel=2
pkgdesc="Interface to Graphviz’s Dot language"
arch=(any)
url="https://${_base}.readthedocs.io"
license=(MIT)
depends=(python-pyparsing graphviz)
makedepends=(python-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('6f06a1f284401123a4514f9e9a4974dee8dc8d01e6b7c40a797fb70eed22b99fe774272f8b106b5632a33f524b356349fe1ff9633101ff61ef2fc3fe69d641ac')

build() {
  cd ${_base}-${pkgver}
  python setup.py build
}

# check() {
#   cd ${_base}-${pkgver}/test
#   PYTHONPATH="${srcdir}/${_base}-${pkgver}/build/lib:${PYTHONPATH}" python pydot_unittest.py
# }

package() {
  cd ${_base}-${pkgver}
  python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
