# Maintainer: leothelion <ponte-vecchio>

pkgname=positron-ide-devel-bin
_pkgname=positron-ide
pkgver=2026.10.2.3
pkgver_url=2026.10.2-3
pkgrel=1
pkgdesc="A next-generation data science IDE. Positron is an extensible, polyglot tool for writing code and exploring data in Python, R, and other languages."
arch=('x86_64' 'aarch64')
options=('!debug')
url="https://github.com/posit-dev/positron"
posit_url="https://cdn.posit.co/positron/releases/deb"
licence=('Elastic-2.0')
license=('Elastic-2.0')
depends=(
    'ca-certificates'
    'alsa-lib'
    'at-spi2-core'
    'atkmm'
    # 'glibc' # mesa
    # 'cairo' # pango
    'libcups'
    'curl'
    'dbus'
    # 'libdrm' # mesa
    # 'expat' # mesa
    'mesa'
    # 'glib2' # pango
    'krb5'
    'gtk3'
    'gtk4'
    # 'nspr' # nss
    'nss'
    'pango'
    # 'gcc-libs' # mesa
    'systemd-libs' # for udev1
    # 'libx11' # mesa, pango
    # 'libxcb' # mesa
    'libxcomposite'
    'libxdamage'
    # 'libxext' # mesa
    # 'libxfixes' # mesa
    'libxkbcommon'
    # 'libxkbfile' # mesa
    'libxrandr'
    'xdg-utils'
)
optdepends=(
    'vulkan-intel: Intel Vulkan driver'
    'vulkan-radeon: Radeon Vulkan driver'
    'vulkan-icd-loader: Vulkan ICD loader'
    'bash-completion: Bash completion support'
    'zsh-completions: Zsh completion support'
    'nodejs: Extra functionality for Positron'
)
provides=("positron")
conflicts=("positron-bin")
source_x86_64=("${posit_url}/x86_64/Positron-${pkgver_url}-x64.deb")
source_aarch64=("${posit_url}/arm64/Positron-${pkgver_url}-arm64.deb")
sha256sums_x86_64=('2131efacd9d0227cf50db49c1ced2d976745342200a946ebbe1d95e78e6d6601')
sha256sums_aarch64=('cf2d524dfceba8abf2c62104e2dd7fe173da5c5ac63fad40ffa7581f857a7c7c')

package(){
    shopt -s extglob

    msg "Converting .deb package"
    if [ "${CARCH}" = "x86_64" ]; then
        ar x Positron-${pkgver_url}-x64.deb
    elif [ "${CARCH}" = "aarch64" ]; then
        ar x Positron-${pkgver_url}-arm64.deb
    fi

    cd "${srcdir}"
    tar --extract --xz --file data.tar.xz -C "${pkgdir}"

    # copy licence from root directory
    # msg "Copying licence"
    # install -Dm644 "../LICENCE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    msg "Installing"
    install -d "${pkgdir}/usr/share/appdata"
    install -d "${pkgdir}/usr/share/applications"
    install -d "${pkgdir}/usr/share/mime/packages"
    install -d "${pkgdir}/usr/share/positron"
}