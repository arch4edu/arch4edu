pkgname=libnvidia-container
pkgver=1.0.0_0.1.beta.1
pkgrel=1
pkgdesc='NVIDIA container runtime library'
arch=('x86_64')
url='https://github.com/NVIDIA/libnvidia-container'
license=('custom')
depends=(libcap libseccomp)
source_x86_64=("https://nvidia.github.io/libnvidia-container/centos7/x86_64/libnvidia-container1-1.0.0-0.1.beta.1.x86_64.rpm")
sha256sums_x86_64=('38bb1e0e3e8cd3a7224805d19a3825b90e1c2270027d20552f248abdba1e2364')

package() {
  cd "$srcdir"
  install -m755 -d "$pkgdir/usr/lib"
  cp -a usr/lib64/* "$pkgdir/usr/lib/"
  install -D -m644 usr/share/licenses/*/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
