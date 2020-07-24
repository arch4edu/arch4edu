# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
pkgname=cub
pkgver=1.9.10
pkgrel=1
pkgdesc="A flexible library of cooperative threadblock primitives and other utilities for CUDA kernel programming."
arch=('any')
url='http://nvlabs.github.com/cub/'
license=('custom')
optdepends=('cuda')
source=("https://github.com/NVlabs/cub/archive/${pkgver}.zip"
        "cub.pc")
sha256sums=('063fea7c9bf87677a5fc5889e3fcd51582b77a2b3af9fa599d846a9c98ce9407'
            '93707c5fd3a2f93e825fc9cde8133fc525c7e5d6f22bbb006f494de74930bf87')

package() {
  cd "${srcdir}/cub-${pkgver}"

  # Install headers
  install -d "${pkgdir}/usr/include/cub"
  cp -r "cub" "${pkgdir}/usr/include"

  # Install pkg-config file
  install -Dm644 "${srcdir}/cub.pc" "${pkgdir}"/usr/lib/pkgconfig/cub.pc

  install -Dm644 LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
