# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=dolfinx
pkgname=python-fenics-${_base}
pkgdesc="Next generation FEniCS problem solving environment (python interface)"
pkgver=0.5.1
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(LGPL3)
depends=(dolfinx python-mpi4py)
makedepends=(cmake python-setuptools pybind11)
optdepends=('gmsh: for extract data from Gmsh models')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('2394f3650923723e9a81643f5e1d42ae03e58274872921daeb182c5b99b8e755d91217d9e05fb3d301c8f7cbce3faff84f233232c7d91b541fd405a359b06ea4')

build() {
  cd ${_base}-${pkgver}/python
  source /etc/profile.d/petsc.sh
  python setup.py build
}

package() {
  cd ${_base}-${pkgver}/python
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
}
