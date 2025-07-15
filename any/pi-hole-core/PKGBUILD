# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>
# Maintainer:  graysky <therealgraysky AT protonmail DOT com>
# Contributor: disprofarma <garmengol AT disprofarma DOT com DOT ar>

pkgname=pi-hole-core
_pkgname=pi-hole
pkgver=6.1.4
pkgrel=1
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
backup=(''etc/pihole/adlists.list'' 'etc/sudoers.d/pihole')

source=($pkgname-$pkgver.tar.gz::https://github.com/$_pkgname/$_pkgname/archive/refs/tags/v$pkgver.tar.gz
      "https://raw.githubusercontent.com/max72bra/pi-hole-core-archlinux-customization/main/arch-core-$pkgver-$pkgrel.patch"
	    $_pkgname.tmpfile
	    $_pkgname-gravity.service
	    $_pkgname-gravity.timer
	    $_pkgname-logtruncate.service
	    $_pkgname-logtruncate.timer
	    mimic_setupVars.conf.sh
	    mimic_basic-install.sh
	    piholeDebug.sh
)

sha256sums=('acdfbc35494d28fe9060a35fbd01120563accee15e6302b89c8f7ec80a918213'
            '6539cc9063b82336547e458de0585b8c5951cad5fdd7da242dea6d6c83846e91'
            'd09f9d10ebdfb6db24d4e1abff8cd09519a7b3f3878ef3974c26aa6838f74e7e'
            '9b72d7769036f8f4bb7121968d2ae4bdba427e4b16787ce340205a5f62b45c7c'
            '5228b4f923eab7784952a0fd6da895e7bff2f80a7f91c4a7c6350491dfdbb2e8'
            '88e3c78bbeaf5dc1100df65202ded8207877954a96bdf1b0ab3d9990d9fa759f'
            'ff507ce58c9492cce57e947696e1b814469fc2d856a1e303c6e68f98c62ebf46'
            'd3bc841ce7f21b5a597dc47cdae23faeba64cb0bbb8c897d9daf1a2bc4fe0821'
            '27288535f7d5e18c73b9fe13aa0bcd78a2fd935cb2e978c70d51b0439c87844f'
            '69a71c29dbe42ef0cbd3655fd7ce5cf04e8a77e27a5b2c3a1fcce0b544223309')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  patch -Np1 -i "$srcdir"/arch-core-$pkgver-$pkgrel.patch
}

package() {
  cd "$srcdir"
  install -Dm755 $_pkgname-$pkgver/pihole "$pkgdir"/usr/bin/pihole

  install -dm755 "$pkgdir"/opt/pihole
  install -Dm755 $_pkgname-$pkgver/gravity.sh "$pkgdir"/opt/pihole/gravity.sh

  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/api.sh "$pkgdir"/opt/pihole/api.sh
  install -Dm644 $_pkgname-$pkgver/advanced/Scripts/COL_TABLE "$pkgdir"/opt/pihole/COL_TABLE
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/list.sh "$pkgdir"/opt/pihole/list.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/piholeARPTable.sh "$pkgdir"/opt/pihole/piholeARPTable.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/piholeLogFlush.sh "$pkgdir"/opt/pihole/piholeLogFlush.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/query.sh "$pkgdir"/opt/pihole/query.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/updatecheck.sh "$pkgdir"/opt/pihole/updatecheck.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/utils.sh "$pkgdir"/opt/pihole/utils.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/version.sh "$pkgdir"/opt/pihole/version.sh

  install -Dm644 $_pkgname-$pkgver/advanced/Templates/gravity.db.sql "$pkgdir"/opt/pihole/gravity.db.sql
  install -Dm644 $_pkgname-$pkgver/advanced/Templates/gravity_copy.sql "$pkgdir"/opt/pihole/gravity_copy.sql

  install -Dm755 piholeDebug.sh "$pkgdir"/opt/pihole/piholeDebug.sh
  install -Dm755 mimic_setupVars.conf.sh "$pkgdir"/opt/pihole/mimic_setupVars.conf.sh
  install -Dm755 mimic_basic-install.sh "$pkgdir"/opt/pihole/basic-install.sh

  cp -dpr --no-preserve=ownership $_pkgname-$pkgver/advanced/Scripts/database_migration "$pkgdir"/opt/pihole/

  install -dm750 "$pkgdir"/etc/sudoers.d
  install -Dm440 $_pkgname-$pkgver/advanced/Templates/pihole.sudo "$pkgdir"/etc/sudoers.d/pihole

  install -Dm644 pi-hole.tmpfile "$pkgdir"/usr/lib/tmpfiles.d/pi-hole.conf

  install -Dm644 "$_pkgname-gravity.timer" "$pkgdir/usr/lib/systemd/system/$_pkgname-gravity.timer"
  install -Dm644 "$_pkgname-gravity.service" $pkgdir/usr/lib/systemd/system/$_pkgname-gravity.service
  install -Dm644 "$_pkgname-logtruncate.timer" "$pkgdir/usr/lib/systemd/system/$_pkgname-logtruncate.timer"
  install -Dm644 "$_pkgname-logtruncate.service" $pkgdir/usr/lib/systemd/system/$_pkgname-logtruncate.service
  install -dm755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants"
  ln -s ../$_pkgname-gravity.timer "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_pkgname-gravity.timer"
  ln -s ../$_pkgname-logtruncate.timer "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_pkgname-logtruncate.timer"

  install -dm755 "$pkgdir"/etc/pihole
  install -Dm644 $_pkgname-$pkgver/advanced/Templates/logrotate "$pkgdir"/etc/pihole/logrotate
  install -Dm644 $_pkgname-$pkgver/adlists.list "$pkgdir"/etc/pihole/adlists.list

  install -dm755 "$pkgdir"/usr/share/licenses/pihole
  install -Dm644 ${pkgname%-*}-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/pihole/Pi-hole
}
