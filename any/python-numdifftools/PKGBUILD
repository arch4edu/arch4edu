# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lex Black <autumn-wind@web.de>
# Contributor: Hector <hsearaDOTatDOTgmailDOTcom>
_base=numdifftools
pkgname=python-${_base}
pkgver=0.11.2
pkgrel=1
pkgdesc="Solve automatic numerical differentiation problems in one or more variables"
url="https://github.com/pbrod/${_base}"
license=(BSD-3-Clause)
arch=(x86_64)
depends=(python-scipy)
makedepends=(python-build python-installer python-pdm-backend python-wheel)
checkdepends=(python-pytest-cov python-matplotlib python-lineprofiler python-hypothesis python-statsmodels python-algopy)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('fa9a3b5ed3dd1baccc45bf03503dde5cb0d3455db4b1b6c5bce88cf1fadc4b3c1ffa6a27653bf9a37285c6aa72a89b6ae3b0cc0a572477ba4da8111eefe766c7')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest src/${_base}/tests
  #-k 'not nd_scipy and not scripts and not first_order_derivative and not scalar_to_vector and not on_matrix_valued_function and not issue_25 and not run_gradient_and_hessian_benchmarks and not on_function_and_follow_function and not on_class_method_and_follow_function and not on_all_class_methods_without_decorator'
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
