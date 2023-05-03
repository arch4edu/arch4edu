# Maintainer: Christian Heusel <christian@heusel.eu>
# Contributor: Knut Ahlers <knut at ahlers dot me>
# Contributor: Det <nimetonmaili g-mail>
# Contributor: t3ddy, Lex Rivera aka x-demon, ruario

# Check for new Linux releases in: http://googlechromereleases.blogspot.com/search/label/Stable%20updates
# or use: $ curl -s https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz | gzip -df | xq -x "otherdata/package[@name='google-chrome-$_channel']/version/@ver"

pkgname=google-chrome
pkgver=113.0.5672.63
pkgrel=1
pkgdesc="The popular and trusted web browser by Google (Stable Channel)"
arch=('x86_64')
url="https://www.google.com/chrome"
license=('custom:chrome')
depends=(
	'alsa-lib'
	'gtk3'
	'libcups'
	'libxss'
	'libxtst'
	'nss'
	'ttf-liberation'
	'xdg-utils'
)
optdepends=(
	'pipewire: WebRTC desktop sharing under Wayland'
	'kdialog: for file dialogs in KDE'
	'gnome-keyring: for storing passwords in GNOME keyring'
	'kwallet: for storing passwords in KWallet'
)
options=('!emptydirs' '!strip')
install=$pkgname.install
_channel=stable
source=("https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-${_channel}/google-chrome-${_channel}_${pkgver}-1_amd64.deb"
	'eula_text.html'
	"google-chrome-$_channel.sh")
sha512sums=('6904d1273b1843322299b505a20f4cd1e8884d1a804c93dc5d88d4bf31a165e16a809b43f1ebc814c4e249c87c6befd86fc0e54a6ef00b2a715f75db94593b61'
            'a225555c06b7c32f9f2657004558e3f996c981481dbb0d3cd79b1d59fa3f05d591af88399422d3ab29d9446c103e98d567aeafe061d9550817ab6e7eb0498396'
            '43519ec81d008c9f949ef52b98a718473913e888d99ff6598083e30cd1f07376b5e58a7639fd309ee19056c18eac58cbf6a31bec6bfd2509ebce9fa9d6919743')

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"

	# Launcher
	install -m755 google-chrome-$_channel.sh "$pkgdir"/usr/bin/google-chrome-$_channel

	# Icons
	for i in 16x16 24x24 32x32 48x48 64x64 128x128 256x256; do
		install -Dm644 "$pkgdir"/opt/google/chrome/product_logo_${i/x*/}.png \
			"$pkgdir"/usr/share/icons/hicolor/$i/apps/google-chrome.png
	done

	# License
	install -Dm644 eula_text.html "$pkgdir"/usr/share/licenses/google-chrome/eula_text.html
	install -Dm644 "$pkgdir"/opt/google/chrome/WidevineCdm/LICENSE \
		"$pkgdir"/usr/share/licenses/google-chrome-$_channel/WidevineCdm-LICENSE.txt

	# Fix the Chrome desktop entry
	sed -i \
		-e "/Exec=/i\StartupWMClass=Google-chrome" \
		-e "s/x-scheme-handler\/ftp;\?//g" \
		"$pkgdir"/usr/share/applications/google-chrome.desktop

	# Remove the Debian Cron job, duplicate product logos and menu directory
	rm -r \
		"$pkgdir"/etc/cron.daily/ \
		"$pkgdir"/opt/google/chrome/cron/ \
		"$pkgdir"/opt/google/chrome/product_logo_*.{png,xpm} \
		"$pkgdir"/usr/share/menu/
}
