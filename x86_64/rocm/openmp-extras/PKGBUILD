# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=openmp-extras
pkgdesc='Radeon Open Compute - openmp-extras with flang (OpenMP AMD GPU Offloading)'
pkgver=5.2.3
pkgrel=1
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/aomp'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(hsa-rocr rocm-llvm)
makedepends=(cmake python-setuptools python-pip python-wheel)
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
        "aomp-openmp-buildpath.patch"
        "aomp-5.2.0-openmp-rocm_dir.patch"
        "aomp-flang-decouple-out-dir-and-rocm-install.patch"
        "aomp-flang-libomp-path.patch"
        "aomp-extras-5.2.0-rocm-dir-llvm.patch"
        "aomp-5.2.0-extras-version-string.patch"
        )
sha256sums=(
            '1b852711aec3137b568fb65f93606d37fdcd62e06f5da3766f2ffcd4e0c646df'
            '4ba1792095427588c484feed01f2f48e66aaad26bc000cbc74a15032551699e7'
            'f42ca7d85b0b64e6890502f1cf8309ef97f707829876742da2ea5c2cdf3ad8ac'
            '16b7fc7db4759bd6fb54852e9855fa16ead76c97871d7e1e9392e846381d611a'
            '496f00918721c72eae0bd926a5a8f1f35bd443f6b22bc08e2a42c67e44a4dbaf'

            'c846bac17580e939492b843bee092c2e1b2b414a683bdb6be2973ae044642424'
            'f7ed1704ffb095bbe8512b1c567a111936685d35f64123c786194e4239277251'
            '0d91c5408192dcceacde986c3419592efc67ad40d359d127604ee9bfbdba477a'
            'e82a4f065cc259095bf96778b913b97fe39d7c207e4e25ccf59d8fa264014262'
            'ff3c3e56bfc11c0c9a6ab5c5392168da06aed3b4a21cdfcf7a149d12a69e2906'
            'bae31efe2dd3f6813e9198c210ba3390028ed89e0d47e86366bef741c70c4db7'
            '7c5372078c74facbd7cae451c3a717bf281344dcd5c4103e1c837d980e79ccc9'
            )
options=(staticlibs !lto)

prepare() {

    ln -f -s "$srcdir/llvm-project-rocm-$pkgver" "$srcdir/llvm-project"
    ln -f -s "$srcdir/flang-rocm-$pkgver" "$srcdir/flang"
    ln -f -s "$srcdir/aomp-extras-rocm-$pkgver" "$srcdir/aomp-extras"

    cd "$srcdir/llvm-project-rocm-$pkgver"
    patch -Np1 < "$srcdir/llvm-project-hostrpc-fprintf-decl.patch"

    cd "$srcdir/aomp-rocm-$pkgver"
    patch -Np1 < "$srcdir/aomp-openmp-buildpath.patch"
    patch -Np1 < "$srcdir/aomp-5.2.0-openmp-rocm_dir.patch"
    patch -Np1 < "$srcdir/aomp-flang-decouple-out-dir-and-rocm-install.patch"
    patch -Np1 < "$srcdir/aomp-flang-libomp-path.patch"
    patch -Np1 < "$srcdir/aomp-5.2.0-extras-version-string.patch"

    cd "$srcdir/aomp-extras"
    patch -Np1 < "$srcdir/aomp-extras-5.2.0-rocm-dir-llvm.patch"

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
