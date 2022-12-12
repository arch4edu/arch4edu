# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Fabian Bornschein <fabiscafe-cat-mailbox-dog-org>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-core
_pkgver_major=5
_pkgver_minor=4
_pkgver_patch=0
_pkgver_str="${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)"
_pkgver_magic=72
_pkgver_ubunturel=22.04
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc='AMD ROCm core package'
arch=('x86_64')
url='https://docs.amd.com/'
license=()
depends=()
makedepends=('cmake')
source=(# https://repo.radeon.com/rocm/apt/5.4/pool/main/r/rocm-core/rocm-core_5.4.0.50400-72~22.04_amd64.deb
        "${pkgname}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver/.0/}/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}.${_pkgver_str}-${_pkgver_magic}~${_pkgver_ubunturel}_amd64.deb"
        "rocm_version.c"
        "CMakeLists.txt")
sha256sums=('dc8913f8520134c4dc0e33699550093bd9ce7b392104a09bf6ddcc76608a7357'
            '23ded36e5cf003be491e09e56b10982efb585b6bb93ae18884a8a160f0d9cae0'
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
  install -Dm644 opt/rocm-${pkgver}/include/rocm-core/rocm_version.h "$pkgdir/opt/rocm/include/rocm-core/rocm_version.h"
  install -Dm644 opt/rocm-${pkgver}/lib/rocmmod "$pkgdir/opt/rocm/lib/rocmmod"
  mkdir -p "$pkgdir/opt/rocm/lib/CMakeFiles/rocm-core.dir"
}
