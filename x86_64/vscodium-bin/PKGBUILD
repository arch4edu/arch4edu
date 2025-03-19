# Maintainer: Carson Rueter <swurl at swurl dot x y z>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.98.2.25078
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
provides=('vscode' 'codium' 'vscodium')
conflicts=('vscodium')
install=$pkgname.install

sha256sums=('3a5bc109974fcf408855c13965f6d6be0997655c5b359de0bfd19a678c00844e'
            '6eef345b65bf2679c928c763529540435ab9c6e1836917319810a7a2d484ae1b'
            '01ba3d33e76804e2346d08f4eda256a29610c9eb59432e4b016d05ad93d901ba'
            '63b9f3e07dcfe92f59e851fdeeaed6ee986950672f75cc950489bce67e85d884'
            '07f0314b1869e3666f1ba52cd02dd40c841beef11a1ab9ae3246cafd01ef6caa')
sha256sums_x86_64=('aa2482acf49c3ed7e8c555e98daa4e52acc800794db17c1501935837a09eb90a')
sha256sums_aarch64=('c1ac7ab53164686b0ab0eae47dc5c5d72bc1b159947b13707bb01ec74e074bf4')

source=('vscodium-bin.desktop'
        'vscodium-bin-url-handler.desktop'
        'vscodium-bin.install'
        'vscodium-bin.sh'
        'vscodium-bin-wayland.desktop')
source_x86_64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-x64-${pkgver}.tar.gz")
source_aarch64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-arm64-${pkgver}.tar.gz")

shopt -s extglob

package() {
  install -d -m755 "${pkgdir}/opt/${pkgname}"
  install -d -m755 "${pkgdir}/usr/bin"
  install -d -m755 "${pkgdir}/usr/share/"{applications,pixmaps}
  cp -r "${srcdir}"/!(vscodium-bin?(-url-handler).desktop|${_pkgname}-linux-@(x|arm)64-${pkgver}.tar.gz) "${pkgdir}/opt/${pkgname}"
  ln -s "/opt/${pkgname}/bin/codium" "${pkgdir}/usr/bin/codium"
  ln -s "/opt/${pkgname}/bin/codium" "${pkgdir}/usr/bin/vscodium"
  install -D -m644 "${srcdir}/vscodium-bin.desktop" "${pkgdir}/usr/share/applications/codium.desktop"
  install -D -m644 "${srcdir}/vscodium-bin-wayland.desktop" "${pkgdir}/usr/share/applications/codium-wayland.desktop"
  install -D -m644 "${srcdir}/vscodium-bin-url-handler.desktop" "${pkgdir}/usr/share/applications/codium-url-handler.desktop"
  install -D -m644 "${srcdir}/resources/app/resources/linux/code.png" \
          "${pkgdir}/usr/share/pixmaps/vscodium.png"
  install -D -m644 "${srcdir}/resources/app/resources/linux/code.png" \
          "${pkgdir}/usr/share/icons/hicolor/1024x1024/apps/vscodium.png"
  install -m755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/codium"

  # Fix chrome-sandbox permissions
  chown root "${pkgdir}/opt/${pkgname}/chrome-sandbox"
  chmod 4755 "${pkgdir}/opt/${pkgname}/chrome-sandbox"

  # Symlink shell completions
  install -d -m755 "${pkgdir}/usr/share/zsh/site-functions"
  install -d -m755 "${pkgdir}/usr/share/bash-completion/completions"
  ln -s "/opt/${pkgname}/resources/completions/zsh/_codium" "${pkgdir}/usr/share/zsh/site-functions"
  ln -s "/opt/${pkgname}/resources/completions/bash/codium" "${pkgdir}/usr/share/bash-completion/completions"
}
