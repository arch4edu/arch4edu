# Maintainer: acxz <akashpatel2008@yahoo.com>
pkgname=rock-dkms-bin
pkgver=3.8
_pkgver=3.8-30
pkgrel=1
pkgdesc="Linux AMD GPU kernel driver from ROC in DKMS format."
arch=('any')
url="https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver"
license=('GPL')
depends=('dkms' 'rock-dkms-firmware')
provides=('rock-dkms')
conflicts=('rock-dkms')
backup=('etc/modprobe.d/blacklist-radeon.conf')
options=('!strip' '!emptydirs')
source=("${pkgname}-${pkgver}.tar.gz"::"http://repo.radeon.com/rocm/apt/${pkgver}/pool/main/r/rock-dkms/rock-dkms_${_pkgver}_all.deb"
        "rock_compatibility.patch"::"https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/ROCK-Kernel-Driver/pull/95.patch")
sha256sums=('a468b61b1529c458a7ab0c58515377c99af1c5b2c42c8ab3fef4e74386a2b2f7'
            'SKIP')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"

  cd $pkgdir/usr/src/amdgpu-${_pkgver}
  patch --forward -p4 -t --input=${srcdir}/rock_compatibility.patch > patching.log \
     || echo "patch is meant to fail as not all files from the kernel is in the binary"

  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
