# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>
# Maintainer: Kien Dang <mail at kien dot ai>

pkgname=nvidia-docker

pkgver=2.2.1
pkgrel=1

pkgdesc='Build and run Docker containers leveraging NVIDIA GPUs'
url='https://github.com/NVIDIA/nvidia-docker'
arch=(any)
license=(BSD)

depends=(docker nvidia-container-runtime)

source=("https://github.com/NVIDIA/nvidia-docker/archive/v${pkgver}.tar.gz")
sha256sums=('a63c55429fe4a42258aef4948222b8d7ae7d4003173988bf082de74fe5c54572')

package() {
  cd "${pkgname}-${pkgver}"

  install -D -m755 "nvidia-docker" "${pkgdir}/usr/bin/nvidia-docker"
  install -D -m644 "daemon.json" "${pkgdir}/etc/docker/daemon.json"
  install -D -m644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
# vim:set ts=2 sw=2 et:
