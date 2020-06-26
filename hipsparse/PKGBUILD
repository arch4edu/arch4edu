# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=hipsparse
pkgver=3.5.0
pkgrel=2
pkgdesc='rocSPARSE marshalling library.'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#hipsparse'
license=('MIT')
depends=('hip-rocclr' 'rocsparse')
makedepends=('cmake' 'git' 'rocminfo')
_git='https://github.com/ROCmSoftwarePlatform/hipSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "fix_hcc_compress.patch::$_git/commit/e79985dccde22d826aceb3badfc643a3227979d2.patch"
        "fix_nvcc_compress.patch::$_git/commit/530047af4a0f437dafc02f76b3a17e3b1536c7ec.patch")
sha256sums=('fa16b2a307a5d9716066c2876febcbc1cef855bf0c96d235d2d8f2206a0fb69d'
            '6b7493f0caa1b8042ef43c1a4cee6584abeeb9319c53a79e8b2e558cd1076992'
            'db755df3ae712d33d4954b7d302d656b1bdc8f226c063ee701d3b4d835297686')

prepare() {
  cd ${srcdir}/hipSPARSE-rocm-$pkgver
  patch --forward --strip=1 --input="${srcdir}/fix_hcc_compress.patch"
  patch --forward --strip=1 --input="${srcdir}/fix_nvcc_compress.patch"
}

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -DCMAKE_CXX_STANDARD=20 \
        -DCMAKE_INSTALL_PREFIX=opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DAMDDeviceLibs_DIR=/opt/rocm/lib/cmake/AMDDeviceLibs \
        -Dhip_DIR=/opt/rocm/hip/lib/cmake/hip \
        -Drocsparse_DIR=/opt/rocm/rocsparse/lib/cmake/rocsparse \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_CLIENTS_TESTS=OFF \
        "$srcdir/hipSPARSE-rocm-$pkgver"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hipsparse.conf" << EOF
/opt/rocm/hipsparse/lib
EOF
  install -Dm644 "$srcdir/hipSPARSE-rocm-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
