# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-astropy
pkgver=3.1.2
pkgrel=1
pkgdesc="A community python library for astronomy"
arch=('i686' 'x86_64')
url="http://www.astropy.org/"
license=('BSD')
depends=('python' 'python-numpy' 'python-scipy' 'python-h5py' 'cfitsio' 'expat' 'wcslib' 'erfa' 'python-jinja')
conflicts=('python-pyfits' 'python-vo')
makedepends=('cython')
source=("https://files.pythonhosted.org/packages/source/a/astropy/astropy-${pkgver}.tar.gz")
md5sums=('2e197984c6ab44672b807bc25ce4b03f')

build() {
  cd ${srcdir}/astropy-${pkgver}

  python setup.py build --use-system-libraries --offline
}

package() {
  cd ${srcdir}/astropy-${pkgver}

  install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}/"
  install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" licenses/*
  python setup.py install --offline --root=${pkgdir} --prefix=/usr --optimize=1
}

