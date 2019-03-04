pkgname=nvidia-container-runtime
pkgver=2.0.0+1.docker18.03.0
pkgrel=1
pkgdesc='NVIDIA container runtime'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('custom')
depends=(libseccomp libnvidia-container-tools)
source_x86_64=("https://nvidia.github.io/nvidia-container-runtime/centos7/x86_64/${pkgname}-2.0.0-1.docker18.03.0.x86_64.rpm")
sha256sums_x86_64=('cd3ade9f4122b293002091900dc152ea0d928de343677a06ca8252158f25a1c8')

package() {
  cd "$srcdir"
  install -m755 -d "$pkgdir/usr/bin"
  install -D -m755 usr/bin/* "$pkgdir/usr/bin/"
  install -D -m644 usr/share/licenses/$pkgname-*/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
