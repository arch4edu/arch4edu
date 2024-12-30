# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>

pkgname=pi-hole-standalone
_pkgname=pi-hole
pkgver=5.18.4
pkgrel=1
pkgdesc='The Pi-hole is an advertising-aware DNS/Web server. Arch alteration for standalone PC.'
arch=('any')
license=('EUPL-1.2')
url="https://github.com/pi-hole/pi-hole"
depends=('pi-hole-ftl' 'netcat' 'inetutils' 'iproute2' 'bind-tools' 'sudo' 'lsof' 'procps-ng')
makedepends=('git')
conflicts=('pi-hole-server')
install=$pkgname.install
backup=()

source=($pkgname-core-$pkgver.tar.gz::https://github.com/$_pkgname/$_pkgname/archive/v$pkgver.tar.gz
		"https://raw.githubusercontent.com/max72bra/pi-hole-standalone-archlinux-customization/master/arch-server-core-$pkgver-$pkgrel.patch"
	01-pihole.conf
	$_pkgname.tmpfile
	$_pkgname-gravity.service
	$_pkgname-gravity.timer
	$_pkgname-logtruncate.service
	$_pkgname-logtruncate.timer
	mimic_setupVars.conf.sh
	mimic_basic-install.sh
	piholeDebug.sh)

sha256sums=('723ed042ae3703eaef8bc0e52ab6ab8d2062684af96c4e4ca09ddc513505df1f'
            'ff474a9a17956685b1dd32da25d86a033dac7541c2f03573356a85b7a9ee3f01'
            '4e92687a1c34bcc7f5aaf76ab3cdff73228d2acafefd99c7aad89046c570136a'
            '6da6bba6cfac4e87a1f1e8e1488b71858ac6feb0a2e327470a58d8f1e9ad8cbf'
            '9b72d7769036f8f4bb7121968d2ae4bdba427e4b16787ce340205a5f62b45c7c'
            '5228b4f923eab7784952a0fd6da895e7bff2f80a7f91c4a7c6350491dfdbb2e8'
            '88e3c78bbeaf5dc1100df65202ded8207877954a96bdf1b0ab3d9990d9fa759f'
            'ff507ce58c9492cce57e947696e1b814469fc2d856a1e303c6e68f98c62ebf46'
            '851dc423a08e289163bdd3c05675513ab3deff5dbe8dfcbd523cc3fac11f939d'
            '85fe4178b12445767c7ab090cfad70d8faed9d5a28218e9425d27c2d42d6e106'
            '73a8362f7a3eac91c77efbbcb4910ff079203bb5f829e32ecf3391d017117bb8')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  patch -Np1 -i "$srcdir"/arch-server-core-$pkgver-$pkgrel.patch
}

package() {
  cd "$srcdir"
  install -Dm755 $_pkgname-$pkgver/pihole "$pkgdir"/usr/bin/pihole

  install -dm755 "$pkgdir"/opt/pihole
  install -Dm755 $_pkgname-$pkgver/gravity.sh "$pkgdir"/opt/pihole/gravity.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/version.sh "$pkgdir"/opt/pihole/version.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/updatecheck.sh "$pkgdir"/opt/pihole/updatecheck.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/piholeLogFlush.sh "$pkgdir"/opt/pihole/piholeLogFlush.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/chronometer.sh "$pkgdir"/opt/pihole/chronometer.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/list.sh "$pkgdir"/opt/pihole/list.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/utils.sh "$pkgdir"/opt/pihole/utils.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/webpage.sh "$pkgdir"/opt/pihole/webpage.sh
# install -Dm755 $_pkgname-$pkgver/advanced/Scripts/wildcard_regex_converter.sh "$pkgdir"/opt/pihole/wildcard_regex_converter.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/query.sh "$pkgdir"/opt/pihole/query.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/pihole-reenable.sh "$pkgdir"/opt/pihole/pihole-reenable.sh
  install -Dm755 $_pkgname-$pkgver/advanced/Scripts/piholeARPTable.sh "$pkgdir"/opt/pihole/piholeARPTable.sh

  install -Dm644 $_pkgname-$pkgver/advanced/Scripts/COL_TABLE "$pkgdir"/opt/pihole/COL_TABLE

  install -Dm644 $_pkgname-$pkgver/advanced/Templates/gravity.db.sql "$pkgdir"/opt/pihole/gravity.db.sql
  install -Dm644 $_pkgname-$pkgver/advanced/Templates/gravity_copy.sql "$pkgdir"/opt/pihole/gravity_copy.sql

  install -Dm755 piholeDebug.sh "$pkgdir"/opt/pihole/piholeDebug.sh
  install -Dm755 mimic_setupVars.conf.sh "$pkgdir"/opt/pihole/mimic_setupVars.conf.sh
  install -Dm755 mimic_basic-install.sh "$pkgdir"/opt/pihole/basic-install.sh

  cp -dpr --no-preserve=ownership $_pkgname-$pkgver/advanced/Scripts/database_migration "$pkgdir"/opt/pihole/

  install -Dm644 $_pkgname-$pkgver/advanced/dnsmasq.conf.original "$pkgdir"/etc/dnsmasq.conf
  install -Dm644 01-pihole.conf "$pkgdir"/etc/dnsmasq.d/01-pihole.conf
  install -Dm644 $_pkgname-$pkgver/advanced/06-rfc6761.conf "$pkgdir"/etc/dnsmasq.d/06-rfc6761.conf

  install -Dm644 pi-hole.tmpfile "$pkgdir"/usr/lib/tmpfiles.d/pi-hole.conf

  install -Dm644 "$_pkgname-gravity.timer" "$pkgdir/usr/lib/systemd/system/$_pkgname-gravity.timer"
  install -Dm644 "$_pkgname-gravity.service" $pkgdir/usr/lib/systemd/system/$_pkgname-gravity.service
  install -Dm644 "$_pkgname-logtruncate.timer" "$pkgdir/usr/lib/systemd/system/$_pkgname-logtruncate.timer"
  install -Dm644 "$_pkgname-logtruncate.service" $pkgdir/usr/lib/systemd/system/$_pkgname-logtruncate.service
  install -dm755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants"
  ln -s ../$_pkgname-gravity.timer "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_pkgname-gravity.timer"
  ln -s ../$_pkgname-logtruncate.timer "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_pkgname-logtruncate.timer"

  install -dm775 "$pkgdir"/etc/pihole
  install -dm755 "$pkgdir"/usr/share/pihole/configs
  install -Dm644 $_pkgname-$pkgver/adlists.list "$pkgdir"/etc/pihole/adlists.list

  install -dm755 "$pkgdir"/usr/share/licenses/pihole
  install -Dm644 ${pkgname%-*}-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/pihole/Pi-hole
}
