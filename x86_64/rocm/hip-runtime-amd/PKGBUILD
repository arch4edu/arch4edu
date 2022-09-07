# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-amd
pkgver=5.2.3
pkgrel=1
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('mesa' 'comgr' 'rocminfo' 'rocm-llvm' 'libelf')
makedepends=('cmake' 'python' 'git')
provides=('hip')
conflicts=('hip')
_hip='https://github.com/ROCm-Developer-Tools/HIP'
_opencl='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
_rocclr='https://github.com/ROCm-Developer-Tools/ROCclr'
_hipamd='https://github.com/ROCm-Developer-Tools/hipamd'
source=("$pkgname-$pkgver.tar.gz::$_hip/archive/rocm-$pkgver.tar.gz"
        "$pkgname-opencl-$pkgver.tar.gz::$_opencl/archive/rocm-$pkgver.tar.gz"
        "$pkgname-rocclr-$pkgver.tar.gz::$_rocclr/archive/rocm-$pkgver.tar.gz"
        "$pkgname-hipamd-$pkgver.tar.gz::$_hipamd/archive/rocm-$pkgver.tar.gz"
        "git-hash.patch::https://github.com/ROCm-Developer-Tools/hipamd/commit/56b32604729cca08bdcf00c7a69da8a75cc95b8a.patch"
        "noinline.patch::https://github.com/ROCm-Developer-Tools/hipamd/commit/28009bc68faf2b4dd8fda91c99b0725e1b063a18.patch")
sha256sums=('5b83d1513ea4003bfad5fe8fa741434104e3e49a87e1d7fad49e5a8c1d06e57b'
            '932ea3cd268410010c0830d977a30ef9c14b8c37617d3572a062b5d4595e2b94'
            '0493c414d4db1af8e1eb30a651d9512044644244488ebb13478c2138a7612998'
            '5031d07554ce07620e24e44d482cbc269fa972e3e35377e935d2694061ff7c04'
            '3b0ec136c9bad206697087df0908922df705ec76085f57e36d0d15f52a5fd981'
            'f45f2087ba3fab3ee3b9e65baefad604cd774611f3d433273afc1166d146e8ed')
_dirhip="$(basename "$_hip")-$(basename "${source[0]}" ".tar.gz")"
_diropencl="$(basename "$_opencl")-$(basename "${source[1]}" ".tar.gz")"
_dirrocclr="$(basename "$_rocclr")-$(basename "${source[2]}" ".tar.gz")"
_dirhipamd="$(basename "$_hipamd")-$(basename "${source[3]}" ".tar.gz")"

prepare() {
    cd "$_dirhipamd"
    patch -Np1 -i "$srcdir/git-hash.patch"
    patch -Np1 -i "$srcdir/noinline.patch"
}

build() {
  local cmake_args=(-DHIP_COMMON_DIR="$srcdir/$_dirhip"
                    -DHIP_COMMON_DIR="$srcdir/$_dirhip"
                    -DAMD_OPENCL_PATH="$srcdir/$_diropencl"
                    -DROCCLR_PATH="$srcdir/$_dirrocclr"
                    -DHIP_PLATFORM=amd
                    -DCMAKE_INSTALL_PREFIX=/opt/rocm)
  if [[ -n "$AMDGPU_TARGETS" ]]; then
      cmake_args+=(-DAMDGPU_TARGETS="${AMDGPU_TARGETS}")
  fi

  # build fails if cmake and make are called from outside the build directory
  mkdir build && cd build
  cmake -Wno-dev \
  -S "$srcdir/$_dirhipamd" \
  "${cmake_args[@]}"

  make
}

package() {
  DESTDIR="$pkgdir" make -C build install

  # add links (hipconfig is for rocblas with tensile)
  install -d "$pkgdir/usr/bin"
  local _fn
  for _fn in hipcc hipconfig hipcc.pl hipconfig.pl; do
    ln -s "/opt/rocm/hip/bin/$_fn" "$pkgdir/usr/bin/$_fn"
  done

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hip.conf" <<EOF
/opt/rocm/hip/lib
EOF
  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
