# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-common
_tarver=2.9.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=1
pkgdesc="Infrastructure and foundation classes"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=('custom:GPL2 with runtime exception')
depends=(cmake git lapack python-setuptools
  python-portalocker python-numpy python-mpi4py python-jinja)
makedepends=(python-scikit-build python-ninja doxygen graphviz python-sphinx texlive-latexextra biber)
optdepends=('vc: C++ Vectorization library'
  'texlive-latexextra: Type setting system'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'inkscape: Conversion routines for generate PNG images'
  'bash-completion: for completion when using bash'
  'parmetis: Parallel Graph Partitioning and Fill-reducing Matrix Ordering'
  'scotch: Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering'
  'tbb: High level abstract threading library'
  'man-db: manual pages for dune'
  'python-matplotlib: for Matplotlib rendering'
  'mayavi: for 3D plotting')
provides=('dunecontrol' 'dune-ctest' 'dune-git-whitespace-hook' 'dunepackaging.py' 'duneproject' 'rmgenerated.py')
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('4d1f05ee7d5c2376f0fc782b4978596501eed0e7c6d6c68b3a37949a0141cf308b42a6df1b171804a9606907f6597039f28916731c1caa0c54a36775402e6e97'
  'SKIP')
validpgpkeys=('E5B47782DE09813BCC3518E159DA94F1FC8FD313') # Andreas Dedner <a.s.dedner@warwick.ac.uk>

prepare() {
  cd ${pkgname}-${pkgver}
  export _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  sed -i 's/^Version: '"${pkgver%%.0}"'-git/Version: '"${pkgver}"'/' dune.module
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
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -DALLOW_CXXFLAGS_OVERWRITE=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_LATEX=FALSE \
    -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=FALSE \
    -DENABLE_HEADERCHECK=ON \
    -DDUNE_ENABLE_PYTHONBINDINGS=ON \
    -DDUNE_PYTHON_INSTALL_LOCATION='none' \
    -DDUNE_PYTHON_WHEELHOUSE="dist" \
    -DCMAKE_DISABLE_FIND_PACKAGE_Vc=TRUE

  cmake --build _skbuild/linux-${CARCH}-${_pyversion}/cmake-build --target sphinx_html
}

package() {
  cd ${pkgname}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py --skip-cmake install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -d "${pkgdir}"/usr/share/doc/"${pkgname}"/buildsystem
  mv _skbuild/linux-${CARCH}-${_pyversion}/cmake-build/doc/buildsystem/html/* "${pkgdir}"/usr/share/doc/${pkgname}/buildsystem
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}
