# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-common
_tarver=2.9.1
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=1
pkgdesc="Infrastructure and foundation classes"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=('custom:GPL2 with runtime exception')
depends=(cmake git lapack python-setuptools python-portalocker python-numpy python-mpi4py python-jinja)
makedepends=(python-scikit-build doxygen graphviz python-sphinx texlive-latexextra biber)
optdepends=('vc: C++ Vectorization library'
  'texlive-latexextra: Type setting system'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'inkscape: Conversion routines for generate PNG images'
  'bash-completion: for completion when using bash'
  'parmetis: Parallel Graph Partitioning and Fill-reducing Matrix Ordering'
  'scotch: Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering'
  'onetbb: High level abstract threading library'
  'man-db: manual pages for dune'
  'python-matplotlib: for Matplotlib rendering'
  'python-mayavi: for 3D plotting')
provides=('dunecontrol' 'dune-ctest' 'dune-git-whitespace-hook' 'dunepackaging.py' 'duneproject' 'rmgenerated.py')
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('554d9f5dde66930d8966b99832728d17bb7670aa055c071e00260c6f90e739818672e3b9fb3f292bcb96f128f9e82679c921d8603bb993eb768f89a7b3951ac1'
  'SKIP')
validpgpkeys=('2AA99AA4E2D6214E6EA01C9A4AF42916F6E5B1CF') # Christoph Grüninger <pgp@grueninger.de>

prepare() {
  cd ${pkgname}-${pkgver}
  local _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  # https://salsa.debian.org/science-team/dune-common/-/blob/master/debian/patches/skip-dirs-starting-with-dot.patch
  sed -i 's/^        $(find -H "$dir" -name $CONTROL | $GREP -v '\''dune-\[-_a-zA-Z\]\/dune-\[-a-zA-Z_\]\*-\[0-9\]\\{1,\\}.\[0-9\]\\{1,\\}\/'\'')/        $(find -H "$dir" -name '\''.?\*'\'' -prune -o -name $CONTROL -print | $GREP -v '\''dune-\[-_a-zA-Z\]\/dune-\[-a-zA-Z_\]\*-\[0-9\]\\{1,\\}.\[0-9\]\\{1,\\}\/'\'')/' lib/dunemodules.lib
  python -m venv --system-site-packages _skbuild/linux-${CARCH}-${_pyversion}/cmake-build/dune-env
}

build() {
  cd ${pkgname}-${pkgver}
  XDG_CACHE_HOME="${PWD}" \
    python setup.py build \
    --build-type=None \
    -G 'Unix Makefiles' \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_FLAGS='-Wall -fdiagnostics-color=always' \
    -DCMAKE_CXX_FLAGS='-O2 -Wall -fdiagnostics-color=always -mavx' \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -DALLOW_CXXFLAGS_OVERWRITE=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_LATEX=FALSE \
    -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=FALSE \
    -DENABLE_HEADERCHECK=ON \
    -DDUNE_ENABLE_PYTHONBINDINGS=ON \
    -DDUNE_PYTHON_INSTALL_LOCATION='none' \
    -DDUNE_PYTHON_WHEELHOUSE="dist" \
    -DCMAKE_DISABLE_FIND_PACKAGE_Vc=TRUE

  local _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  cmake --build _skbuild/linux-${CARCH}-${_pyversion}/cmake-build --target sphinx_html
}

package() {
  cd ${pkgname}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py --skip-cmake install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -d "${pkgdir}"/usr/share/doc/"${pkgname}"/buildsystem
  local _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  mv _skbuild/linux-${CARCH}-${_pyversion}/cmake-build/doc/buildsystem/html/* "${pkgdir}"/usr/share/doc/${pkgname}/buildsystem
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}
