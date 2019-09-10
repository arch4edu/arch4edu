# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>
# Maintainer: Kien Dang <mail at kien dot ai>

pkgname=nvidia-docker

pkgver=2.2.2
pkgrel=1

pkgdesc='Build and run Docker containers leveraging NVIDIA GPUs'
url='https://github.com/NVIDIA/nvidia-docker'
arch=(any)
license=(BSD)

depends=(docker nvidia-container-runtime)

source=("https://github.com/NVIDIA/nvidia-docker/archive/v${pkgver}.tar.gz")
sha256sums=('93b94208cd814b078313a458f6086acb6876b9a5b076a596fe8753d2d7b78622')

package() {
  cd "${pkgname}-${pkgver}"

  install -D -m755 "nvidia-docker" "${pkgdir}/usr/bin/nvidia-docker"
  install -D -m644 "daemon.json" "${pkgdir}/etc/docker/daemon.json"
  install -D -m644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
# vim:set ts=2 sw=2 et:
