# Maintainer: acxz <akashpatel2008@yahoo.com>
pkgname=rock-dkms-bin
pkgver=3.5
_pkgver=$pkgver-32
pkgrel=4
pkgdesc="Linux AMD GPU kernel driver from ROC in DKMS format."
arch=('any')
url="https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver"
license=('GPL')
depends=('dkms' 'rock-dkms-firmware')
provides=('rock-dkms')
conflicts=('rock-dkms')
backup=('etc/modprobe.d/blacklist-radeon.conf')
options=('!strip' '!emptydirs')
source=("http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms_${_pkgver}_all.deb"
        "rock_compatibility.patch"::"https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/ROCK-Kernel-Driver/pull/95.patch")

sha256sums=('96bb0730df239e9c7ea6b0086060dff04a31e620a08c51e7b1f9235858dbe2af'
            'a8dec1dc7d118844dfe2bbf4beab8b15b69cdae478957dfc5e033997f58d00cb')

package() {
  cd "$srcdir"

  tar xf data.tar.xz -C "$pkgdir"

  head -n 37 rock_compatibility.patch > Makefile.patch
  grep "amdgpu_bios.c b" rock_compatibility.patch -A 52 > amdgpu_bios.c.patch
  tail -n 104 rock_compatibility.patch > amdkcl_kallsyms.patch

  cd $pkgdir/usr/src/amdgpu-${_pkgver}/amd
  patch --forward -p4 dkms/Makefile --input=${srcdir}/Makefile.patch
  patch --forward -p4 amdgpu/amdgpu_bios.c --input=${srcdir}/amdgpu_bios.c.patch
  patch --forward -p5 --input=${srcdir}/amdkcl_kallsyms.patch

  install -Dm644 "$pkgdir/usr/share/doc/rock-dkms/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
