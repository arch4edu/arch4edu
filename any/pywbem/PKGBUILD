# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='pywbem'
pkgbase="${_name}"
pkgname=('python-pywbem')
pkgver='1.6.2'
pkgrel='1'
pkgdesc='A WBEM client and related utilities'
arch=('x86_64' 'aarch64')
url="https://github.com/${_name}/${_name}"
depends=('python-pyyaml' 'python-six' 'python-requests'
	 'python-urllib3' 'python-nocasedict' 'python-nocaselist'
	 'python-yamlloader')
makedepends=('python' 'python-setuptools' 'python-wheel'
	     'python-mock' 'python-ply')
license=('LGPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('0437e869719effd85ba7316d5db1e8783dd4ccec4b05e95d49e878265abfc820')

package() {
  cd "${_name}-${pkgver}"
  python setup.py install -O1 --root="${pkgdir}"
}
