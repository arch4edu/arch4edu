# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=samplomatic
pkgname=python-${_name}
pkgver=0.20.0
pkgrel=1
pkgdesc="A library that helps you sample randomizations of your quantum circuits"
arch=(any)
url=https://github.com/Qiskit/samplomatic
license=(Apache-2.0)
depends=(
    blas-openblas
    python-numpy
    python-orjson
    python-pybase64
    python-qiskit
    python-rustworkx
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
)
checkdepends=(
    jupyter-nbformat
    python-matplotlib
    python-plotly
    python-pylatexenc
    python-pytest
    python-qiskit-aer
    python-scipy-doctest
)
optdepends=(
    "jupyter-nbformat: visualization"
    "python-plotly: visualization"
    "python-matplotlib: visualization"
    "python-pylatexenc: LaTeX"
)
source=($_name::git+https://github.com/Qiskit/$_name.git#tag=$pkgver)
b2sums=('1e84671ae68b42ed560fbbf36902251ff3e3521b3c7ba9f45bfb2bc75a4bd52fed02e237889af5a82185c2867e6a74024593b63f1b09992644922cc4406ee1fb')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

check() {
    cd $_name
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf $_name
    test-env/bin/python -P -m pytest -o addopts="" test/unit
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
