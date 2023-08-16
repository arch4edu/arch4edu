# Maintainer: Grey Christoforo <first name at last name dot net>
# Co-Maintainer: Bert Peters <bert@bertptrs.nl>

pkgname=python-plotly
pkgver=5.16.0
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
source=(
"${pkgname}-${pkgver}.tar.gz::https://github.com/plotly/plotly.py/archive/v${pkgver}.tar.gz"
fix_for_python3.11.patch
)
options=(!strip) # strip isn't useful for python files and takes forever
sha256sums=('e353b9c29c040847b7a0104e6da50996ebe42d95bd7903e991d325060254d16a'
            'e235e66eae73bcd8579a64a241a79fb7cad0aa94e62f45acc3ac487277282b1b')

prepare() {
  cd plotly.py-${pkgver}
  cat ../fix_for_python3.11.patch | patch -p1
}

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
