# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='pywbem'
pkgbase="${_name}"
pkgname=('python-pywbem')
pkgver='1.7.2'
pkgrel='2'
pkgdesc='A WBEM client and related utilities'
arch=('x86_64' 'aarch64')
url="https://github.com/${_name}/${_name}"
depends=('python-pyyaml' 'python-six' 'python-requests'
	 'python-urllib3' 'python-nocasedict' 'python-nocaselist'
	 'python-yamlloader' 'python-ply')
makedepends=('python-build' 'python-installer' 'python-setuptools'
	     'python-mock' 'python-wheel')
license=('LGPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('9b4d0a0945f94e4d10d3e4151ebf0e149b311fbbd592a05ccaf41b4f5d172850')

build() {
  cd "${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" "dist/"*".whl"
  install -Dm0644 "LICENSE.txt" "${pkgdir}/usr/share/doc/${pkgname}/LICENSE"
}
