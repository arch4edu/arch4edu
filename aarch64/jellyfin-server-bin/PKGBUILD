# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Eric Cheng <ericcheng@hey.com>

pkgname=jellyfin-server-bin
pkgver=10.9.7
_pkgver="${pkgver}+deb12"
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
source_x86_64=("https://repo.jellyfin.org/files/server/debian/latest-stable/amd64/jellyfin-server_${_pkgver}_amd64.deb")
source_aarch64=("https://repo.jellyfin.org/files/server/debian/latest-stable/arm64/jellyfin-server_${_pkgver}_arm64.deb")
source_armv7h=("https://repo.jellyfin.org/files/server/debian/latest-stable/armhf/jellyfin-server_${_pkgver}_armhf.deb")
sha256sums=('d28c4219f2ab87ca7b7e9dd53710fb689d604baffd9acb3fef6b663d537944ec'
            '0f8511673816daf528625366b6c27bc7e6182e4ac789191c87474667398376e2'
            '9bc1ddb77c73d46cc4078356b5773e5a776ebf8b47a1c820ad5fb17591ad5228'
            'b7faa4b0c756cdb361ef5b04fddfdc416b00f1246bb3a19a34bf4d185a6a7e5a')
sha256sums_x86_64=('fcd2486ce67ab6eba639e06865cc17945a785b698f34e0e9b102807413d727c1')
sha256sums_aarch64=('f096803d494fe6b60faeb787a11a6e4a3576c13eee46db393f40767d156d0568')
sha256sums_armv7h=('c5f0cd1a685c31276204b85bda20f6739945f3c4c27212ef116fd91364a3afef')
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
