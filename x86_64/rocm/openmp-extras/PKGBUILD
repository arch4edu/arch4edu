# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=openmp-extras
pkgdesc='Radeon Open Compute - openmp-extras with flang (OpenMP AMD GPU Offloading)'
pkgver=5.1.3
pkgrel=1
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/aomp'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(hsa-rocr rocm-llvm)
makedepends=(cmake python python-pip python-wheel ninja gawk)
llvm_url='https://github.com/RadeonOpenCompute/llvm-project'
dlibs_url='https://github.com/RadeonOpenCompute/ROCm-Device-Libs'
flang_url='https://github.com/ROCm-Developer-Tools/flang'
extras_url='https://github.com/ROCm-Developer-Tools/aomp-extras'
source=("llvm-amdgpu-${pkgver}.tar.gz::$llvm_url/archive/rocm-$pkgver.tar.gz"
        "aomp-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "aomp-extras-$pkgver.tar.gz::$extras_url/archive/rocm-$pkgver.tar.gz"
        "aomp-device-libs-$pkgver.tar.gz::$dlibs_url/archive/rocm-$pkgver.tar.gz"
        "flang-$pkgver.tar.gz::$flang_url/archive/rocm-$pkgver.tar.gz"
        "llvm-project-hostrpc-fprintf-decl.patch"
        "aomp-gcc8-only-for-cuda.patch"
        "aomp-openmp-buildpath.patch"
        "aomp-openmp-llvm.patch"
        "aomp-flang-alarm-signature.patch"
        "aomp-flang-decouple-out-dir-and-rocm-install.patch"
        "aomp-flang-libomp-path.patch"
        "aomp-extras-compiler-in-rocm-dir.patch"
        )
sha256sums=(
            'd236a2064363c0278f7ba1bb2ff1545ee4c52278c50640e8bb2b9cfef8a2f128'
            '8bab3d621343f419b29043ac0cb56e062f114991dc3ec1e33e786f771deecc8f'
            '2e3151a47d77166d071213af2a1691487691aae0abd5c1718d818a6d7d09cb2d'
            'c41958560ec29c8bf91332b9f668793463904a2081c330c0d828bf2f91d4f04e'
            'd7847b5c6e1344dc0b4723dbe76a859257b4c242644dedb34e425f07738530d4'
            'c846bac17580e939492b843bee092c2e1b2b414a683bdb6be2973ae044642424'
            '705a7103c3aeff514e5645c130786172961c54673dfdd772caece3b5e7536088'
            'f7ed1704ffb095bbe8512b1c567a111936685d35f64123c786194e4239277251'
            '6efb9538e016e1e6e2fb6ce52408bb6317c213ebdd46a60925447d0b43f42ee6'
            '7c796d44952da8f089dc3ee013970dba7be43c60eb90131f86ce7d15c67b4b9b'
            'e82a4f065cc259095bf96778b913b97fe39d7c207e4e25ccf59d8fa264014262'
            'ff3c3e56bfc11c0c9a6ab5c5392168da06aed3b4a21cdfcf7a149d12a69e2906'
            'f8f57cdcc4ddf535323f4f84a4a4a4fa830fbad72b19c7ea45d74fa5579ee72f'
            )
options=(staticlibs !lto)

prepare() {

    ln -f -s "$srcdir/llvm-project-rocm-$pkgver" "$srcdir/llvm-project"
    ln -f -s "$srcdir/flang-rocm-$pkgver" "$srcdir/flang"
    ln -f -s "$srcdir/aomp-extras-rocm-$pkgver" "$srcdir/aomp-extras"

    cd "$srcdir/llvm-project-rocm-$pkgver"
    patch -Np1 < "$srcdir/llvm-project-hostrpc-fprintf-decl.patch"

    cd "$srcdir/aomp-rocm-$pkgver"
    patch -Np1 < "$srcdir/aomp-gcc8-only-for-cuda.patch"
    patch -Np1 < "$srcdir/aomp-openmp-buildpath.patch"
    patch -Np1 < "$srcdir/aomp-openmp-llvm.patch"
    patch -Np1 < "$srcdir/aomp-flang-decouple-out-dir-and-rocm-install.patch"
    patch -Np1 < "$srcdir/aomp-flang-libomp-path.patch"

    cd "$srcdir/flang"
    patch -Np1 < "$srcdir/aomp-flang-alarm-signature.patch"

    cd "$srcdir/aomp-extras"
    patch -Np1 < "$srcdir/aomp-extras-compiler-in-rocm-dir.patch"

}

build() {

    export OMPEXTRA_DIR="$srcdir/out/openmp-extras"
    export OUT_DIR="$OMPEXTRA_DIR"
    export AOMP="$OUT_DIR/llvm"
    export AOMP_STANDALONE_BUILD=0
    export AOMP_REPOS="$srcdir"
    export ROCM_DIR=/opt/rocm
    export DEVICELIBS_ROOT="$srcdir/ROCm-Device-Libs-rocm-$pkgver"
    export LLVM_PROJECT_ROOT="$srcdir/llvm-project"

    cd "$srcdir/aomp-rocm-$pkgver/bin"
    ./build_extras.sh
    ./build_extras.sh install

    ./build_openmp.sh
    ./build_openmp.sh install

    ./build_pgmath.sh
    ./build_pgmath.sh install

    ./build_flang.sh
    ./build_flang.sh install

    ./build_flang_runtime.sh
    ./build_flang_runtime.sh install
}


package() {

    mkdir -p "$pkgdir/opt/rocm/"
    cp -r "$srcdir"/out/openmp-extras/* "$pkgdir/opt/rocm/"
}
