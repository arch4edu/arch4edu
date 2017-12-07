# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Adria Arrufat <adria.arrufat AT protonmail+aur DOT com>
# Contributor: Sami B. <spidermario@free.fr>
# Contributor: Yunhui Fu <yhfdev@gmail.com>
pkgname=cudnn6
pkgver=6.0.21
pkgrel=2
pkgdesc="NVIDIA CUDA Deep Neural Network library (version 6)"
arch=('x86_64')
url="https://developer.nvidia.com/cuDNN"
license=('proprietary')
depends=('cuda-8.0')
source=("http://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-8.0-linux-x64-v6.0.tgz")
sha512sums=('ddeeacb5b449920d942a26b98c353d78fd6f7d7fb3b3ce42a078626473efdda25c7ae641232702d62eb5749e39ecfd03e88346119c920c19348ac3ee82d3ff47')

package() {
  mkdir -p "${pkgdir}/opt"
  mkdir -p "${pkgdir}/etc"

  cp -r cuda "${pkgdir}/opt/cudnn6"

  install -d ${pkgdir}/etc/ld.so.conf.d
  echo "/opt/cudnn6/lib64/" > ${pkgdir}/etc/ld.so.conf.d/cudnn6.conf
}
# vim: ft=sh syn=sh et
