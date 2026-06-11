# Contributor: Mettacrawer <metta.crawler@gmail.com>
# Contributor: luizribeiro <luizribeiro@gmail.com>
# Contributor: max.bra <max dot bra dot gtalk at gmail dot com>
# Contributor: graysky <therealgraysky AT protonmail DOT com>
# Maintainer: Piotr Zarycki <piotr.zarycki@gmail.com>

pkgname=pi-hole-ftl
_pkgname=FTL
_servicename=pihole-FTL
pkgver=6.6.2
pkgrel=3
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
pkgdesc="The Pi-hole FTL engine"
url="https://github.com/pi-hole/FTL"
license=('EUPL-1.2')
depends=('nettle' 'gmp' 'mbedtls' 'pi-hole-web')
makedepends=('cmake' 'xxd')
conflicts=('dnsmasq')
provides=('dnsmasq')
install=$pkgname.install
backup=('etc/pihole/pihole-FTL.conf' 'etc/pihole/dhcp.leases')
source=($pkgname-v$pkgver.tar.gz::"https://github.com/pi-hole/FTL/archive/v$pkgver.tar.gz"
        "$pkgname.tmpfile"
        "$pkgname.sysuser"
        "$pkgname.service"
        "nettle4_base64_decode_update.patch")
sha256sums=('5827e6bfd7ff4a8ed8cd1e475f9bee66061533375ea5061ba1946c73992de082'
            '0feb4597a4afd9054553505d305b0feb7e1f6e1705b092561648ff37d0a2893c'
            'dd1d2a341e774d4e549373ae75604031b9af0ee44debcd71a89259d9110d2a77'
            '0998da040d038ddbad129ba8e1ea74741bc912813407b579cab1b3b3f206e721'
            '998cb258704aeecd9a73aa566673b451be72c73be327987b14e0ffa7c9570dc6')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  # Fix nettle 4.0 API change: base64_decode_update dst_length is now also an input
  patch -Np1 -i "$srcdir"/nettle4_base64_decode_update.patch
  # Fix strstr redefined warning treated as error (GCC 14+)
  sed -i '/#define memmove/a #undef strstr' src/FTL.h
  # Fix const qualifier warnings in webserver.c (GCC 14+)
  sed -i 's/\bchar \*pos = strchr(host,/const char *pos = strchr(host,/g' src/webserver/webserver.c
  sed -i 's/\bchar \*equal_sign = strchr(opt,/const char *equal_sign = strchr(opt,/g' src/webserver/webserver.c
  # Fix mbedtls 3.x API changes
  sed -i 's/mbedtls_x509write_crt_pem(\([^,]*\), \([^,]*\), sizeof(\([^)]*\)))/mbedtls_x509write_crt_pem(\1, \2, sizeof(\3), NULL, NULL)/g' src/webserver/x509.c
  sed -i 's/mbedtls_pk_parse_keyfile(\([^,]*\), \([^,]*\), NULL);/mbedtls_pk_parse_keyfile(\1, \2, NULL, NULL, NULL);/g' src/webserver/x509.c
  # Fix nettle 4.0 API change: digest functions no longer take a length argument
  find src -name '*.[ch]' -print0 | \
    xargs -0 sed -i 's/\(hmac_sha[0-9]*_digest\|sha[0-9]*_digest\)(\([^,]*\), [A-Z0-9_]*DIGEST_SIZE, \([^)]*\))/\1(\2, \3)/g'
  sed -i 's/hash->digest(ctx, hash->digest_size, digest)/hash->digest(ctx, digest)/g' src/dnsmasq/dnssec.c
}

build() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  STATIC=false ./build.sh
}

package() {
  cd "$srcdir"
  install -Dm775 "$_pkgname"-$pkgver/pihole-FTL "${pkgdir}"/usr/bin/pihole-FTL

  install -Dm644 "$pkgname.tmpfile" "$pkgdir"/usr/lib/tmpfiles.d/$pkgname.conf
  install -Dm644 "$pkgname.sysuser" "$pkgdir"/usr/lib/sysusers.d/$pkgname.conf

  install -dm755 "$pkgdir"/etc/pihole
  install -Dm664 /dev/null "$pkgdir"/etc/pihole/dhcp.leases

  install -Dm644 "$pkgname.service" "$pkgdir"/usr/lib/systemd/system/$_servicename.service
  install -dm755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants"
  ln -s ../$_servicename.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_servicename.service"

  install -dm755 "$pkgdir"/usr/share/licenses/pihole
  install -Dm644 "$_pkgname"-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/pihole/Pi-hole-FTL

  # ver. 5.0+ dnamasq dropin support
  ln -s ./pihole-FTL "$pkgdir/usr/bin/dnsmasq"
}
