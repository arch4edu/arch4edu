# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>

_name=KaHIP
pkgname=${_name,,}
pkgver=3.30
pkgrel=2
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=('x86_64')
url="https://github.com/KaHIP/KaHIP"
license=('MIT' 'BSD-3-Clause')
depends=('python'
         'glibc'
         'gperftools'
         'libgcc'
         'libgomp'
         'libstdc++'
         'metis'
         'openmpi')
makedepends=('cmake'
             'gcc-fortran'
             'pybind11')
options=(!lto)
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz"
        "fix-out-of-bounds.patch"
        "fix-prefetch.patch")
sha256sums=('9fe214ba2978951fdc75b3f4f2dc944e3279bb1ddeac32ae097121310b1c5c51'
            '03250c9f51c4e6391d19549263a7a501d264c5c032a8ce35dab49ea599ec65d8'
            '78492503be743a72f1a4aae7d3f913ae8f6247e1641e16b8b3fa5fd6b872f2cd')

prepare() {
  cd "$_name-$pkgver"
  # Out-of-range accesses caught by Arch's -D_GLIBCXX_ASSERTIONS:
  # compute_fill() (node_ordering, fast_node_ordering) and
  # maxNodeHeap::changeKey()/deleteNode() on nodes no longer queued (node separators)
  patch -Np1 -i ../fix-out-of-bounds.patch
  # ParHIP fails to build with libstdc++ 16: the fallback ordered_edge_map lacks prefetch(), fixed upstream in KaHIP/KaHIP@bab6e0c
  patch -Np1 -i ../fix-prefetch.patch
}

build() {
  cd "$_name-$pkgver"
  local _site_packages=$(python -c "import sysconfig; print(sysconfig.get_path('platlib'))")
  cmake \
    -S . \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_FLAGS_NONE="-DNDEBUG" \
    -DCMAKE_C_FLAGS_NONE="-DNDEBUG" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS -Wl,-Bsymbolic" \
    -DCMAKE_MODULE_LINKER_FLAGS="$LDFLAGS -Wl,-Bsymbolic" \
    -DCMAKE_INSTALL_PYTHONDIR="$_site_packages" \
    -DNONATIVEOPTIMIZATIONS=ON \
    -DPARHIP=ON \
    -DNOMPI=OFF \
    -DBUILDPYTHONMODULE=ON \
    -DBUILDFORTRAN=ON \
    -DUSE_TCMALLOC=ON \
    -DUSE_ILP=OFF \
    -D64BITMODE=OFF \
    -DDETERMINISTIC_PARHIP=OFF \
    -DOPTIMIZED_OUTPUT=OFF \
    -Wno-dev
  cmake --build build
}

check() {
  cd "$_name-$pkgver"
  export OMPI_MCA_rmaps_base_oversubscribe=1
  ctest --test-dir build --output-on-failure
}

package() {
  cd "$_name-$pkgver"
  DESTDIR="$pkgdir" cmake --install build
  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  install -Dm 644 extern/argtable3-3.2.2/LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.argtable3
  local _site_packages=$(python -c "import sysconfig; print(sysconfig.get_path('platlib'))")
  install -Dm 644 python/$pkgname/__init__.py -t "$pkgdir$_site_packages/$pkgname"
  echo "__version__ = \"$pkgver\"" > "$pkgdir$_site_packages/$pkgname/_version.py"
  python -m compileall -q -d "$_site_packages" "$pkgdir$_site_packages/$pkgname"
  python -O -m compileall -q -d "$_site_packages" "$pkgdir$_site_packages/$pkgname"
  rm -f "$pkgdir"/usr/lib/lib{kahip,parhip_interface}_static.a
  rm -f "$pkgdir"/usr/bin/interface_test
}
