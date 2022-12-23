# Maintainer: Ondrej Hosek <ondra.hosek@gmail.com>
# Contributor: Yacob Zitouni <yacob.zitouni@gmail.com>
# Contributor: Michael Kapelko <kornerr@gmail.com>
# Contributor: Angelo Theodorou <encelo@users.sourceforge.net>
# Contributor: David H. Bronke <whitelynx@gmail.com>
# Contributor: Andrea Ratto <andrearatto_liste@yahoo.it>

_name=oracledb
pkgname=python-oracledb
pkgver=1.2.1
pkgrel=1
pkgdesc="Python extension module that allows access to Oracle databases"
arch=('i686' 'x86_64')
url='https://oracle.github.io/python-oracledb/'
license=('Apache' 'custom:UPL')
depends=('python' 'python-cryptography')
optdepends=('oracle-instantclient-basic')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'cython')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
b2sums=('98a9b1750a4002e1223a25fe4957b5a0dae633c15b6c87a374ac6b46ee027e6f368b49a13eaa67500d4301555c6c672eeba5b922512f50b5a5aa57ba8530f811')

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
