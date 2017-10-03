# Maintainer: Benjamin Chretien <chretien at lirmm dot fr>

pkgname=cub
pkgver=1.4.1
pkgrel=1
pkgdesc="A flexible library of cooperative threadblock primitives and other utilities for CUDA kernel programming."
arch=('any')
url='http://nvlabs.github.com/cub/'
license=('New BSD')
makedepends=()
optdepends=('cuda')

source=("https://github.com/NVlabs/cub/archive/${pkgver}.zip"
        "cub.pc")
sha256sums=('f464eda366e4dfe0c1d9ae2a6bbc22c5804cf131f8a67974c01fae4ae8213e8b'
            'de2d52cbdb9a81936c7cc519cc5a68c4c62012755c2ab3a07bba158a9d4626c4')

package() {
  cd "${srcdir}/cub-${pkgver}"

  # Install headers
  install -d "${pkgdir}/usr/include/cub"
  cp -r "cub" "${pkgdir}/usr/include"

  # Install pkg-config file
  install -Dm644 "${srcdir}/cub.pc" "${pkgdir}"/usr/lib/pkgconfig/cub.pc
}
