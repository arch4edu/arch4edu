# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='nocasedict'
pkgname="python-${_name}"
pkgver='2.0.1'
pkgrel='2'
pkgdesc='A case-insensitive ordered dictionary for Python'
arch=('any')
url="https://github.com/pywbem/${_name}"
depends=('python-six')
makedepends=('python-build' 'python-installer' 'python-setuptools'  'python-wheel')
license=('GPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('d2052d842ea59878cc6196faaac89cad7308d3a4cc21ec7318db9946397b13a6')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" "dist/"*".whl"
  install -Dm0644 "LICENSE" "${pkgdir}/usr/share/doc/${pkgname}/LICENSE"
}
