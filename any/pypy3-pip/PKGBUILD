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
pkgver=24.0
pkgrel=1
pkgdesc="The PyPA recommended tool for installing Python packages"
url="https://pip.pypa.io"
arch=(any)
license=(MIT)
depends=(pypy3 pypy3-setuptools)
source=(https://github.com/pypa/${_base}/archive/${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('0c2ecb2ecde4f155c83468d35bc4f52f37efffc16821ae7c706d035e1e8cc3709b41cb10f8140ff09205e8bbdba2c76128ad76d1cbd18401328b619228e834df')
b2sums=('17a7ed9e15e9b8efa0d3e3c5586dc446958b62cf9ba52155a0d1ad97a3e212ee7a08a0e88a592718fc3d542eb8f434155a75cb98d90c008904bd8f59bd2b40b6')

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
