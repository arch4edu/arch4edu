# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.91.1
pkgrel=1
pkgdesc="Visual Studio Code (vscode): Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64' 'aarch64' 'armv7h')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('code' 'vscode')
conflicts=('code')
install=$pkgname.install
# lsof: needed for terminal splitting, see https://github.com/Microsoft/vscode/issues/62991
# xdg-utils: needed for opening web links with xdg-open
depends=(libxkbfile gnupg gtk3 libsecret nss gcc-libs libnotify libxss glibc lsof shared-mime-info xdg-utils alsa-lib)
optdepends=('glib2: Needed for move to trash functionality'
            'libdbusmenu-glib: Needed for KDE global menu'
            'org.freedesktop.secrets: Needed for settings sync'
             # See https://github.com/MicrosoftDocs/live-share/issues/4650
            'icu69: Needed for live share' )
source=(code.desktop code-url-handler.desktop ${_pkgname}-workspace.xml ${_pkgname}-bin.sh)
source_x86_64=(code_x64_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-x64/stable)
source_aarch64=(code_arm64_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-arm64/stable)
source_armv7h=(code_armhf_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-armhf/stable)

# This generates cleaner checksums
sha256sums=('b8d55bc61c7c974087930168c2ff93e3ff28cf09e023d02db410d6e5723c361a'
            '89a417423b3acfb3ed1d044cb4c12014241f3c67f494d651e9bddffce1f85b82'
            '24ba09a6398c9781ed7cb6f1a9f6f38ec204899ba1f33db92638bf6d3cb0aed6'
            '8257a5ad82fa1f7dec11dfa064217b80df4cfec24f50cec7ca0ad62cf8295bfe')
sha256sums_x86_64=('8049c311aadce5893c1311db0b9254df6c1d44fe7f7281976a9d21563987f045')
sha256sums_aarch64=('c9730ddc7dd62eebe83dd8c13761dce283121b4d25344de909d005da51280e58')
sha256sums_armv7h=('79329f572a2262fb7908996570859f2d90253c14a64ba93dca38e68ff106bb89')



package() {
  _pkg=VSCode-linux-x64
  if [ "${CARCH}" = "aarch64" ]; then
    _pkg=VSCode-linux-arm64
  fi
  if [ "${CARCH}" = "armv7h" ]; then
    _pkg=VSCode-linux-armhf
  fi
  if [ "${CARCH}" = "i686" ]; then
    _pkg=VSCode-linux-ia32
  fi

  install -d "${pkgdir}/usr/share/licenses/${_pkgname}"
  install -d "${pkgdir}/opt/${_pkgname}"
  install -d "${pkgdir}/usr/bin"
  install -d "${pkgdir}/usr/share/applications"
  install -d "${pkgdir}/usr/share/icons"
  install -d "${pkgdir}/usr/share/mime/packages"

  install -m644 "${srcdir}/${_pkg}/resources/app/LICENSE.rtf" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.rtf"
  install -m644 "${srcdir}/${_pkg}/resources/app/resources/linux/code.png" "${pkgdir}/usr/share/icons/${_pkgname}.png"
  install -m644 "${srcdir}/code.desktop" "${pkgdir}/usr/share/applications/code.desktop"
  install -m644 "${srcdir}/code-url-handler.desktop" "${pkgdir}/usr/share/applications/code-url-handler.desktop"
  install -m644 "${srcdir}/${_pkgname}-workspace.xml" "${pkgdir}/usr/share/mime/packages/${pkgname}-workspace.xml"
  install -Dm 644 "${srcdir}/${_pkg}/resources/completions/bash/code" "${pkgdir}/usr/share/bash-completion/completions/code"
  install -Dm 644 "${srcdir}/${_pkg}/resources/completions/zsh/_code" "${pkgdir}/usr/share/zsh/site-functions/_code"

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${_pkgname}"

  # Launcher
	install -m755 "${srcdir}/${_pkgname}-bin.sh" "${pkgdir}/usr/bin/code"
}

