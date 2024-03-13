_name=skypeforlinux
pkgname=${_name}-bin
pkgver=8.113.0.210
pkgrel=2
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
source_x86_64=("${_name}-${pkgver}-x86_64.snap::https://api.snapcraft.io/api/v1/snaps/download/QRDEfjn4WJYnm0FzDKwqqRZZI77awQEV_330.snap")
sha256sums_x86_64=('ab0cc12e3967b991c8b059060449ab4fb5add3a8f2299f72c97f3fd7af8c0b05')

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
    install -dm755 "${pkg_bin}"
    ln -s '/opt/skypeforlinux/skypeforlinux' -t "${pkg_bin}"

    local pkg_app="${pkgdir}/usr/share/applications"
    mv "${pkgdir}/snap/gui" -T "${pkg_app}"
    sed -e 's/Exec=skype/Exec=skypeforlinux/;s/Icon=.*/Icon=skypeforlinux/' -i "${pkg_app}/"*
}
