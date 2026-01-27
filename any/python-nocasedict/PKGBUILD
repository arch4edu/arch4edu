# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='nocasedict'
pkgname="python-${_name}"
pkgver='2.2.0'
pkgrel='1'
pkgdesc='A case-insensitive ordered dictionary for Python'
arch=('any')
url="https://github.com/pywbem/${_name}"
depends=('python-six')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
license=('GPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('145342221eb83c13b7c302b2591c4747823f96f7ca6789b86bdcbc2482027e83')

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
