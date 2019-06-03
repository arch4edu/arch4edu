# Contributor(s): Drew DeVault <sir@cmpwn.com>
# Maintainer: Bruce Zhang <zttt183525594@gmail.com>

pkgname='python-pycrypto'
_pkgname='pycrypto'
pkgver=2.6.1
pkgrel=3
pkgdesc='Cryptographic primitives and algorithms for Python'
arch=('any')
url='https://pypi.python.org/pypi/pycrypto'
license=('Public domain')
depends=('python-flask')
makedepends=('python-setuptools')
provides=('python-pycryptodome' 'python-crypto')
source=("https://files.pythonhosted.org/packages/60/db/645aa9af249f059cc3a368b118de33889219e0362141e75d4eaf6f80f163/pycrypto-${pkgver}.tar.gz")
sha256sums=('f2ce1e989b272cfcb677616763e0a2e7ec659effa67a88aa92b3a65528f60a3c')

build() {
	cd "$_pkgname-$pkgver"
	python setup.py build
}

package() {
	cd "$_pkgname-$pkgver"
	python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
