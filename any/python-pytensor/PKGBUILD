# New Maintainer: SecByShresth <Shresthpaul133@gmail.com>
# Maintainer: Harriet O'Brien <harrietobrien@protonmail.com>
# Contributor: Carl Smedstad <carsme@archlinux.org>

pkgname=python-pytensor
_pkgname=${pkgname#python-}
pkgver=2.38.0
pkgrel=1
pkgdesc="Fork of Aesara -- Library for defining, optimizing, and efficiently evaluating mathematical expressions involving multi-dimensional arrays"
arch=(x86_64)
url="https://github.com/pymc-devs/pytensor"
license=(LicenseRef-PyTensorLicense)
depends=(
  glibc
  python
  python-cons
  python-etuples
  python-filelock
  python-llvmlite
  python-logical-unification
  python-minikanren
  python-numpy
  python-pydot
  python-scipy
  python-setuptools
)
makedepends=(
  cython
  git
  python-build
  python-installer
  python-versioneer
  python-wheel
)
checkdepends=(
  python-jax
  python-numba
  python-pytest
  python-pytest-mock
  python-tensorflow-probability
)
optdepends=(
  'python-jax: for graph transpilation compilation via JAX'
  'python-numba: for graph transpilation compilation via Numba'
  'python-tensorflow-probability: for graph transpilation compilation via JAX'
)
source=("${url}/archive/refs/tags/rel-${pkgver}.tar.gz")
sha256sums=('535b8cb894bd00fc45120d8b6eb92946199e4f315ad536fa139b010e30fb5350')

build() {
  cd "$srcdir/$_pkgname-rel-$pkgver"
  python -m build --wheel --no-isolation
}

:||{
check() {
  cd "$srcdir/$_pkgname-rel-$pkgver"

  local deselect_test_args=(
    # d3viz functionality is currently not being maintained, see:
    # https://github.com/pymc-devs/pytensor/issues/333
    --deselect=tests/d3viz/test_d3viz.py

    # Raises ImportError when importing 'bijectors' from "partially
    # initialized" module 'tensorflow_probability.substrates.jax', unsure why.
    --deselect=tests/link/jax/test_scalar.py

    # Requires python-pytest-benchmark.
    --deselect=tests/link/jax/test_elemwise.py::test_logsumexp_benchmark

    # Most time-consuming test files, deselect these to make test duration
    # more reasonable.
    --deselect=tests/link/numba/test_elemwise.py
    --deselect=tests/link/numba/test_scan.py
    --deselect=tests/scalar/test_basic.py
    --deselect=tests/scan/test_basic.py
    --deselect=tests/scan/test_checkpoints.py
    --deselect=tests/scan/test_rewriting.py
    --deselect=tests/sparse/test_basic.py
    --deselect=tests/sparse/test_var.py
    --deselect=tests/tensor/conv/test_abstract_conv.py
    --deselect=tests/tensor/rewriting/test_basic.py
    --deselect=tests/tensor/rewriting/test_elemwise.py
    --deselect=tests/tensor/rewriting/test_math.py
    --deselect=tests/tensor/rewriting/test_subtensor.py
    --deselect=tests/tensor/test_basic.py
    --deselect=tests/tensor/test_blas.py
    --deselect=tests/tensor/test_blockwise.py
    --deselect=tests/tensor/test_casting.py
    --deselect=tests/tensor/test_elemwise.py
    --deselect=tests/tensor/test_extra_ops.py
    --deselect=tests/tensor/test_inplace.py
    --deselect=tests/tensor/test_math.py
    --deselect=tests/tensor/test_math_scipy.py
    --deselect=tests/tensor/test_slinalg.py
    --deselect=tests/tensor/test_sort.py
    --deselect=tests/tensor/test_subtensor.py
  )

  rm -rf tmp_install
  python -m installer --destdir=tmp_install dist/*.whl

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  export PYTHONPATH="$PWD/tmp_install/$site_packages"
  pytest tests "${deselect_test_args[@]}"
}
}

package() {

  cd "$srcdir/$_pkgname-rel-$pkgver"

  python -m installer --destdir="/$pkgdir" dist/*.whl
  #python -m installer --destdir="/usr/bin" dist/*.whl
  #python -m installer --destdir="/opt" dist/*.whl

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE.txt
}
options=(!debug !emptydirs)
