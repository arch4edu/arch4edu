# Maintainer: leothelion <ponte-vecchio>

pkgname=positron-ide-devel-bin
_pkgname=positron-ide
pkgver=2025.12.0.167
pkgver_url=2025.12.0-167
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
    # python modules
    'ipython'
    'jupyter-nbclient'
    'jupyter-nbformat'
    'python-argcomplete'
    'python-asttokens'
    'python-cffi'
    'python-chardet'
    'python-colorama'
    'python-comm'
    'python-dateutil'
    'python-decorator'
    'python-docutils'
    'python-executing'
    'python-gobject'
    'python-greenlet'
    'python-importlib-metadata'
    'python-ipykernel'
    'python-jupyter-client'
    'python-jupyter-core'
    'python-markdown-it-py'
    'python-matplotlib-inline'
    'python-msgpack'
    'python-nest-asyncio'
    'python-numpy'
    'python-parso'
    'python-pexpect'
    'python-pickleshare'
    'python-pillow'
    'python-pip'
    'python-platformdirs'
    'python-pluggy'
    'python-prompt_toolkit'
    'python-psutil'
    'python-ptyprocess'
    'python-pure-eval'
    'python-pygments'
    'python-pyparsing'
    'python-pyqt5'
    'python-pytest'
    'python-pytz'
    'python-pyzmq'
    'python-requests'
    'python-six'
    'python-sphinx'
    'python-stack-data'
    'python-tomlkit'
    'python-tornado'
    'python-traitlets'
    'python-twisted'
    'python-typing_extensions'
    'python-wcwidth'
    'python-websockets'
    'python-wheel'
    'python-yaml'
    'python-zipp'
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
source_aarch64=("${posit_url}/arm64/Positron-${pkgver_url}-arm64.deb")
source_x86_64=("${posit_url}/x86_64/Positron-${pkgver_url}-x64.deb")
sha256sums_aarch64=('58ff142c2318dbaf1abfc5b43a9d23e8feabcbc3304e336c8d5d62255e74c138')
sha256sums_x86_64=('dd9e2644de56395d308f9d53ce8c82d307d4d59bbac0401bd604c7e481504488')

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