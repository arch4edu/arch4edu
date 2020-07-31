# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=aomp-amdgpu
pkgdesc='Clang/LLVM based compiler with added support for the OpenMP API on Radeon GPUs'
_pkgver=11.7-1
pkgver=11.7.1
pkgrel=1
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/aomp'
license=('Apache')
depends=(z3 numactl pciutils libelf libffi guile2.0 ncurses expat xz zlib mpfr source-highlight babeltrace)
makedepends=(git cmake
    python python-pip python-argparse python-cppheaderparser python-ply python-wheel
    mesa texinfo)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rel_$_pkgver.tar.gz"
        'disable_ocl_tests.patch'
        'adjust_rpath.patch'
        'remove_gcc_logic.patch'
        'opencl_includes.patch::https://patch-diff.githubusercontent.com/raw/ROCm-Developer-Tools/ROCclr/pull/16.patch')
sha256sums=('74089dc689408ace339998cfd2fb8c04dded3776e63a30cc78f4c43fe3d5016f'
            'bf3aab8fc2c828554ba76ab1876179130704f1c35906228fcf7e94239f5e4170'
            '94c670cd991c95a7b6312feb77d32a11c1ac1b839218bcd251042563b7af1a44'
            'd1040410c7cebc109d2905722e959d4e9d3e4f122fe0a4ae72e3f3d8e5b9a722'
            '3edeb8aeaf335297ec0f61a15b99c259d607d8f534173fbc3d17832ad03cd63f')
_dirname="$(basename "$url")-$(basename ${source[0]} .tar.gz)"

prepare() {
    mv "$_dirname" aomp
    cd aomp/bin

    AOMP_REPOS="$srcdir" \
    ./clone_aomp.sh

    cd "$srcdir/opencl-on-vdi"
    patch -Np1 -i "$srcdir/disable_ocl_tests.patch"

    cd "$srcdir/vdi"
    patch -Np1 -i "$srcdir/opencl_includes.patch"

    cd "$srcdir/aomp"
    patch -Np1 -i "$srcdir/adjust_rpath.patch"
    patch -p1  -i "$srcdir/remove_gcc_logic.patch"
}

package() {
    cd aomp/bin

    #FORTIFY_SOURCE breaks flang-runtime
    export CPPFLAGS="$(sed -e 's/-D_FORTIFY_SOURCE=2//' <<< "$CPPFLAGS")"
    AOMP="$pkgdir/opt/rocm/aomp" \
    AOMP_REPOS="$srcdir" \
    ./build_aomp.sh

    #Fix symlink created by the build script
    rm "$pkgdir/opt/rocm/aomp"
    ln -s "/opt/rocm/aomp_$_pkgver" "$pkgdir/opt/rocm/aomp"

    #Export AOMP variable for rocminfo
    install -Dm777 /dev/stdin "$pkgdir/etc/profile.d/aomp-amdgpu.sh" <<EOF
export AOMP=/opt/rocm/aomp
EOF
}
