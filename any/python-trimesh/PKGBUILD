# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Auto update bot <auto-update-bot@arch4edu.org>
# Contributor: Brad Pitcher <bradpitcher@gmail.com>
# Contributor: Jelle van der Waa <jelle@archlinux.org>

_base=trimesh
pkgname=python-${_base}
pkgver=4.4.9
pkgrel=1
pkgdesc="Import, export, process, analyze and view triangular meshes"
arch=(any)
url="https://trimsh.org"
license=(MIT)
depends=(python-numpy)
makedepends=(python-build python-installer python-setuptools python-wheel)
# checkdepends=(python-pytest python-scipy python-lxml python-rtree python-networkx
# python-jsonschema python-pillow python-requests python-shapely python-pyinstrument
# python-collada python-svg.path python-mapbox-earcut) # python-sympy python-msgpack python-pyglet openscad
optdepends=('python-scipy: convex hulls'
  'python-lxml: handle XML better and faster than built- in XML'
  'python-networkx: graph operations'
  'python-shapely: vector path handling'
  'python-rtree: vector path handling'
  'python-httpx: network requests'
  'python-sympy: do analytical math'
  'python-xxhash: hash ndarrays faster than built-in MD5/CRC'
  'python-chardet: encoding'
  'python-colorlog: print logs with colors'
  'python-pillow: load images'
  'python-svg.path: handle SVG format path strings'
  'python-jsonschema: validate JSON schemas like GLTF'
  'python-collada: parse collada/dae/zae files'
  'python-pyglet: preview windows'
  'python-fcl: collision queries between meshes'
  'python-meshio: load mesh formats'
  'python-scikit-image: for voxel ops'
  'python-mapbox-earcut: triangulate polygons'
  'python-psutil: get memory usage'
  'gmsh: gmsh file support'
  'python-ruff: static code analyzer'
  'python-pytest: test runner'
  'python-pyinstrument: sampling based profiler') # python-xatlas python-glooey
source=(${_base}-${pkgver}.tar.gz::https://github.com/mikedh/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('3b58a0378231dd1111ac4ffe030b1dd18d24647e22fe815bc411a7854f83e12a9482cb0b48d5333be9f6f6ebf622c15e29c446531ce27ff12c1835a6f25cc51a')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

# check() {
#   cd ${_base}-${pkgver}
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -m pytest
# }

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -D -m644 LICENSE.md "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
