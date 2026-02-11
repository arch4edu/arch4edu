# Maintainer: Carson Rueter <swurl at swurl dot x y z>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.109.01000
pkgrel=1
pkgdesc="Binary releases of VS Code without MS branding/telemetry/licensing."
arch=('x86_64' 'aarch64')
url="https://github.com/VSCodium/vscodium"
license=('MIT')
depends=(
        fontconfig libxtst gtk3 python cairo alsa-lib nss gcc-libs libnotify libxss
        'glibc>=2.28-4' bash
        )
optdepends=(
        'gvfs: For move to trash functionality'
        'libdbusmenu-glib: For KDE global menu'
)
options=('!emptydirs' '!strip' '!debug')
provides=('vscode' 'codium' 'vscodium')
conflicts=('vscodium')
install=$pkgname.install

sha256sums=('3a5bc109974fcf408855c13965f6d6be0997655c5b359de0bfd19a678c00844e'
            '121f2db8a65cfc74c10d3e7c3135b62b66297cf27f8f7f00c3ad29d412e968b7'
            '01ba3d33e76804e2346d08f4eda256a29610c9eb59432e4b016d05ad93d901ba'
            '63b9f3e07dcfe92f59e851fdeeaed6ee986950672f75cc950489bce67e85d884'
            '2fa3f8948a0a17ea30b62845caf1ee8aae8b55b5417273920ca2df2642209e0e')
sha256sums+=('e622e6bdb70b0cfec57ad9df8717ea023b87e5e215003119b5a1a4d059fcd347')
sha256sums_x86_64=('32e52a31b292e66c93a5be124bd520f9176b1c0971cb69dcbf084cb78283021f')
sha256sums_aarch64=('2754d0f31d1fea52687d19a832f6953f1ec669095d727332c9716826996608bc')

source=('vscodium-bin.desktop'
        'vscodium-bin-url-handler.desktop'
        'vscodium-bin.install'
        'vscodium-bin.sh'
        'LICENSE')
source+=("https://raw.githubusercontent.com/VSCodium/vscodium/refs/tags/${pkgver}/src/stable/resources/linux/code.svg")
source_x86_64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-x64-${pkgver}.tar.gz")
source_aarch64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-arm64-${pkgver}.tar.gz")

shopt -s extglob

package() {
  install -d -m755 "${pkgdir}/opt/${pkgname}"
  install -d -m755 "${pkgdir}/usr/bin"
  install -d -m755 "${pkgdir}/usr/share/"{applications,pixmaps}
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  cp -r * "${pkgdir}/opt/${pkgname}"
  # remove source file links
  find "${pkgdir}/opt/${pkgname}" -maxdepth 1 -type l -delete
  ln -s "/opt/${pkgname}/bin/codium" "${pkgdir}/usr/bin/codium"
  ln -s "/opt/${pkgname}/bin/codium" "${pkgdir}/usr/bin/vscodium"
  install -D -m644 "vscodium-bin.desktop" "${pkgdir}/usr/share/applications/codium.desktop"
  install -D -m644 "vscodium-bin-url-handler.desktop" "${pkgdir}/usr/share/applications/codium-url-handler.desktop"
  install -D -m644 "resources/app/resources/linux/code.png" \
          "${pkgdir}/usr/share/pixmaps/vscodium.png"
  install -D -m644 "code.svg" \
          "${pkgdir}/usr/share/icons/hicolor/scalable/apps/vscodium.svg"
  install -m755 "${pkgname}.sh" "${pkgdir}/usr/bin/codium"

  install -Dm4755 chrome-sandbox "${pkgdir}/opt/${pkgname}/chrome-sandbox"

  # Symlink shell completions
  install -d -m755 "${pkgdir}/usr/share/zsh/site-functions"
  install -d -m755 "${pkgdir}/usr/share/bash-completion/completions"
  ln -s "/opt/${pkgname}/resources/completions/zsh/_codium" "${pkgdir}/usr/share/zsh/site-functions"
  ln -s "/opt/${pkgname}/resources/completions/bash/codium" "${pkgdir}/usr/share/bash-completion/completions"
}
