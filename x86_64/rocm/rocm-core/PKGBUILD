# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-core
_pkgver_major=5
_pkgver_minor=1
_pkgver_patch=3
_pkgver_str="${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)"
_pkgver_magic=66
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc='AMD ROCm core package'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/'
license=()
depends=()
makedepends=('cmake')
source=("${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.$_pkgver_str-${_pkgver_magic}_amd64.deb"
        "rocm_version.c"
        "CMakeLists.txt")
sha256sums=('99a4631736fc9d0a88db6e76886b68e066a33a4e673ab350c0fba07010ba52c8'
            '976781c610ac766c91a1da3f3f1474595216f69a0fdcb8c966f1f94095ce947a'
            'ed98f0e1712e99b34d9da5ae7ade1e33847ef000760012bd5ed57170d9577560')

prepare() {
  tar -xf data.tar.gz
}

build() {
  cmake -B build \
    -DROCM_VERSION=$_pkgver_str \
    -DCMAKE_PREFIX_PATH="$srcdir/opt/rocm-${pkgver}" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm

  make -C build

  sed -i "s|/opt/rocm-${pkgver}|/opt/rocm|g" opt/rocm-${pkgver}/lib/rocmmod
}

package() {
  make DESTDIR="$pkgdir" -C build install
  install -Dm644 opt/rocm-${pkgver}/.info/version "$pkgdir/opt/rocm/.info/version"
  install -Dm644 opt/rocm-${pkgver}/include/rocm_version.h "$pkgdir/opt/rocm/include/rocm_version.h"
  install -Dm644 opt/rocm-${pkgver}/lib/rocmmod "$pkgdir/opt/rocm/lib/rocmmod"
  mkdir -p "$pkgdir/opt/rocm/lib/CMakeFiles/rocm-core.dir"
}
