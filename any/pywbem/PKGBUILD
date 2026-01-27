# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='pywbem'
pkgbase="${_name}"
pkgname=('python-pywbem')
pkgver='1.9.0'
pkgrel='1'
pkgdesc='A WBEM client and related utilities'
arch=('x86_64' 'aarch64')
url="https://github.com/${_name}/${_name}"
depends=('python-pyyaml' 'python-six' 'python-requests'
	 'python-urllib3' 'python-nocasedict' 'python-nocaselist'
	 'python-yamlloader' 'python-ply')
makedepends=('python-build' 'python-installer' 'python-setuptools'
	 'python-setuptools-scm' 'python-mock' 'python-wheel')
license=('LGPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c6c19c3028dfefac7cd4e99c042719c29122eb1f59b21dd4bc87b53edb82eda5')

build() {
  cd "${_name}-${pkgver}"
  export SETUPTOOLS_SCM_PRETEND_VERSION="${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" "dist/"*".whl"
  install -Dm0644 "LICENSE.txt" "${pkgdir}/usr/share/doc/${pkgname}/LICENSE"
}
