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
pkgver=23.3
pkgrel=1
pkgdesc="The PyPA recommended tool for installing Python packages"
url="https://pip.pypa.io"
arch=(any)
license=(MIT)
depends=(pypy3 pypy3-setuptools)
source=(https://github.com/pypa/${_base}/archive/${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('1afef5374410387bd1056a9ada21893f1fbb81e7a2d0ab2c9f4b500c99d25b98b55254e0dc36c4e4e408ad84b7be0e24709d25447168b076ce7723d35462d055')
b2sums=('6ef608b204a4cb796585c5ff130ee642bce0e7a464099b7eaf9c9199203fc28ff0a1b260a731f9ba462a9b82e6f68be12fc622ed809ad41a1ab92adaa4993cbd')

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
