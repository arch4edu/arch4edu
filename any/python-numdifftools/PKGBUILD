# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lex Black <autumn-wind@web.de>
# Contributor: Hector <hsearaDOTatDOTgmailDOTcom>
_base=numdifftools
pkgname=python-${_base}
pkgver=0.9.41
pkgrel=2
pkgdesc="Solve automatic numerical differentiation problems in one or more variables"
url="https://github.com/pbrod/${_base}"
license=('custom:BSD-3-clause')
arch=(x86_64)
depends=(python-scipy)
makedepends=(python-build python-installer python-pytest-runner python-wheel)
checkdepends=(python-hypothesis python-matplotlib python-algopy python-lineprofiler)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('7eb26ca23238b1592a6d230d9b59d49e2574b97151de66fda158bc37e49e1598e7ca931628c9a163a2614a4e24bbb165f22b50ec043d43486d415123517c7148')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest src/${_base}/tests -k 'not nd_scipy and not scripts and not first_order_derivative and not scalar_to_vector and not on_matrix_valued_function and not issue_25 and not run_gradient_and_hessian_benchmarks and not on_function_and_follow_function and not on_class_method_and_follow_function and not on_all_class_methods_without_decorator'
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
}
