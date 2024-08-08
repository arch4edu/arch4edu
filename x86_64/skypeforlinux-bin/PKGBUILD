# curl -H 'Snap-Device-Series: 16' 'https://api.snapcraft.io/v2/snaps/info/skype'
_snap_id='QRDEfjn4WJYnm0FzDKwqqRZZI77awQEV'
_snap_rev_x86_64=353

_name=skypeforlinux
pkgname=${_name}-bin
pkgver=8.125.0.201
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
    'bash'
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

_get_source() {
    local rname="_snap_rev_${1}"
    echo -n "${_name}-${pkgver}-${1}.snap::https://api.snapcraft.io/api/v1/snaps/download/${_snap_id}_${!rname}.snap"
}

source=('flags.sh')
source_x86_64=("$(_get_source 'x86_64')")

sha256sums=('d83693ffd8034c21030262ac00ce529c8da7b0196ea4b4eb2168861fc2657a2a')
sha256sums_x86_64=('a719f3429acdbb77e6ff7f69f971bf181c24b49a6cbdb90729e0671b134f29ff')

package() {
    local sname="source_${CARCH}"

    local extract=(
        'snap/gui/*.desktop'
        'usr/share/icons/hicolor/*/apps'
        'usr/share/pixmaps'
        'usr/share/skypeforlinux'
    )

    unsquashfs -no-xattrs -d "${pkgdir}" "${!sname[0]%::*}" "${extract[@]}"

    local pkg_opt="${pkgdir}/opt"
    install -dm755 "${pkg_opt}"
    mv "${pkgdir}/usr/share/skypeforlinux" -t "${pkg_opt}"

    sed -e 's|@NAME@|skypeforlinux|;s|@EXEC@|/opt/skypeforlinux/skypeforlinux|' "${source[0]}" |
        install -Dm755 '/dev/stdin' -T "${pkgdir}/usr/bin/${_name}"

    local pkg_app="${pkgdir}/usr/share/applications"
    mv "${pkgdir}/snap/gui" -T "${pkg_app}"
    sed -e 's/^Exec=skype/Exec=skypeforlinux/;s/^Icon=.*/Icon=skypeforlinux/' -i "${pkg_app}/"*

    chmod -R go-w "${pkgdir}"
}
