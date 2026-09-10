# Maintainer: notfire <notfire@posteo.net>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Eric Cheng <ericcheng@hey.com>

pkgname=jellyfin-server-bin
pkgver=12.0
_pkgver="${pkgver}+deb12"
pkgrel=1
pkgdesc='Jellyfin server backend'
arch=('x86_64' 'aarch64')
url='https://jellyfin.org/'
license=('GPL2')
provides=('jellyfin-server')
conflicts=('jellyfin-server' 'jellyfin-server-git')
depends=('bash' 'sqlite' 'fontconfig' 'jellyfin-ffmpeg')
optdepends=('jellyfin-web: to run web-app on the same machine')
source=('jellyfin.conf'
        'jellyfin.service'
        'jellyfin.sysusers'
        'jellyfin.tmpfiles')
source_x86_64=("https://repo.jellyfin.org/files/server/debian/latest-stable/amd64/jellyfin-server_${_pkgver}_amd64.deb")
source_aarch64=("https://repo.jellyfin.org/files/server/debian/latest-stable/arm64/jellyfin-server_${_pkgver}_arm64.deb")
sha256sums=('d28c4219f2ab87ca7b7e9dd53710fb689d604baffd9acb3fef6b663d537944ec'
            '0f8511673816daf528625366b6c27bc7e6182e4ac789191c87474667398376e2'
            '9bc1ddb77c73d46cc4078356b5773e5a776ebf8b47a1c820ad5fb17591ad5228'
            'b7faa4b0c756cdb361ef5b04fddfdc416b00f1246bb3a19a34bf4d185a6a7e5a')
sha256sums_x86_64=('15d3a51dc2211ad6a9aa90dd2e6ff9083c6b38fc6882c255469895b098bb2e27')
sha256sums_aarch64=('fe14287ebfd3018c05b575020247de0600895f86d052424554d270f348047d95')
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
