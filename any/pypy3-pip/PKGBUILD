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
pkgver=26.1.1
pkgrel=1
pkgdesc="The PyPA recommended tool for installing Python packages"
url="https://${_base}.pypa.io"
arch=(any)
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('e9419b7b2756c5ee43ec141c14f0d34349dea8b35c0ff5cbd7802fe090ef1340a4eada25f3007a71967544936245d035b05805001ace1a55b61f3e5fcb9afd0f')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  mkdir -p "${pkgdir}/usr/bin"
  mv "${pkgdir}/opt/pypy3/bin/pip" "${pkgdir}/usr/bin/pip-pypy3"
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
