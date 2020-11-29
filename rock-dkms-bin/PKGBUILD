# Maintainer: acxz <akashpatel2008@yahoo.com>
pkgname=rock-dkms-bin
pkgver=3.9.1
_pkgver=3.9-19
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
sha256sums=('de1c56272a0de7fe0c3b8f802677d413be4b2b2930f74682c08f32ae0f3d9988'
            'SKIP')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"

  cd $pkgdir/usr/src/amdgpu-${_pkgver}
  patch --forward -p4 -t --input=${srcdir}/rock_compatibility.patch > patching.log \
     || echo "patch is meant to fail as not all files from the kernel is in the binary"

  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
