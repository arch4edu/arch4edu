# Contributor: Drew DeVault <sir@cmpwn.com>
# Contributor: Bruce Zhang <zttt183525594@gmail.com>
# Maintainer: Davide Depau <davide@depau.eu>

pkgname='python-pycrypto'
_pkgname='pycrypto'
pkgver=2.6.1
pkgrel=4
pkgdesc='Cryptographic primitives and algorithms for Python'
arch=('any')
url='https://pypi.python.org/pypi/pycrypto'
license=('Public domain')
depends=('python-flask')
makedepends=('python-setuptools')
provides=('python-pycryptodome' 'python-crypto')
source=(
  "https://files.pythonhosted.org/packages/60/db/645aa9af249f059cc3a368b118de33889219e0362141e75d4eaf6f80f163/pycrypto-${pkgver}.tar.gz"
  0001-replaced-time.clock-with-time.process_time-time-cloc.patch
)
sha512sums=('20a4aed4dac4e9e61d773ebc1d48ea577e9870c33f396be53d075a9bf8487d93e75e200179882d81e452efd0f6751789bac434f6f431b3e7c1c8ef9dba392847'
            '9a8c9812b3a13701571cb9cebb2fd755be7206f4045cbec76375259b716c2769dd25996cd8af89248cf7d9de0b088193a245442169c0c645ccd6083b529e3e50')

build() {
	cd "$_pkgname-$pkgver"
	python setup.py build
}

prepare() {
  cd "$_pkgname-$pkgver"
  patch -p1 < ../0001-replaced-time.clock-with-time.process_time-time-cloc.patch
}

package() {
	cd "$_pkgname-$pkgver"
	python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}

