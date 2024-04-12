_name=skypeforlinux
pkgname=${_name}-bin
pkgver=8.117.0.202
pkgrel=1
pkgdesc='Skype for Linux'
arch=('x86_64')
url='https://www.skype.com/'
license=('custom')
provides=("${_name}" 'skype')
conflicts=("${_name}" 'skype')
options=('!strip' '!emptydirs')

depends=(
    'alsa-lib'
    'glibc'
    'gtk3'
    'libsecret'
    'libxss'
    'libxtst'
    'nss'
)

makedepends=(
    'squashfs-tools'
)

optdepends=(
    'org.freedesktop.secrets: keyring/password support'
    'libappindicator-gtk3: system tray icon support'
)

# curl -H 'Snap-Device-Series: 16' 'https://api.snapcraft.io/v2/snaps/info/skype'
source=('flags.sh')
source_x86_64=("${_name}-${pkgver}-x86_64.snap::https://api.snapcraft.io/api/v1/snaps/download/QRDEfjn4WJYnm0FzDKwqqRZZI77awQEV_342.snap")

sha256sums=('d83693ffd8034c21030262ac00ce529c8da7b0196ea4b4eb2168861fc2657a2a')
sha256sums_x86_64=('7b8acb67490139ee4ab8be9756ed32345850f4ad018babf106d3e073e1f3e053')

package() {
    local sname="source_${CARCH}"

    local extract=(
        'snap/gui/*.desktop'
        'usr/share/icons/hicolor/*/apps'
        'usr/share/pixmaps'
        'usr/share/skypeforlinux'
    )

    unsquashfs -d "${pkgdir}" "${!sname[0]%::*}" "${extract[@]}"

    local pkg_opt="${pkgdir}/opt"
    install -dm755 "${pkg_opt}"
    mv "${pkgdir}/usr/share/skypeforlinux" -t "${pkg_opt}"

    local pkg_bin="${pkgdir}/usr/bin"
    local exec="${pkg_bin}/${_name}"
    install -dm755 "${pkg_bin}"
    sed -e 's|@NAME@|skypeforlinux|;s|@EXEC@|/opt/skypeforlinux/skypeforlinux|' "${source[0]}" > "${exec}"
    chmod 755 "${exec}"

    local pkg_app="${pkgdir}/usr/share/applications"
    mv "${pkgdir}/snap/gui" -T "${pkg_app}"
    sed -e 's/Exec=skype/Exec=skypeforlinux/;s/Icon=.*/Icon=skypeforlinux/' -i "${pkg_app}/"*
}
