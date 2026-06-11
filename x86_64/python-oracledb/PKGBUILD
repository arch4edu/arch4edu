# Maintainer: Ondrej Hosek <ondra.hosek@gmail.com>
# Contributor: Yacob Zitouni <yacob.zitouni@gmail.com>
# Contributor: Michael Kapelko <kornerr@gmail.com>
# Contributor: Angelo Theodorou <encelo@users.sourceforge.net>
# Contributor: David H. Bronke <whitelynx@gmail.com>
# Contributor: Andrea Ratto <andrearatto_liste@yahoo.it>

_name=oracledb
pkgname=python-oracledb
pkgver=3.4.1
pkgrel=1
pkgdesc="Python extension module that allows access to Oracle databases"
arch=('i686' 'x86_64')
url='https://oracle.github.io/python-oracledb/'
license=('Apache' 'custom:UPL')
depends=('python' 'python-cryptography')
optdepends=('oracle-instantclient-basic')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'cython')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
b2sums=('a2b295b6fef4f09372476be9af218827673838309840b770a3312b081ea95b1656dd7f2cf36b71b37ea50afdffc543aa2bf8b4dedc0a69ccc82b74c13095f368')

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
