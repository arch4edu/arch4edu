# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
pkgname=cub
pkgver=1.7.4
pkgrel=1
pkgdesc="A flexible library of cooperative threadblock primitives and other utilities for CUDA kernel programming."
arch=('any')
url='http://nvlabs.github.com/cub/'
license=('custom')
optdepends=('cuda')
source=("https://github.com/NVlabs/cub/archive/${pkgver}.zip"
        "cub.pc")
sha256sums=('20a1a39fd97e5da7f40f5f2e7fd73fd2ea59f9dc4bb8a6c5f228aa543e727e31'
            '5003a9ee6d7dfa32bbdfbd67d2a7cfcc6c1ca54630c85012ec0b18b519d80230')

package() {
  cd "${srcdir}/cub-${pkgver}"

  # Install headers
  install -d "${pkgdir}/usr/include/cub"
  cp -r "cub" "${pkgdir}/usr/include"

  # Install pkg-config file
  install -Dm644 "${srcdir}/cub.pc" "${pkgdir}"/usr/lib/pkgconfig/cub.pc

  install -Dm644 LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
