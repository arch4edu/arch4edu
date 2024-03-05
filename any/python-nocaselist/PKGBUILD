# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='nocaselist'
pkgname="python-${_name}"
pkgver='2.0.0'
pkgrel='2'
pkgdesc='A case-insensitive list for Python'
arch=('any')
url="https://github.com/pywbem/${_name}"
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
license=('GPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('2e13029432b95d4890fb75c5d97d3d5a002940de14ac4ea0569e6a4d9fd81d71')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" "dist/"*".whl"
  install -Dm0644 "LICENSE" "${pkgdir}/usr/share/doc/${pkgname}/LICENSE"
}
