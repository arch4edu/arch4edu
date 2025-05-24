# Maintainer: Nicolas Narvaez <nicomix1006@gmail.com>
# Co-Maintainer: Aakash Hemadri <aakashhemadri123@gmail.com>
# Contributor: EsauPR
# Contributor: bittin
# Contributor: nowy

pkgname=microsoft-edge-stable-bin
_pkgname=microsoft-edge
_pkgshortname=msedge
_channel=stable
pkgver=136.0.3240.92
pkgrel=1
pkgdesc="A browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier"
arch=('x86_64')
url="https://www.microsoftedgeinsider.com/en-us/download"
license=('custom')

provides=('microsoft-edge-stable' 'edge-stable')
conflicts=('microsoft-edge-stable' 'edge-stable' 'edge-stable-bin' 'edge')
depends=('gtk3' 'libcups' 'nss' 'alsa-lib' 'libxtst' 'libdrm' 'mesa')
optdepends=(
	'pipewire: WebRTC desktop sharing under Wayland'
	'kdialog: for file dialogs in KDE'
	'gnome-keyring: for storing passwords in GNOME keyring'
	'kwallet: for storing passwords in KWallet'
	)
options=(!strip !zipman)
source=("https://packages.microsoft.com/yumrepos/edge/Packages/m/${_pkgname}-stable-${pkgver}-1.x86_64.rpm"
	"microsoft-edge-stable.sh")
sha256sums=('322512d4ef620b9a7bd92987744b960f3f9be528f14118df39cf9d99c59694ea'
			'dc3765d2de6520b13f105b8001aa0e40291bc9457ac508160b23eea8811e26af')

package() {
	cp --parents -a {opt,usr} "$pkgdir"

	# suid sandbox
	chmod 4755 "${pkgdir}/opt/microsoft/${_pkgshortname}/msedge-sandbox"

	# install icons
	for res in 16 24 32 48 64 128 256; do
		install -Dm644 "${pkgdir}/opt/microsoft/${_pkgshortname}/product_logo_${res}.png" \
			"${pkgdir}/usr/share/icons/hicolor/${res}x${res}/apps/${_pkgname}.png"
	done

	# User flag aware launcher
	install -m755 microsoft-edge-stable.sh "${pkgdir}/usr/bin/microsoft-edge-stable"

	rm "${pkgdir}/opt/microsoft/${_pkgshortname}"/product_logo_*.png
}
