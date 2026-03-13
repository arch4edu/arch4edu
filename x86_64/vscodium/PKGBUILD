# Maintainer: Cedric Roijakkers <cedric [the at sign goes here] roijakkers [the dot sign goes here] be>.
# Inspired from the PKGBUILD for vscodium-bin and code-stable-git.

pkgname=vscodium
# Make sure the pkgver matches the git tags in vscodium and vscode git repo's!
pkgver=1.110.11631
pkgrel=3
pkgdesc="Free/Libre Open Source Software Binaries of VSCode (git build from latest release)."
arch=('x86_64' 'aarch64' 'armv7h')
url='https://github.com/VSCodium/vscodium.git'
license=('MIT')
options=(!strip !debug)
depends=(
    'fontconfig'
    'libxtst'
    'gtk3'
    'cairo'
    'alsa-lib'
    'nss'
    'libnotify'
    'libxss'
    'glibc>=2.28-4'
    'libxkbfile'
)
optdepends=(
    'gvfs: For move to trash functionality'
    'libdbusmenu-glib: For KDE global menu'
)
makedepends=(
    'nvm'
    'gulp'
    'yarn'
    'jq'
    'libxdmcp'
    'git'
    'git-lfs'
    'patch'
    'python'
    'python-distutils-extra'
    'pkg-config'
    'rustup'
)
source=(
    "${pkgname}.desktop"
    "${pkgname}-wayland.desktop"
    "${pkgname}-uri-handler.desktop"
    "https://github.com/VSCodium/vscodium/releases/download/${pkgver}/VSCodium-${pkgver}-src.tar.gz"
)
sha256sums=(
    '7c6864be64a7cb698340c45b4cfc0091a1d9bb78b0e73d7e3a25d8a0b438beec'
    '74509d8ccb685a6d55e8bba8f4231963b766e1e3e38443bc1e72238519dcdeac'
    '3ad1e6bbd7cdc8833eff9afaa9f6ae39350d738678cafbe3437106f0cfe3d985'
    '6f9b0faf38579ee0c7f331c0bc78e0a6a7cd8e0d17ce5a2e6ecc709475daf96e'
)
provides=(
    'codium'
    'vscodium'
)
conflicts=(
    'codium'
    'vscodium'
    'vscodium-bin'
    'vscodium-git'
)

###############################################################################

# Even though we don't officially support other archs, let's allow the
# user to use this PKGBUILD to compile the package for their architecture.
case "$CARCH" in
  x86_64)
    _vscode_arch=x64
    ;;
  aarch64)
    _vscode_arch=arm64
    ;;
  armv7h)
    _vscode_arch=arm
    ;;
  *)
    # Needed for mksrcinfo
    _vscode_arch=DUMMY
    ;;
esac

build() {
    # Deactivate any pre-loaded nvm, and make sure we use our own in the current source directory
    command -v nvm >/dev/null && nvm deactivate && nvm unload
    export NVM_DIR="${srcdir}/.nvm"
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]

    # Install the correct version of NodeJS (read from .nvmrc)
    nvm install $(cat .nvmrc)
    nvm use

    # Check if the correct version of node is being used
    nvmrc_version="$(cat .nvmrc)"
    if [[ "$nvmrc_version" != "v"* ]]
    then
        # Add the v prefix, because it seems to be missing in .nvmrc
        echo "Configured .nvmrc version is [$nvmrc_version], adding the v prefix before checking if it matches with the node command."
        nvmrc_version="v$nvmrc_version"
    fi

    # Now check if the version matches exactly, or at least starts with the same prefix
    if [[ "$(node --version)" != "$nvmrc_version"* ]]
    then
    	echo "Using the wrong version of NodeJS! Expected ["$nvmrc_version"] but using ["$(node --version)"]."
    	exit 1
    fi
    echo "Installed version of node ["$(node --version)"] matches required version ["$nvmrc_version"], continuing."

    rustup default stable

    # Remove old build
    if [ -d "vscode" ]; then
        rm -rf vscode* VSCode*
    fi

    # Export necessary environment variables
    export SHOULD_BUILD="yes"
    export SHOULD_BUILD_REH="no"
    export SHOULD_BUILD_REH_WEB="no"
    export CI_BUILD="no"
    export OS_NAME="linux"
    export VSCODE_ARCH="${_vscode_arch}"
    export VSCODE_QUALITY="stable"
    export RELEASE_VERSION="${pkgver}"
    # the app will be updated with pacman
    export DISABLE_UPDATE="yes"

    . get_repo.sh
    . build.sh
}

package() {
    install -d -m755 ${pkgdir}/usr/bin
    install -d -m755 ${pkgdir}/usr/share/{${pkgname},applications,pixmaps}
    install -d -m755 ${pkgdir}/usr/share/licenses/${pkgname}

    cp -r ${srcdir}/VSCode-linux-${_vscode_arch}/* ${pkgdir}/usr/share/${pkgname}
    cp -r ${srcdir}/VSCode-linux-${_vscode_arch}/resources/app/LICENSE.txt ${pkgdir}/usr/share/licenses/${pkgname}

    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium

    install -D -m644 ${pkgname}.desktop ${pkgdir}/usr/share/applications/${pkgname}.desktop
    install -D -m644 ${pkgname}-wayland.desktop ${pkgdir}/usr/share/applications/${pkgname}-wayland.desktop
    install -D -m644 ${pkgname}-uri-handler.desktop ${pkgdir}/usr/share/applications/${pkgname}-uri-handler.desktop
    install -D -m644 ${srcdir}/VSCode-linux-${_vscode_arch}/resources/app/resources/linux/code.png ${pkgdir}/usr/share/pixmaps/${pkgname}.png
    install -D -m644 ${srcdir}/src/stable/resources/linux/code.svg ${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg

    # Symlink shell completions
    install -d -m755 ${pkgdir}/usr/share/zsh/site-functions
    install -d -m755 ${pkgdir}/usr/share/bash-completion/completions
    ln -s /usr/share/${pkgname}/resources/completions/zsh/_codium ${pkgdir}/usr/share/zsh/site-functions
    ln -s /usr/share/${pkgname}/resources/completions/bash/codium ${pkgdir}/usr/share/bash-completion/completions
}
