# Maintainer: Ivan Semkin (ivan at semkin dot ru)

pkgname=nvidia-docker
pkgver=2.0.3
pkgrel=4
pkgdesc='Build and run Docker containers leveraging NVIDIA GPUs'
url='https://github.com/NVIDIA/nvidia-docker'
arch=(any)
license=(BSD)
depends=(docker nvidia-container-runtime nvidia-container-runtime-hook)
source=("https://github.com/NVIDIA/nvidia-docker/archive/v$pkgver.tar.gz")
sha256sums=('f94c963b6d2a537711c7e8e9e3c3fe3d9f9fddc48599d5a411119276a33763db')

package() {
  cd "${pkgname}-${pkgver}"

  install -d ${pkgdir}/usr/bin
  install -m755 ${pkgname} ${pkgdir}/usr/bin/${pkgname}
  
  install -d ${pkgdir}/etc/docker
  install -m644 daemon.json ${pkgdir}/etc/docker/daemon.json
}
# vim:set ts=2 sw=2 et:
