# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-vtk
_npm_base=vue-vtk-js
pkgname=python-${_base}
pkgdesc="VTK widgets for trame"
pkgver=2.10.1
_npm_pkgver=3.3.1
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(BSD-3-Clause)
depends=(python-trame-client vtk openmpi fmt jsoncpp glew ospray openxr
  openvr ffmpeg hdf5-openmpi postgresql-libs netcdf pdal mariadb-libs
  liblas cgns adios2 libharu gl2ps verdict qt5-tools opencascade)
makedepends=(python-build python-installer python-hatchling python-wheel)
checkdepends=(python-pytest-xprocess python-pixelmatch python-playwright python-pyvista python-pytest-asyncio) # python-trame-vuetify
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  https://registry.npmjs.org/${_npm_base}/-/${_npm_base}-${_npm_pkgver}.tgz
  https://raw.githubusercontent.com/Kitware/vtk-js/2d8de2853a1e63c12f9682acb3531083b77c4e3d/examples/OfflineLocalView/OfflineLocalView.html)
sha512sums=('40fe76998ea2ba5da40814c9349aa6bb5d997cc8ec26217ced2045059c493d612f5050d89d287b4a2e0d616ef76e234665c0ab398d3670af6f1d733acd2cbdd1'
            'fd3a504753b66f9fc0ec0997dc33210c307f15157729e4a8837bf782c5f6af620c625597ac227c31b6635f9573c30e1c64e2f87bed8e6fcedfe5cca62e775afb'
            '6f09789d876b431370dc55b04ba327092af218d1abea52dd4ec4c9de5b4340cbac2218f438bb231e0cab108f7edcc54d2e15d0c0b262067afb7a515a451414f5')

prepare() {
  sed -i 's/^include trame_vtk\/LICENSE/#include trame_vtk\/LICENSE/' ${_base}-${pkgver}/MANIFEST.in
}

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  MPLBACKEND=Agg test-env/bin/python -m pytest tests/test_import.py
  # -k 'not rendering[examples/validation/PyVistaInt64.py] and not rendering[examples/validation/PyVistaLookupTable.py] and not rendering[examples/validation/VolumeRendering.py]'
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  # Install trame-vtk.js
  install -Dm 644 ${srcdir}/package/dist/${_npm_base::-3}.umd.js ${pkgdir}${site_packages}/${_base/-/_}/modules/common/serve/trame-vtk.js
  # Install static_viewer.html
  mv ${srcdir}/OfflineLocalView.html ${pkgdir}${site_packages}/${_base/-/_}/tools/static_viewer.html

  rm ${pkgdir}${site_packages}/trame/__init__.py
  rm ${pkgdir}${site_packages}/trame/modules/__init__.py
  rm ${pkgdir}${site_packages}/trame/widgets/__init__.py
  rm ${pkgdir}${site_packages}/trame/tools/__init__.py
}
