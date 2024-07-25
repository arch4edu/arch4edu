# Maintainer: Grey Christoforo <first name at last name dot net>
# Co-Maintainer: Bert Peters <bert@bertptrs.nl>

pkgname=python-plotly
pkgver=5.23.0
pkgrel=1
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
    npm
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
     "js-build.patch"
)
sha256sums=('fffdb97d8ba828be95b331c4adabaeb8a8b2bbdcc6fee7fc4848f3d7095342bb'
            '347d8de2ed5c6529a0113086780ecdd0b21c0a167fa60a890ca18bbac0d99392')
options=(!strip !debug) # strip and debug aren't useful for python files and take forever

prepare() {
  cd python-plotly

  git clean -dfx
  patch -p1 < ../js-build.patch
}

build() {
  cd python-plotly/packages/python/plotly

  # Skip the dependency check as the version bounds on jupyterlab are too tight
  # and don't allow 4.x, which Arch currently ships.
  python -m build --wheel --no-isolation --skip-dependency-check
}

check() {
  cd python-plotly/packages/python/plotly
  pytest plotly/tests/test_core
}

package() {
  cd python-plotly/packages/python/plotly
  python -m installer --destdir="$pkgdir"/ dist/*.whl
  mv "${pkgdir}/usr/etc" "${pkgdir}"

  # symlink the path where static assets are installed, otherwise jupyterlab
  # will not be able to load the extension properly
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  ln -s "$site_packages/jupyterlab_plotly/labextension/static" "$pkgdir/usr/share/jupyter/labextensions/jupyterlab-plotly/"

  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
