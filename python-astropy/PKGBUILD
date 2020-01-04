# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-astropy
pkgver=4.0
pkgrel=1
pkgdesc="A community python library for astronomy"
arch=('i686' 'x86_64')
url="http://www.astropy.org/"
license=('BSD')
depends=('python' 'python-numpy' 'python-scipy' 'python-h5py' 'cfitsio' 'expat' 'wcslib' 'erfa' 'python-jinja')
conflicts=('python-pyfits' 'python-vo')
makedepends=('cython')
source=("https://files.pythonhosted.org/packages/source/a/astropy/astropy-${pkgver}.tar.gz")
sha512sums=('c32e874d208f312f894643ab5b3d71dc37630e544da0ceb5ee998d752f9a055d32f6e4319f2cb6928637aaf8573bac58d2882bd636b6a89f5501e3ac7e5ab681')

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

