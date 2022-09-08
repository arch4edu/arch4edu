# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Tim Rakowski <tim.rakowski@gmail.com>
_base=pep8
pkgname=python-${_base}
pkgver=1.7.1
pkgrel=3
pkgdesc="The final release of the pep8 package"
arch=('any')
url="https://github.com/PyCQA/pycodestyle"
license=(MIT)
depends=(python)
makedepends=(python-setuptools)
provides=('pep8')
source=(${url}/archive/${pkgver}.tar.gz)
sha512sums=('87206295d8b95c7129ca21a2644dc6ac78d840627d6ffd4d3ed088708833c259b7d6df70463385e8336af7e193f36888a6a69caf8bc43b6aae6b642fe61e99ee')

build() {
  cd "pycodestyle-${pkgver}"
  python setup.py build
}

package() {
  cd "pycodestyle-${pkgver}"
  export PYTHONHASHSEED=0
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
