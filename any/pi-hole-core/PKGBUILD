# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>
# Maintainer:  graysky <therealgraysky AT protonmail DOT com>
# Contributor: disprofarma <garmengol AT disprofarma DOT com DOT ar>

pkgname=pi-hole-core
_pkgname=pi-hole
pkgver=6.5
pkgrel=4
pkgdesc='The Pi-hole is an advertising-aware DNS/Web server. Arch adaptation for lan wide DNS server.'
arch=('any')
license=('EUPL-1.2')
url="https://github.com/pi-hole/pi-hole"
depends=('pi-hole-ftl>=6.0' 'netcat' 'logrotate' 'bind' 'sudo' 'lsof' 'inetutils' 'iproute2' 'procps-ng' 'jq' 'git')
makedepends=()
optdepends=()
conflicts=('pi-hole-standalone' 'pi-hole-server')
provides=('pi-hole-standalone' 'pi-hole-server')
install=$pkgname.install

source=($pkgname-$pkgver.tar.gz::https://github.com/$_pkgname/$_pkgname/archive/refs/tags/v$pkgver.tar.gz
        arch-core.patch
	    $_pkgname.tmpfile
	    $_pkgname-gravity.service
	    $_pkgname-gravity.timer
	    mimic_basic-install.sh
	    piholeDebug.sh
)
sha256sums=('277a1115b3b3b3ee0c115a6496710539709eefcd34fb5015480cd0bf2785b3f7'
            '6dd5182c1b744a76a93a4eb959e5faa15b8d68e825eae4ff8ad2a1e13deb52df'
            'd09f9d10ebdfb6db24d4e1abff8cd09519a7b3f3878ef3974c26aa6838f74e7e'
            'b8f93892c98f8e7cac4890dc510e38e0aa471387868a416fbb01f35576ab0c6f'
            '4cf95831215536bea184468d3dc7a43e88e86c550516b7d12381d37cf30adf9b'
            '27288535f7d5e18c73b9fe13aa0bcd78a2fd935cb2e978c70d51b0439c87844f'
            '69a71c29dbe42ef0cbd3655fd7ce5cf04e8a77e27a5b2c3a1fcce0b544223309')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  patch -Np1 -i "$srcdir"/arch-core.patch
}

package() {
  cd "$srcdir"
  install -Dm755 $_pkgname-$pkgver/pihole "$pkgdir"/usr/bin/pihole

  install -dm755 "$pkgdir"/opt/pihole
  install -Dm755 $_pkgname-$pkgver/gravity.sh "$pkgdir"/opt/pihole/gravity.sh

  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/api.sh "$pkgdir"/opt/pihole/api.sh
  install -Dm644 $_pkgname-$pkgver/advanced/Scripts/COL_TABLE "$pkgdir"/opt/pihole/COL_TABLE
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/list.sh "$pkgdir"/opt/pihole/list.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/piholeLogFlush.sh "$pkgdir"/opt/pihole/piholeLogFlush.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/query.sh "$pkgdir"/opt/pihole/query.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/updatecheck.sh "$pkgdir"/opt/pihole/updatecheck.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/utils.sh "$pkgdir"/opt/pihole/utils.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/version.sh "$pkgdir"/opt/pihole/version.sh

  install -Dm644 $_pkgname-$pkgver/advanced/Templates/gravity.db.sql "$pkgdir"/opt/pihole/gravity.db.sql
  install -Dm644 $_pkgname-$pkgver/advanced/Templates/gravity_copy.sql "$pkgdir"/opt/pihole/gravity_copy.sql

  install -Dm755 piholeDebug.sh "$pkgdir"/opt/pihole/piholeDebug.sh
  install -Dm755 mimic_basic-install.sh "$pkgdir"/opt/pihole/basic-install.sh

  cp -dpr --no-preserve=ownership $_pkgname-$pkgver/advanced/Scripts/database_migration "$pkgdir"/opt/pihole/

  install -Dm644 pi-hole.tmpfile "$pkgdir"/usr/lib/tmpfiles.d/pi-hole.conf

  install -Dm644 "$_pkgname-gravity.timer" "$pkgdir/usr/lib/systemd/system/$_pkgname-gravity.timer"
  install -Dm644 "$_pkgname-gravity.service" $pkgdir/usr/lib/systemd/system/$_pkgname-gravity.service
  install -dm755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants"
  ln -s ../$_pkgname-gravity.timer "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_pkgname-gravity.timer"

  install -dm755 "$pkgdir"/etc/pihole
  install -Dm644 $_pkgname-$pkgver/advanced/Templates/logrotate "$pkgdir"/etc/logrotate.d/pihole

  install -dm755 "$pkgdir"/usr/share/licenses/pihole
  install -Dm644 ${pkgname%-*}-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/pihole/Pi-hole
}
