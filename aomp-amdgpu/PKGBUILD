# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=aomp-amdgpu
pkgdesc='Clang/LLVM based compiler with added support for the OpenMP API on Radeon GPUs'
_pkgver=11.11-0
pkgver=11.11.0
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
        'remove_gcc_logic.patch')
sha256sums=('7d9cea6b8944f110dfdb307fdd7e11809168a5a8f6502ffbd8dbf1e711e20707'
            '10450211c4ee15a39d3ce9d85403b11174430b17bafd229019cf5ed5840a8b7a'
            '5cf8144d9f3e42feecdb12aaef013921fed5e4e61b4bf8e3c1960dced26d13ae')
_dirname="$(basename "$url")-$(basename ${source[0]} .tar.gz)"

prepare() {
    mv "$_dirname" aomp
    cd aomp/bin

    AOMP_REPOS="$srcdir" \
    ./clone_aomp.sh

    cd "$srcdir/opencl-on-vdi"
    patch -Np1 -i "$srcdir/disable_ocl_tests.patch"

    cd "$srcdir/aomp"
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
