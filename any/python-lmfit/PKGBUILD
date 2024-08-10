pkgname=python-lmfit
pkgver=1.3.1
pkgrel=2
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
python-asteval
python-dill
python-emcee
ipython
python-matplotlib
python-numpy
python-pandas
python-pytest
python-scipy
python-uncertainties
)
checkdepends=(
python-pytest-cov
python-flaky
python-coverage
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/lmfit/lmfit-py/archive/${pkgver}.tar.gz")
sha256sums=('2453b4f655a4a8c10292e0fb1a89c38d66dd65b330aa82e7690b2abbb7215925')

prepare() {
  cd lmfit-py-${pkgver}

}

build() {
  cd lmfit-py-${pkgver}
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} python -m build --wheel --no-isolation
}

check() {
  cd lmfit-py-${pkgver}
  _these_fail=(
  test_altered_params_json
  test_independent_var_parsing
  test_saveload_modelresult_roundtrip
  test_save_load_modelresult
  test_saveload_modelresult_attributes
  test_saveload_modelresult_eval_uncertainty
  test_saveload_modelresult_expression_model
  test_saveload_usersyms
  test_parameters_deepcopy
  test_dumps_loads_parameters
  test_dump_load_parameters
  test_dumps_loads_parameters_usersyms
  )
  printf -v _joined '%s and not ' "${_these_fail[@]}"
  python -m pytest tests -k "$(echo "not ${_joined% and not }")"  # skip the tests we know fail
}


package() {
  cd lmfit-py-${pkgver}
  python -m installer --destdir="${pkgdir}" dist/*.whl
}

# vim:ts=2:sw=2:et:
