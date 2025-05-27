# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Michael Schubert <mschu.dev at gmail>
pkgname=symengine-0.13
_pkgname=symengine
pkgver=0.13.0
pkgrel=2
pkgdesc='Fast symbolic manipulation library, written in C++'
url='http://sympy.org/'
arch=(x86_64)
license=(MIT)
depends=(
    flint
    gcc-libs
    glibc
    gmp
    gmp-ecm
    gperftools
    libmpc
    llvm-libs
    mpfr
    primesieve
)
makedepends=(
    boost
    cereal
    cmake
    git
    llvm
)
provides=(symengine)
conflicts=(symengine)
source=(
    git+https://github.com/symengine/symengine#tag=v$pkgver
    llvm-shared.patch
    cmake.patch
)
b2sums=('b31f3338a9e590017d48e7da00011941f05ec52e8d2bd1cc6a236ace2931d3a10fff7c18e43bbf3503f38a7fca15073879f9ad8f41d34fe0ee78659c8809646f'
        '085519c1fc429e0f88608105fe910aa84b2df724fb9dd4cd6488de5da0d797e740c02ffa518ac10740b339dc4878772aea1a73c7bbe5726261d62b2f7d5ef37d'
        'c4a03e3d080bdb2859fabb9ebf7288bc64a1b90bf9ac5866cbeeb669f0683acc502d9a48d159bfcf6ccb882e35aac9c181ae9b10b71670b6a5bf84b1f615bb32')

prepare() {
    cd $_pkgname
    # Use shared LLVM (Gentoo)
    patch -p1 < ../llvm-shared.patch
    # So that build also works using cmake 4.0 from [kde-unstable]
    patch -p1 < ../cmake.patch
}

build() {
    cmake -B build -S $_pkgname \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_SHARED_LIBS=ON \
        -DWITH_TCMALLOC=ON \
        -DWITH_PTHREAD=ON \
        -DWITH_SYMENGINE_THREAD_SAFE=ON \
        -DWITH_ARB=ON \
        -DWITH_ECM=ON \
        -DWITH_LLVM=ON \
        -DWITH_MPFR=ON \
        -DWITH_MPC=ON \
        -DWITH_PRIMESIEVE=ON \
        -DWITH_BOOST=ON \
        -DWITH_COTIRE=OFF \
        -DWITH_SYSTEM_CEREAL=ON
    cmake --build build
}

check() {
    cmake --build build --target test
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 $_pkgname/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
