# Maintainer: Grey Christoforo <first name [at] last name [dot] net>

pkgname=python-lmfit
pkgver=1.2.2
pkgrel=1
pkgdesc="Non-Linear Least Squares Minimization, with flexible Parameter settings, based on scipy.optimize.leastsq, and with many additional classes and methods for curve fitting"
arch=(x86_64)
url=http:/lmfit.github.io/lmfit-py/
license=(BSD)
depends=('python' 'python-numpy' 'python-scipy' 'python-asteval' 'python-uncertainties')
makedepends=(python-setuptools-scm)
source=(https://github.com/lmfit/lmfit-py/archive/${pkgver}.tar.gz)
sha256sums=('fbd401317d5639c7fd23150efc00a387691f8d45ad690e2a3aaea12e951baf6f')

build() {
  cd "$srcdir/lmfit-py-$pkgver"
  SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver python setup.py build
}

package(){
  cd "$srcdir/lmfit-py-$pkgver"
  SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}

# vim:ts=2:sw=2:et:
