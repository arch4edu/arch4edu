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
pkgver=23.1
pkgrel=1
pkgdesc="The PyPA recommended tool for installing Python packages"
url="https://pip.pypa.io"
arch=(any)
license=(MIT)
depends=(pypy3 pypy3-setuptools)
source=(https://github.com/pypa/${_base}/archive/${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('ba1417811d69462b1e858d6a431abdafdf66a217f9fb25ad9c8430b3ea5289c631a282f3c399f607539d2ce9e2a71b556926f6ebf30be18d86ccda192afe0dfb')
b2sums=('2d4e0dcfa730fe68b6b73d87fb3706a5c68f8eb497fe84c15a8a4ed5aa436a5ef07949d3c3d1393aa836bc8d2f67dbfad25609f807519a3d36b3aed34aff4756')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 setup.py install --prefix=/opt/pypy3/ --root="${pkgdir}"

  mkdir -p "${pkgdir}/usr/bin"
  mv "${pkgdir}/opt/pypy3/bin/pip" "${pkgdir}/usr/bin/pip-pypy3"

  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
