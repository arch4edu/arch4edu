# Maintainer: acxz <akashpatel2008@yahoo.com>
pkgname=rock-dkms-bin
pkgver=3.9
_pkgver=3.9-17
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
sha256sums=('1ab7c5f38c91f20a33e63154a803c6360ad05f6e01c95ef34c659b0ba769ad3b'
            'SKIP')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"

  cd $pkgdir/usr/src/amdgpu-${_pkgver}
  patch --forward -p4 -t --input=${srcdir}/rock_compatibility.patch > patching.log \
     || echo "patch is meant to fail as not all files from the kernel is in the binary"

  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
