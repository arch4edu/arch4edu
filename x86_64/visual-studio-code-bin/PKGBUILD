# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.88.0
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
sha256sums=('10a5ee77a89fc934bcbd3e2a41a2ec4bd51d3cd048702f6d739ecec9eb3a7c4b'
            '2264dd138b77358709aa49fb3a7fe7d1b05b7ab0715760d66958000107bdd3dc'
            '24ba09a6398c9781ed7cb6f1a9f6f38ec204899ba1f33db92638bf6d3cb0aed6'
            '8257a5ad82fa1f7dec11dfa064217b80df4cfec24f50cec7ca0ad62cf8295bfe')
sha256sums_x86_64=('aeaf16500a4fdcb0db855f60be8bcadb4a3641b662907c219c37fb25d71d284f')
sha256sums_aarch64=('b1af885c58952362140273b3bb3d6492e841a1f2921284060899628d4452e32e')
sha256sums_armv7h=('f63b75d68242064ebcc8c46fd335e5ac19f23d8eac81139efbc3fdfd582c319b')



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

