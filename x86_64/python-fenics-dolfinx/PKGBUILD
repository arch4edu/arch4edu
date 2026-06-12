# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=dolfinx
pkgname=python-fenics-${_base}
pkgdesc="Next generation FEniCS problem solving environment (python interface)"
pkgver=0.11.0.post0
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(LGPL-3.0-or-later GPL-3.0-or-later)
depends=(dolfinx python-mpi4py)
makedepends=(python-build python-installer python-scikit-build-core python-wheel nanobind hdf5-openmpi)
checkdepends=(python-pytest python-sympy python-scipy python-matplotlib python-numba)
optdepends=('python-pyvista: for plotting'
  'python-numba: for jit support'
  'slepc: for eigenvalue solver support'
  'gmsh: for extract data from Gmsh models')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('97e6cd94ae7ff0f0e97df30217037d0cf8585b518d606f865e76b711007b74fc34a43ab26fb2fa79c95e4765a908842e2634d62d4a82d7e5c38e8c841e622c88')

build() {
  # Force CMake to find parallel HDF5
  export CMAKE_ARGS="-DHDF5_IS_PARALLEL=TRUE -DHDF5_ROOT=/usr"
  cd ${_base}-${pkgver}/python
  source /etc/profile.d/petsc.sh
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  # Force CMake to find parallel HDF5
  export CMAKE_ARGS="-DHDF5_IS_PARALLEL=TRUE -DHDF5_ROOT=/usr"
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer python/dist/*.whl
  MPLBACKEND=Agg test-env/bin/python -m pytest python/test/unit \
    -k 'not mixed_topology_partitioning and not custom_mesh_loop_rank1[complex64] and not custom_mesh_loop_rank1[complex128] and not read_write_p2_mesh[Encoding.HDF5] and not read_write_p2_mesh[Encoding.ASCII]' \
    --ignore=python/test/unit/mesh/test_higher_order_mesh.py \
    --ignore=python/test/unit/io/test_xdmf_function.py \
    --ignore=python/test/unit/io/test_adios2.py
  MPLBACKEND=Agg test-env/bin/python -m pytest python/demo/test.py \
  -k 'not demos[path5-demo_gmsh.py] and not demos[path13-demo_pml.py] and not demos[path18-demo_scattering_boundary_conditions.py] and not demos[path19-demo_static-condensation.py] and not demos_mpi[path5-demo_gmsh.py] and not demos_mpi[path13-demo_pml.py] and not demos_mpi[path18-demo_scattering_boundary_conditions.py] and not demos_mpi[path19-demo_static-condensation.py]'
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" python/dist/*.whl
  install -Dm 644 COPYING* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
