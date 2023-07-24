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
pkgver=23.2.1
pkgrel=1
pkgdesc="The PyPA recommended tool for installing Python packages"
url="https://pip.pypa.io"
arch=(any)
license=(MIT)
depends=(pypy3 pypy3-setuptools)
source=(https://github.com/pypa/${_base}/archive/${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('a6c629976c332cffe5dff0ec1e201d694c7a42fa8def202ebf1db251a6dbd90091eaac89c36a354a0cf0c60cdb267b4e0ec9ff6a88b0ac61cfaafdf159e34fc8')
b2sums=('9e7855aae371a773a070c24b50f985dac6ff7c2412d51e268368b911b92d0d0b52a839f9d761d5f6aaff33f1e7570d5f930e5063e8af98aa99f50d2f1c1b5ed2')

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
