# Contributor: Mettacrawer <metta.crawler@gmail.com>
# Contributor: luizribeiro <luizribeiro@gmail.com>
# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>
# Maintainer:  graysky <therealgraysky AT protonmail DOT com>

pkgname=pi-hole-ftl
_pkgname=FTL
_servicename=pihole-FTL
pkgver=5.25.2
pkgrel=2
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
pkgdesc="The Pi-hole FTL engine"
url="https://github.com/pi-hole/FTL"
license=('EUPL-1.2')
depends=('nettle' 'gmp' 'libidn')
makedepends=('cmake' 'sqlite' 'xxd')
conflicts=('dnsmasq')
provides=('dnsmasq')
install=$pkgname.install
backup=('etc/pihole/pihole-FTL.conf' 'etc/pihole/dhcp.leases')
source=($pkgname-v$pkgver.tar.gz::"https://github.com/pi-hole/FTL/archive/v$pkgver.tar.gz"
        "https://raw.githubusercontent.com/max72bra/pi-hole-ftl-archlinux-customization/master/arch-ftl-$pkgver-$pkgrel.patch"
        "$pkgname.tmpfile"
        "$pkgname.sysuser"
        "$pkgname.service"
        "$pkgname.conf")
sha256sums=('d14523c623a4a79afe48b64f3953f73eb454c688edeeded9d95b169b275d354d'
            '66a3b62441397b2c6642d402e56edaf0692764567c44c211ed41125d388e3395'
            '538d2f66e30eabeeb0ac6794ac388b96ddf1830d9e988a0aaa810cb17c5c69fc'
            '39ef7bfd672ce59440bbf89e812992adc4d40091bc8d70fa24bd586381979064'
            '8ac9e414f3330a8c7f5d761a17c1a7a9b3c025c8927467222c3e5d6c57f784d8'
            'efb7f8195b7f8b87a4af20c66f5ae123d7b5bf97a5f0947de6dc60244545d074')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  patch -Np1 -i "$srcdir"/arch-ftl-$pkgver-$pkgrel.patch
}

build() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  ./build.sh
}

package() {
  cd "$srcdir"
  install -Dm775 "$_pkgname"-$pkgver/pihole-FTL "${pkgdir}"/usr/bin/pihole-FTL
  
  install -Dm644 "$pkgname.tmpfile" "$pkgdir"/usr/lib/tmpfiles.d/$pkgname.conf
  install -Dm644 "$pkgname.sysuser" "$pkgdir"/usr/lib/sysusers.d/$pkgname.conf

  install -dm775 "$pkgdir"/etc/pihole
  install -Dm644 "$pkgname.conf" "$pkgdir"/etc/pihole/pihole-FTL.conf
# install -Dm644 "$pkgname.db" "$pkgdir"/etc/pihole/pihole-FTL.db
  install -Dm664 /dev/null "$pkgdir"/etc/pihole/dhcp.leases

  install -Dm644 "$pkgname.service" "$pkgdir"/usr/lib/systemd/system/$_servicename.service
  install -dm755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants"
  ln -s ../$_servicename.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_servicename.service"
  
  install -dm755 "$pkgdir"/usr/share/licenses/pihole
  install -Dm644 "$_pkgname"-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/pihole/Pi-hole-FTL
  
  # ver. 5.0 dnamasq dropin support
  ln -s ./pihole-FTL "$pkgdir/usr/bin/dnsmasq"
}
