# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Eric Cheng <ericcheng@hey.com>

pkgname=jellyfin-server-bin
pkgver=10.8.13
_pkgver="${pkgver}-1"
pkgrel=1
pkgdesc='Jellyfin server backend'
arch=('x86_64' 'aarch64' 'armv7h')
url='https://jellyfin.org/'
license=('GPL2')
provides=('jellyfin-server')
conflicts=('jellyfin-server' 'jellyfin-server-git')
depends=('aspnet-runtime-6.0' 'bash' 'sqlite' 'fontconfig' 'jellyfin-ffmpeg')
optdepends=('jellyfin-web: to run web-app on the same machine')
source=('jellyfin.conf'
        'jellyfin.service'
        'jellyfin.sysusers'
        'jellyfin.tmpfiles')
source_x86_64=("https://repo.jellyfin.org/releases/server/debian/stable/server/jellyfin-server_${_pkgver}_amd64.deb")
source_aarch64=("https://repo.jellyfin.org/releases/server/debian/stable/server/jellyfin-server_${_pkgver}_arm64.deb")
source_armv7h=("https://repo.jellyfin.org/releases/server/debian/stable/server/jellyfin-server_${_pkgver}_armhf.deb")
sha256sums=('dadc9a0bd154e6413ea87c645cc9e77e5a905d51d554b6cebfffe6c86aadd2a5'
            '0f8511673816daf528625366b6c27bc7e6182e4ac789191c87474667398376e2'
            '9bc1ddb77c73d46cc4078356b5773e5a776ebf8b47a1c820ad5fb17591ad5228'
            'b7faa4b0c756cdb361ef5b04fddfdc416b00f1246bb3a19a34bf4d185a6a7e5a')
sha256sums_x86_64=('d54decc098d5e61be50847edba8722d6468e22134bae2df514859e064eb8d727')
sha256sums_aarch64=('b9b917ec6ed4ddd3c728cb7be84245ff625c0a7ae12653a921cb3a9f6149252d')
sha256sums_armv7h=('ee4588aeeb55282b044d3bb4efef146a43abd742d3ef9327e042b2959008dc60')
backup=('etc/conf.d/jellyfin')
options=('staticlibs')

package() {
	tar -xf data.tar.xz

	cp -r "$srcdir"/usr "$pkgdir"/usr
	rm -r "$pkgdir"/usr/share
	
	install -Dm 644 jellyfin.service -t "$pkgdir"/usr/lib/systemd/system/
	install -Dm 644 jellyfin.sysusers "$pkgdir"/usr/lib/sysusers.d/jellyfin.conf
	install -Dm 644 jellyfin.tmpfiles "$pkgdir"/usr/lib/tmpfiles.d/jellyfin.conf
	install -Dm 644 jellyfin.conf "$pkgdir"/etc/conf.d/jellyfin
}
