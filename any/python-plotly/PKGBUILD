# Maintainer: Grey Christoforo <first name at last name dot net>
# Co-Maintainer: Bert Peters <bert@bertptrs.nl>

pkgname=python-plotly
pkgver=5.20.0
pkgrel=3
pkgdesc="An open-source, interactive graphing library"
arch=('any')
url="https://github.com/plotly/plotly.py"
license=('MIT')
depends=(
    python
    python-tenacity
)
# optdepends based on optional_requirements.txt
optdepends=(
    ipython
    jupyterlab
    python-ipywidgets
    python-numpy
    python-matplotlib
    python-pillow
    python-scipy
    python-ipykernel
    python-pandas
    python-colorcet
    python-inflect
    python-psutil
)
makedepends=(
    git
    python-wheel
    python-build
    python-installer
    python-setuptools
    python-jupyter_core
    python-tornado
    jupyterlab
)
checkdepends=(
     python-requests
     python-pytest
)
source=(
     "${pkgname}::git+https://github.com/plotly/plotly.py#tag=v$pkgver"
)
sha256sums=('b0e4718894929e788aa5823d999f18246997dc256d94adc51e26b205c318ef50')
options=(!strip !debug) # strip and debug aren't useful for python files and take forever

prepare() {
  cd python-plotly/packages/python/plotly

  git clean -dfx
}

build() {
  cd python-plotly/packages/python/plotly

  # Skip the dependency check as the version bounds on jupyterlab are too tight
  # and don't allow 4.x, which Arch currently ships.
  SKIP_NPM=1 python -m build --wheel --no-isolation --skip-dependency-check
}

check() {
  cd python-plotly/packages/python/plotly
  pytest plotly/tests/test_core
}

package() {
  cd python-plotly/packages/python/plotly
  python -m installer --destdir="$pkgdir"/ dist/*.whl
  mv "${pkgdir}/usr/etc" "${pkgdir}"

  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
