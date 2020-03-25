# Maintainer: Ranieri Althoff <ranisalt+aur at gmail dot com>

_opencl_icd_loader_commit='978b4b3a29a3aebc86ce9315d5c5963e88722d03'

pkgbase=rocm-opencl-runtime
pkgname=(rocm-device-libs rocm-opencl-runtime)
pkgver=3.1.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute'
makedepends=(mesa cmake git llvm-roc rocm-comgr)
provides=("$pkgname" 'opencl-driver')
source=(
    "rocm-device-libs::git+https://github.com/RadeonOpenCompute/ROCm-Device-Libs#tag=roc-ocl-$pkgver"
    "rocm-opencl-runtime::git+https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime#tag=roc-$pkgver"
    "rocm-cmake::git+https://github.com/RadeonOpenCompute/rocm-cmake#tag=roc-3.0.0"
    "opencl-icd-loader::git+https://github.com/KhronosGroup/OpenCL-ICD-Loader#commit=$_opencl_icd_loader_commit"
    # "rocm-opencl-runtime-2.8.0-change-AMDCompilerh.patch"
    "rocm-opencl-runtime-2.8.0-change-opencl.patch"
    "rocm-opencl-runtime-2.8.0-amdocl64icd.patch"
    "rocm-opencl-runtime-3.0.0-change-install-location.patch"
)

sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '3af5c9c3b8b88b78a2fd574f339e88a5cd62c365d94e9289c2a2cb4afef3d435'
            '2cfd11bda9a485d6de2231c56742ad553329cab9b6dcc009dbddbcde1436f485'
            '941a29f8704a2839c32bcf3cf374dde30bc8a839c1136d4faa65c60a7500cf98')

prepare() {
    cd "$srcdir/rocm-opencl-runtime"

    # [ -d tools/clinfo ] && rm -rf tools/clinfo

    mkdir -p api/opencl/khronos
    mv "$srcdir/opencl-icd-loader" api/opencl/khronos/icd

    local src
    for src in "${source[@]}"; do
        src="${src%%::*}"
        src="${src##*/}"
        [[ $src = *.patch ]] || continue
        msg2 "Applying patch $src..."
        patch -Np1 -i "$srcdir/$src"
    done
}

build() {
    CMAKE_FLAGS=(
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_INSTALL_PREFIX='/opt/rocm'
        -DLLVM_DIR=/opt/rocm/lib/cmake/llvm
    )
    if check_buildoption "ccache" "y"; then
        CMAKE_FLAGS+=(-DROCM_CCACHE_BUILD=ON)
    fi

    msg2 'Building prepare builtins...'
    cd "$srcdir/rocm-device-libs/utils"
    cmake ${CMAKE_FLAGS[@]} ..
    make

    msg2 'Building device libs...'
    cd "$srcdir/rocm-device-libs"
    mkdir -p build && cd build
    cmake ${CMAKE_FLAGS[@]} \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DPREPARE_BUILTINS="$srcdir/rocm-device-libs/utils/utils/prepare-builtins/prepare-builtins" \
        ..
    make

    msg2 'Building OpenCL runtime...'
    cd "$srcdir/rocm-opencl-runtime"
    mkdir -p build && cd build
    cmake ${CMAKE_FLAGS[@]} \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_INSTALL_SYSCONFDIR=/etc \
        -DCMAKE_MODULE_PATH="$srcdir/rocm-cmake/share/rocm/cmake" \
        -DCMAKE_PREFIX_PATH=/opt/rocm/lib/cmake \
        -DUSE_COMGR_LIBRARY=yes \
        ..
    make
}

package_rocm-device-libs() {
    pkgdesc='Radeon Open Compute - device libs'
    license=('unknown')

    DESTDIR="$pkgdir/" make -C "$srcdir/rocm-device-libs/build" install
}

package_rocm-opencl-runtime() {
    pkgdesc='Radeon Open Compute - OpenCL runtime'
    depends=("roct-thunk-interface>=${pkgver}" "rocr-runtime>=${pkgver}" 'opencl-icd-loader')
    license=('MIT')

    DESTDIR="$pkgdir/" make -C "$srcdir/rocm-opencl-runtime/build" install

    mkdir -p "$pkgdir/etc/ld.so.conf.d"
    echo '/opt/rocm/lib' > "$pkgdir/etc/ld.so.conf.d/rocm-opencl.conf"

    install -Dm644 "$srcdir/rocm-opencl-runtime/License" "$pkgdir/usr/share/licenses/rocm-opencl-runtime/LICENSE"
}
