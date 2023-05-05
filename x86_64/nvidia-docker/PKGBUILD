# Maintainer: Julie Shapiro <jshapiro at nvidia dot com>
# Maintainer: Kien Dang <mail at kien dot ai>

pkgname=nvidia-docker

pkgver=2.13.0
pkgrel=1

pkgdesc='Build and run Docker containers leveraging NVIDIA GPUs'
url='https://github.com/NVIDIA/nvidia-docker'
arch=(any)
license=(BSD)

depends=(docker 'nvidia-container-runtime>=3.12.0' 'nvidia-container-toolkit>=1.12.0')

source=("https://github.com/NVIDIA/nvidia-docker/archive/v${pkgver}.tar.gz")
sha256sums=('0df0c4efd4a8efb615226d0f68e44f8abb45935223c3be0de8fbcb072a984c0d')

package() {
  cd "${pkgname}-${pkgver}"

  install -D -m755 "nvidia-docker" "${pkgdir}/usr/bin/nvidia-docker"
  install -D -m644 "daemon.json" "${pkgdir}/etc/docker/daemon.json"
  install -D -m644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
# vim:set ts=2 sw=2 et:
