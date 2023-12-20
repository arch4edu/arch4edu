# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Brad Pitcher <bradpitcher@gmail.com>
# Contributor: Jelle van der Waa <jelle@archlinux.org>

_base=trimesh
pkgname=python-${_base}
pkgver=4.0.7
pkgrel=1
pkgdesc="Import, export, process, analyze and view triangular meshes"
arch=(any)
url="https://trimsh.org"
license=(MIT)
depends=(python python-numpy)
makedepends=(python-build python-installer python-setuptools python-wheel)
# checkdepends=(python-pytest python-scipy python-lxml python-rtree python-networkx
#   python-jsonschema python-pillow python-requests python-shapely python-pyinstrument
#   python-collada python-svg.path python-mapbox-earcut) # python-sympy python-msgpack python-pyglet openscad
optdepends=('python-scipy: convex hulls'
  'python-lxml: handle XML better and faster than built- in XML'
  'python-networkx: graph operations'
  'python-shapely: vector path handling'
  'python-rtree: vector path handling'
  'python-requests: network requests'
  'python-sympy: do analytical math'
  'python-xxhash: hash ndarrays faster than built-in MD5/CRC'
  'python-msgpack: serialize into msgpack'
  'python-chardet: encoding'
  'python-colorlog: print logs with colors'
  'python-pillow: load images'
  'python-svg.path: handle SVG format path strings'
  'python-jsonschema: validate JSON schemas like GLTF'
  'python-collada: parse collada/dae/zae files'
  'python-pyglet: preview windows'
  'python-meshio: load mesh formats'
  'python-scikit-image: for voxel ops'
  'python-mapbox-earcut: triangulate polygons'
  'python-psutil: get memory usage'
  'python-ruff: static code analyzer'
  'autopep8: code formatter'
  'python-pytest: test runner'
  'python-pyinstrument: sampling based profiler') # python-xatlas python-fcl python-glooey
source=(${_base}-${pkgver}.tar.gz::https://github.com/mikedh/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('fcbc6cd917d1b6d0d23064efe6c484c8f920e966c9108cc9664cea502d43abc4cd3fb77cdd54491bb3098efae964910a9fb211aef763f576cf0ab1ae1267f657')

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
