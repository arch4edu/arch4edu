# Maintainer: Ondrej Hosek <ondra.hosek@gmail.com>
# Contributor: Yacob Zitouni <yacob.zitouni@gmail.com>
# Contributor: Michael Kapelko <kornerr@gmail.com>
# Contributor: Angelo Theodorou <encelo@users.sourceforge.net>
# Contributor: David H. Bronke <whitelynx@gmail.com>
# Contributor: Andrea Ratto <andrearatto_liste@yahoo.it>

_name=oracledb
pkgname=python-oracledb
pkgver=1.4.2
pkgrel=1
pkgdesc="Python extension module that allows access to Oracle databases"
arch=('i686' 'x86_64')
url='https://oracle.github.io/python-oracledb/'
license=('Apache' 'custom:UPL')
depends=('python' 'python-cryptography')
optdepends=('oracle-instantclient-basic')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'cython')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
b2sums=('2167eaa9f61075ef41baf57b411fd353dedd11e6e758f7e3c5df160e1f0190857a4060017c1c9e1a937d2ab4d96a184e49b140ebdd0446dce08dd763cdb4b882')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="$pkgdir/" dist/*.whl
  install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt
  install -Dm644 README.txt "$pkgdir"/usr/share/doc/$pkgname/README.txt
}
