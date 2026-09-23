# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lex Black <autumn-wind@web.de>
# Contributor: Hector <hsearaDOTatDOTgmailDOTcom>
_base=numdifftools
pkgname=python-${_base}
pkgver=0.11.1
pkgrel=1
pkgdesc="Solve automatic numerical differentiation problems in one or more variables"
url="https://github.com/pbrod/${_base}"
license=(BSD-3-Clause)
arch=(x86_64)
depends=(python-scipy)
makedepends=(python-build python-installer python-pdm-backend python-wheel)
checkdepends=(python-pytest-cov python-matplotlib python-lineprofiler python-hypothesis python-statsmodels python-algopy)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('42a5889216b2437720499bb689de5def76eb8f17f578c907115b179662d6e69e9350e25f72151f5667e5ba2e268d379de74ae036151fe7aa718bb995bbde536c')

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
