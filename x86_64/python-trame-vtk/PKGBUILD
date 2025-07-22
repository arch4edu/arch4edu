# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-vtk
_npm_base=vue-vtk-js
pkgname=python-${_base}
pkgdesc="VTK widgets for trame"
pkgver=2.9.1
_npm_pkgver=3.2.2
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(BSD-3-Clause)
depends=(python-trame-client vtk openmpi fmt jsoncpp glew ospray openxr
  openvr ffmpeg hdf5-openmpi postgresql-libs netcdf pdal mariadb-libs
  liblas cgns adios2 libharu gl2ps verdict qt5-tools opencascade)
makedepends=(python-build python-installer python-hatchling python-wheel)
checkdepends=(python-pytest-xprocess python-pixelmatch python-seleniumbase python-pyvista) # python-trame-vuetify
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  https://registry.npmjs.org/${_npm_base}/-/${_npm_base}-${_npm_pkgver}.tgz
  https://raw.githubusercontent.com/Kitware/vtk-js/2d8de2853a1e63c12f9682acb3531083b77c4e3d/examples/OfflineLocalView/OfflineLocalView.html)
sha512sums=('64001c02fb83e4da4c5f74b8172b449d7e936e3bdbef2a983120473ea89a0ea1c68f628dfa74777ce54680ee4afddf9790c40dbe6f76aa658264811b5214a1fe'
            'b00526ad3f3c1d2f2e05a287034100cbebb4ad931b642f590c6b273f01768aaa15766c3542031977716db7f138bba41eacbe7c7f8ea4fdf489772f35e9382009'
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
  MPLBACKEND=Agg test-env/bin/python -m pytest \
    --ignore=tests/test_gc.py \
    -k 'not rendering[examples/validation/PyVistaInt64.py] and not rendering[examples/validation/PyVistaLookupTable.py] and not rendering[examples/validation/VolumeRendering.py]'
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
