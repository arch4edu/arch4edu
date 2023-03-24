# Contributor: Discordian <therealdiscordian@gmail.com>

pkgname=ipfs-sync
pkgver=0.7.0
pkgrel=1
pkgdesc="A simple daemon which will watch files on your filesystem, mirror them to MFS, automatically update related pins, and update related IPNS keys."
url="https://github.com/TheDiscordian/ipfs-sync"
license=('custom' 'BSD')
arch=('any')
depends=('go-ipfs')
makedepends=('go')
source=(https://github.com/TheDiscordian/ipfs-sync/archive/v${pkgver}.tar.gz)
md5sums=('7962b6c318046ea886e1d8cfc7b1e9b8')
sha512sums=("2ae2db945ece0cd44bc781b9b6092c45f6e8c695dd9a00bffd15a20be83750259431b34f4541ecde4934a09190d84f5c5f629d57ced13ea359f35c28392519c6")

package() {
	cd ${pkgname}-${pkgver}/
	go build -o ipfs-sync -ldflags "-X main.version=v$pkgver"
	mkdir -p ${pkgdir}/usr/bin/
	install ./ipfs-sync ${pkgdir}/usr/bin/ipfs-sync
	mkdir -p ${pkgdir}/usr/lib/systemd/user
	install ./systemd/user/ipfs-sync.service ${pkgdir}/usr/lib/systemd/user/
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
