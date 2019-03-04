pkgname=nvidia-container-runtime-hook
pkgver=1.3.0+1
pkgrel=1
pkgdesc='NVIDIA container runtime hook'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('custom')
depends=(nvidia-container-runtime)
source_x86_64=("https://nvidia.github.io/nvidia-container-runtime/centos7/x86_64/${pkgname}-1.3.0-1.x86_64.rpm")
sha256sums_x86_64=('9c18b62a9cf1310650d015b5610e09c359dc9e21bc3fcf8ffaea9098f03ddaa1')

package() {
  cd "$srcdir"
  install -m755 -d "$pkgdir/usr/bin"
  install -D -m755 usr/bin/* "$pkgdir/usr/bin/"
  install -D -m644 "etc/nvidia-container-runtime/config.toml" "$pkgdir/etc/nvidia-container-runtim/config.toml"
  install -D -m644 usr/share/licenses/$pkgname-*/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
