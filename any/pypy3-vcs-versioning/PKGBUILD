# Maintainer: Jingbei Li <i@jingbei.li>
_base=vcs_versioning
pkgname=pypy3-vcs-versioning
pkgdesc="The blessed package to manage your versions by vcs metadata"
pkgver=2.2.2
pkgrel=1
arch=(any)
url="https://github.com/pypa/setuptools-scm"
license=(MIT)
depends=(pypy3-packaging)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/09/95/c95bb74950763a163defcf4cedf6c5edfca1d623fd5031b76516ece85076/vcs_versioning-2.2.2.tar.gz)
sha256sums=('4ac4ded78720cdb4d0291ae58ace87e1e9201912e1023f3029c6cce5c9152cfb')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
