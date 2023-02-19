# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: dustball <sebastiansonne@hush.com>
# Adapted from the package python-pip with the following original contributors:
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Dan McGee <dan@archlinux.org>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Sebastien Binet <binet@lblbox>
_base=pip
pkgname=pypy3-${_base}
pkgver=23.0.1
pkgrel=1
pkgdesc="The PyPA recommended tool for installing Python packages"
url="https://pip.pypa.io"
arch=(any)
license=(MIT)
depends=(pypy3 pypy3-setuptools)
source=(https://github.com/pypa/${_base}/archive/${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('ed14ce37293e749b4fd93d7f93d81356c77428b1fb14dfd760b59aea720ebb3cce5a49c2d32ab600e73b37389937830ff4dee04750e83078c8ab9d57513f294c')
b2sums=('1781b0340ba7f76299fa8e37f0509f15a08cc599d196c74b90a2cb79321de570240ed9f12bc64d45ede2182ec8a3eead44ce1b840eaa83931d089ecc07923203')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3/ --root="${pkgdir}"

  mkdir -p "${pkgdir}/usr/bin/"
  mv "${pkgdir}/opt/pypy3/bin/pip" "${pkgdir}/usr/bin/pip-pypy3"

  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
