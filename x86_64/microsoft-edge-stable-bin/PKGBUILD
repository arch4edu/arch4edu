# Maintainer: Nicolas Narvaez <nicomix1006@gmail.com>
# Contributor: EsauPR
# Contributor: bittin

pkgname=microsoft-edge-stable-bin
_pkgname=microsoft-edge
_pkgshortname=msedge
pkgver=108.0.1462.54
pkgrel=1
pkgdesc="A browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier"
arch=('x86_64')
url="https://www.microsoftedgeinsider.com/en-us/download"
license=('custom')
provides=('microsoft-edge-stable' 'edge-stable')
conflicts=('microsoft-edge-stable' 'edge-stable' 'edge-stable-bin' 'edge')
depends=('gtk3' 'libcups' 'nss' 'alsa-lib' 'libxtst' 'libdrm' 'mesa')
makedepends=('imagemagick')
optdepends=('libpipewire02: WebRTC desktop sharing under Wayland'
            'kdialog: for file dialogs in KDE'
            'gnome-keyring: for storing passwords in GNOME keyring'
            'kwallet: for storing passwords in KWallet'
            'libunity: for download progress on KDE'
            'ttf-liberation: fix fonts for some PDFs - CRBug #369991'
            'xdg-utils')
options=(!strip !zipman)
_channel=stable
source=("https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/${_pkgname}-stable_${pkgver}-1_amd64.deb"
        "microsoft-edge-stable.sh"
        "Microsoft Standard Application License Terms - Standalone (free) Use Terms.pdf")
sha256sums=('829ab60a9c5ffbab4a13edcf678db4e76dc844f3b7549386b443760d0ade899f'
            'dc3765d2de6520b13f105b8001aa0e40291bc9457ac508160b23eea8811e26af'
            'edf2ed596eb068f168287fc76aa713ad5e0afb59f0a0a47a4f29c0c124ade15e')

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"

	# suid sandbox
	chmod 4755 "${pkgdir}/opt/microsoft/${_pkgshortname}/msedge-sandbox"

	# 256 and 24 are proper colored icons
	for res in 128 64 48 32; do
		convert "${pkgdir}/opt/microsoft/${_pkgshortname}/product_logo_256.png" \
			-resize ${res}x${res} \
			"${pkgdir}/opt/microsoft/${_pkgshortname}/product_logo_${res}.png"
	done
	for res in 22 16; do
		convert "${pkgdir}/opt/microsoft/${_pkgshortname}/product_logo_24.png" \
			-resize ${res}x${res} \
			"${pkgdir}/opt/microsoft/${_pkgshortname}/product_logo_${res}.png"
	done

	# install icons
	for res in 16 22 24 32 48 64 128 256; do
		install -Dm644 "${pkgdir}/opt/microsoft/${_pkgshortname}/product_logo_${res}.png" \
			"${pkgdir}/usr/share/icons/hicolor/${res}x${res}/apps/${_pkgname}.png"
	done
       # User flag aware launcher
       install -m755 microsoft-edge-stable.sh "${pkgdir}/usr/bin/microsoft-edge-stable"

	# License
	install -Dm644 'Microsoft Standard Application License Terms - Standalone (free) Use Terms.pdf' "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.pdf"
	rm -r "${pkgdir}/etc/cron.daily/" "${pkgdir}/opt/microsoft/${_pkgshortname}/cron/"
	# Globbing seems not to work inside double parenthesis
	rm "${pkgdir}/opt/microsoft/${_pkgshortname}"/product_logo_*.png
}
