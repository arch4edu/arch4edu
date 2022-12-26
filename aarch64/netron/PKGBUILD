# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Filipe Bertelli <filipebertelli@tutanota.com>
# Contributor: J. C. Hammons <jch at bitma dot st>
# Contributor: Amr Okasha <amradel55 at gmail dot com>
# Contributor: Dimitris Kiziridis <ragouel at outlook dot com>

pkgbase=netron
pkgname=(netron)
##pkgname+=(netron-cli)
pkgdesc='Visualizer for neural network, deep learning, and machine learning models'
pkgver=6.3.6
pkgrel=1
url='https://netron.app/'
arch=(x86_64)
license=(MIT)
depends=(python)
makedepends=(gendesk npm python-setuptools python-build python-installer python-wheel)
optdepends=(
  'python-onnx: serializing ONNX models'
  'python-pytorch: serializing PyTorch models'
)
source=("https://github.com/lutzroeder/netron/archive/v${pkgver}/netron-${pkgver}.tar.gz")
sha256sums=('2941bf4305376be2d09f0c08b87c698ac735c00a7eb97cb12815896f2cbc4a45')

prepare() {
  cd "${pkgbase}-${pkgver}"

  # Use dependencies from Arch
  sed '/python -m pip/d' -i Makefile

  # Disable mac and windows builds
  sed -e '/--mac /d' -e '/--win /d' -i Makefile
}

build() {
  cd "${pkgbase}-${pkgver}"
  make clean build_python build_electron
}

package_netron() {
  depends+=('gtk3' 'nss' 'dbus-glib' 'libdbusmenu-glib')
  provides=('netron' 'netron-cli')
  conflicts=('netron-cli' 'netron-bin')

  cd "${pkgbase}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/pypi/*.whl
  #mv "${pkgdir}/usr/bin/${pkgbase}" "${pkgdir}/usr/bin/${pkgbase}-cli"

  mkdir -p "${pkgdir}/opt/"
  cp -r dist/linux-unpacked "${pkgdir}/opt/${pkgname}"
  #ln -s "/opt/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

  install -Dm644 publish/icon.png "${pkgdir}/usr/share/pixmaps/${pkgbase}.png"
  gendesk -f -n --pkgname "${pkgname}" \
          --pkgdesc "${pkgdesc}" \
          --name "Netron" \
          --comment "${pkgdesc}" \
          --exec "/opt/${pkgname}/${pkgname}" \
          --categories 'Development;Application;' \
          --icon "${pkgname}"
  install -Dm644 "${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"

  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}

package_netron-cli() {
  pkgdesc="${pkgdesc} (CLI only)"
  arch=(any)
  conflicts=('netron')

  cd "${pkgbase}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/pypi/*.whl
  #mv "${pkgdir}/usr/bin/${pkgbase}" "${pkgdir}/usr/bin/${pkgbase}-cli"

  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
