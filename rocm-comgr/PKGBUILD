# Maintainer: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-comgr
pkgdesc='Radeon Open Compute - compiler support'
pkgver=3.3.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom')
makedepends=(cmake git llvm-roc)
source=(
    "rocm-comgr::git+https://github.com/RadeonOpenCompute/ROCm-CompilerSupport#tag=rocm-$pkgver"
#    "rocm-comgr-2.6.0-find-clang.patch"
#	"rocm-comgr-2.6.0-find-lld-includes.patch"
	# "rocm-comgr-2.8.0-dependencies.patch"
)
sha256sums=('SKIP')
#            'f04ff936e87a888264e9c0920c9356a85b18e9ec9d729fcf53f83755c171828c'
#            '4571b16961f15249e8cc8b9a9ae7f0863600345aa5e95959192149eacdb01d2e')

prepare() {
    cd "$srcdir/rocm-comgr/lib/comgr"

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
    if check_buildoption "ccache" "y"; then
        CMAKE_FLAGS="-DROCM_CCACHE_BUILD=ON"
    fi

    cmake $CMAKE_FLAGS \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DClang_DIR=/opt/rocm/lib/cmake/clang \
        "$srcdir/rocm-comgr/lib/comgr"
    make
}

package() {
    DESTDIR="$pkgdir/" make -C "$srcdir" install
}
