# Maintainer: Grey Christoforo <first name at last name dot net>
# Co-Maintainer: Bert Peters <bert@bertptrs.nl>

pkgname=python-plotly
pkgver=5.13.1
pkgrel=1
pkgdesc="An open-source, interactive graphing library"
arch=('x86_64')
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
python-setuptools
python-jupyter_core
python-tornado
jupyterlab
)
checkdepends=(
python-requests
python-pytest
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/plotly/plotly.py/archive/v${pkgver}.tar.gz")
options=(!strip) # strip isn't useful for python files and takes forever
sha256sums=('794b876446b545584601a8d98f47fa61286ebc32036f4be072b9961d8b7b95ac')

build() {
  cd plotly.py-${pkgver}/packages/python/plotly
  SKIP_NPM=1 python setup.py build
}

check() {
  cd plotly.py-${pkgver}/packages/python/plotly
  pytest plotly/tests/test_core
}

package() {
  cd plotly.py-${pkgver}/packages/python/plotly
  SKIP_NPM=1 python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  mv ${pkgdir}/usr/etc ${pkgdir}

  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
