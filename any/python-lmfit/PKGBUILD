pkgname=python-lmfit
pkgver=1.3.4
pkgrel=1
pkgdesc="Non-Linear Least Squares Minimization, based on scipy.optimize"
arch=(any)
url=http:/lmfit.github.io/lmfit-py/
license=('BSD-3-Clause')
makedepends=(
python-build
python-installer
python-wheel
python-setuptools-scm
)
depends=(
python
python-asteval
python-dill
python-emcee
python-matplotlib
python-numdifftools
python-numpy
python-pandas
python-scipy
python-uncertainties
)
checkdepends=(
python-pytest-cov
python-flaky
python-coverage
python-pytest
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/lmfit/lmfit-py/archive/${pkgver}.tar.gz")
sha256sums=('f40628814051140ac6a7a7c17ee075bb33fac0b00ccd32ff8bd73eebb35e0f40')

prepare() {
  cd lmfit-py-${pkgver}

}

build() {
  cd lmfit-py-${pkgver}
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} python -m build --wheel --no-isolation
}

check() {
  cd lmfit-py-${pkgver}
  python -m pytest
}


package() {
  cd lmfit-py-${pkgver}
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dt "${pkgdir}/usr/share/licenses/${pkgname}" -m644 LICENSE
}

# vim:ts=2:sw=2:et:
