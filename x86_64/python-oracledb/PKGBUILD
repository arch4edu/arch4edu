# Maintainer: Ondrej Hosek <ondra.hosek@gmail.com>
# Contributor: Yacob Zitouni <yacob.zitouni@gmail.com>
# Contributor: Michael Kapelko <kornerr@gmail.com>
# Contributor: Angelo Theodorou <encelo@users.sourceforge.net>
# Contributor: David H. Bronke <whitelynx@gmail.com>
# Contributor: Andrea Ratto <andrearatto_liste@yahoo.it>

_name=oracledb
pkgname=python-oracledb
pkgver=1.3.1
pkgrel=1
pkgdesc="Python extension module that allows access to Oracle databases"
arch=('i686' 'x86_64')
url='https://oracle.github.io/python-oracledb/'
license=('Apache' 'custom:UPL')
depends=('python' 'python-cryptography')
optdepends=('oracle-instantclient-basic')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'cython')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
b2sums=('18986359a8ca1ad5dc6bebd45a42153f0ed6fd775e9b1920c1c0a08fbc2b29b7ddf1c10c1dcfc22b0711b794c201fbb3b6b60a939e0bcfdedaf33afb76dc49cd')

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
