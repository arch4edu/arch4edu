# Maintainer: Ondrej Hosek <ondra.hosek@gmail.com>
# Contributor: Yacob Zitouni <yacob.zitouni@gmail.com>
# Contributor: Michael Kapelko <kornerr@gmail.com>
# Contributor: Angelo Theodorou <encelo@users.sourceforge.net>
# Contributor: David H. Bronke <whitelynx@gmail.com>
# Contributor: Andrea Ratto <andrearatto_liste@yahoo.it>

_name=oracledb
pkgname=python-oracledb
pkgver=4.0.2
pkgrel=1
pkgdesc="Python extension module that allows access to Oracle databases"
arch=('i686' 'x86_64')
url='https://oracle.github.io/python-oracledb/'
license=('Apache' 'custom:UPL')
depends=('python' 'python-cryptography')
optdepends=('oracle-instantclient-basic')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'cython')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
b2sums=('24d9366ecc378d87008647ed850ef03db70c0e2636bd9aa1d36757384676942950bf87e26f60394a14acc93284ed18cee34077770b1e61020e64ea156c490622')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m build --wheel
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="$pkgdir/" dist/*.whl
  install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt
  install -Dm644 README.txt "$pkgdir"/usr/share/doc/$pkgname/README.txt
}
