# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>

_base=KaHIP
pkgname=${_base,,}
pkgver=3.25
pkgrel=2
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=('x86_64')
url="https://github.com/KaHIP/KaHIP"
license=('MIT' 'BSD-3-Clause') # BSD-3-Clause: bundled argtable3
depends=('glibc'
         'gperftools'
         'libgcc'
         'libgomp'
         'libstdc++'
         'metis'
         'openmpi'
         'python')
makedepends=('cmake'
             'pybind11')
options=(!lto)
source=("$url/archive/v$pkgver.tar.gz"
        "fix-out-of-bounds.patch")
sha256sums=('3abad20158887b585b4d4792c35fa9023b7fd634b2bc4494334a3951b69f4842'
            '03250c9f51c4e6391d19549263a7a501d264c5c032a8ce35dab49ea599ec65d8')

prepare() {
  # Out-of-range accesses caught by Arch's -D_GLIBCXX_ASSERTIONS:
  # compute_fill() (node_ordering, fast_node_ordering) and
  # maxNodeHeap::changeKey()/deleteNode() on nodes no longer queued (node separators)
  patch -d ${_base}-${pkgver} -Np1 -i ../fix-out-of-bounds.patch
}

build() {
  local _site_packages=$(python -c "import sysconfig; print(sysconfig.get_path('platlib'))")

  cmake \
    -S $_base-$pkgver \
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
    -DUSE_TCMALLOC=ON \
    -DUSE_ILP=OFF \
    -D64BITMODE=OFF \
    -DDETERMINISTIC_PARHIP=OFF \
    -DOPTIMIZED_OUTPUT=OFF \
    -Wno-dev
  cmake --build build
}


package() {
  DESTDIR="$pkgdir" cmake --install build

  local _site_packages=$(python -c "import sysconfig; print(sysconfig.get_path('platlib'))")
  install -Dm 644 $_base-$pkgver/python/$pkgname/__init__.py -t "$pkgdir$_site_packages/$pkgname"
  echo "__version__ = \"$pkgver\"" > "$pkgdir$_site_packages/$pkgname/_version.py"
  python -m compileall -q -d "$_site_packages" "$pkgdir$_site_packages/$pkgname"
  python -O -m compileall -q -d "$_site_packages" "$pkgdir$_site_packages/$pkgname"

  rm -f "$pkgdir"/usr/lib/lib{kahip,parhip_interface}_static.a
  rm -f "$pkgdir"/usr/bin/interface_test

  install -Dm 644 $_base-$pkgver/LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm 644 $_base-$pkgver/extern/argtable3-3.2.2/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE.argtable3"
}
