# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.101.2
pkgrel=1
pkgdesc="Visual Studio Code (vscode): Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64' 'aarch64' 'armv7h')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('code' 'vscode')
conflicts=('code')
# Upstream has signature verification for extensions and stripping breaks it
# See https://github.com/microsoft/vscode/issues/223455#issuecomment-2610001754
options=(!strip)
install=$pkgname.install
# lsof: needed for terminal splitting, see https://github.com/Microsoft/vscode/issues/62991
# xdg-utils: needed for opening web links with xdg-open
depends=(libxkbfile gnupg gtk3 libsecret nss gcc-libs libnotify libxss glibc lsof shared-mime-info xdg-utils alsa-lib)
optdepends=('glib2: Needed for move to trash functionality'
            'libdbusmenu-glib: Needed for KDE global menu'
            'org.freedesktop.secrets: Needed for settings sync'
             # See https://github.com/MicrosoftDocs/live-share/issues/4650
            'icu69: Needed for live share' )
source=(code-${pkgver}.desktop.in::https://raw.githubusercontent.com/microsoft/vscode/${pkgver}/resources/linux/code.desktop
        code-${pkgver}-url-handler.desktop.in::https://raw.githubusercontent.com/microsoft/vscode/${pkgver}/resources/linux/code-url-handler.desktop
        code-${pkgver}-workspace.xml.in::https://raw.githubusercontent.com/microsoft/vscode/${pkgver}/resources/linux/code-workspace.xml
        ${_pkgname}-bin.sh)
source_x86_64=(code_x64_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-x64/stable)
source_aarch64=(code_arm64_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-arm64/stable)
source_armv7h=(code_armhf_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-armhf/stable)

sha256sums=('2f1782b30c4e040efff655fd9cf477930c5a0c81ddae27749b0cbb922c1d248e'
            'c361efa7e02fcad759ed80d2fbab67877f33219b981578af6fffaf18aeb12d9b'
            '3af748dd6578a1775e8eb7248ba397b7e11840df2ea6ee234ff76fee3dc306cf'
            '8257a5ad82fa1f7dec11dfa064217b80df4cfec24f50cec7ca0ad62cf8295bfe')
sha256sums_x86_64=('ef62ab0835017bec498e7498fe79eb347f7610fe2da7bd71d5f69d8743ded033')
sha256sums_aarch64=('e4bd1902b8feecce5d8590c6cd88fa35ac5861911bf2af3d5619e0be3bb0ef04')
sha256sums_armv7h=('17218fbd0795cfcc8b84b8c51ad0973d354fbc2074fc45faa517b94420265d35')

_set_meta_info() {
  sed 's/@@NAME_LONG@@/Visual Studio Code/g' "$1" |\
  sed 's/@@NAME_SHORT@@/Code/g' |\
  sed 's/@@NAME@@/code/g' |\
  sed 's#@@EXEC@@#/usr/bin/code#g' |\
  sed 's/@@ICON@@/visual-studio-code/g' |\
  sed 's/@@URLPROTOCOL@@/vscode/g'
}

prepare() {
  _set_meta_info "${srcdir}/code-${pkgver}.desktop.in" > "${srcdir}/code.desktop"
  _set_meta_info "${srcdir}/code-${pkgver}-url-handler.desktop.in" > "${srcdir}/code-url-handler.desktop"
  _set_meta_info "${srcdir}/code-${pkgver}-workspace.xml.in" > "${srcdir}/code-workspace.xml"
}

_pkg() {
  if [ "${CARCH}" = "aarch64" ]; then
    echo 'VSCode-linux-arm64'
  elif [ "${CARCH}" = "armv7h" ]; then
    echo 'VSCode-linux-armhf'
  else
    echo 'VSCode-linux-x64'
  fi
}

package() {
  install -d "${pkgdir}/opt/${_pkgname}"
  install -d "${pkgdir}/usr/bin"
  install -d "${pkgdir}/usr/share/"{applications,pixmaps,mime/packages,licenses/${_pkgname}}

  install -m644 "${srcdir}/$(_pkg)/resources/app/LICENSE.rtf" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.rtf"
  install -m644 "${srcdir}/$(_pkg)/resources/app/resources/linux/code.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
  install -m644 "${srcdir}/code.desktop" "${pkgdir}/usr/share/applications/code.desktop"
  install -m644 "${srcdir}/code-url-handler.desktop" "${pkgdir}/usr/share/applications/code-url-handler.desktop"
  install -m644 "${srcdir}/code-workspace.xml" "${pkgdir}/usr/share/mime/packages/${pkgname}-workspace.xml"
  install -Dm 644 "${srcdir}/$(_pkg)/resources/completions/bash/code" "${pkgdir}/usr/share/bash-completion/completions/code"
  install -Dm 644 "${srcdir}/$(_pkg)/resources/completions/zsh/_code" "${pkgdir}/usr/share/zsh/site-functions/_code"

  cp -r "${srcdir}/$(_pkg)/"* "${pkgdir}/opt/${_pkgname}"

  # Launcher
	install -m755 "${srcdir}/${_pkgname}-bin.sh" "${pkgdir}/usr/bin/code"
}
