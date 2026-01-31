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
pkgver=26.0
pkgrel=1
pkgdesc="The PyPA recommended tool for installing Python packages"
url="https://${_base}.pypa.io"
arch=(any)
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('00097de18ae8f80e4093752687a0eeadcc1fd4ba7e3ea8e78a18fffc72f85e679d60399d9117ba889750ce804ae05464bedc09ff87eae13d68c64c507fc7e759')

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
