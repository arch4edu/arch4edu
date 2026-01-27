# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='nocaselist'
pkgname="python-${_name}"
pkgver='2.2.0'
pkgrel='1'
pkgdesc='A case-insensitive list for Python'
arch=('any')
url="https://github.com/pywbem/${_name}"
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
license=('GPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('149cab2e853c397b88502bf9dbbb52620cb34148659f088a1ffc95d6633a6c17')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  export SETUPTOOLS_SCM_PRETEND_VERSION="${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" "dist/"*".whl"
  install -Dm0644 "LICENSE" "${pkgdir}/usr/share/doc/${pkgname}/LICENSE"
}
