# Contributor: Mettacrawer <metta.crawler@gmail.com>
# Contributor: luizribeiro <luizribeiro@gmail.com>
# Contributor: max.bra <max dot bra dot gtalk at gmail dot com>
# Contributor: graysky <therealgraysky AT protonmail DOT com>
# Maintainer: Piotr Zarycki <piotr.zarycki@gmail.com>

pkgname=pi-hole-ftl
_pkgname=FTL
_servicename=pihole-FTL
pkgver=6.7
pkgrel=1

# Upstream release metadata, used to stamp the version into the binary.
# Update both with every version bump.
_commit='fa65a88f8cdef1013594d4de14108077954faea4'
_commit_date='2026-07-06 21:07:11 +0100'

arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
pkgdesc="The Pi-hole FTL engine"
url="https://github.com/pi-hole/FTL"
license=('EUPL-1.2')
# mbedtls3: Arch's mbedtls 4.x is built without MBEDTLS_THREADING_C, which
# civetweb's mod_mbedtls.inl requires (#error otherwise).
depends=('nettle' 'gmp' 'mbedtls3' 'libidn2' 'dbus' 'pi-hole-web')
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
sha256sums=('12100ef39800917a298f1cfc45c40df6b6a415953a5a47f62a94d24894443cde'
            '0feb4597a4afd9054553505d305b0feb7e1f6e1705b092561648ff37d0a2893c'
            'dd1d2a341e774d4e549373ae75604031b9af0ee44debcd71a89259d9110d2a77'
            '0998da040d038ddbad129ba8e1ea74741bc912813407b579cab1b3b3f206e721'
            '998cb258704aeecd9a73aa566673b451be72c73be327987b14e0ffa7c9570dc6')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  # Fix nettle 4.0 API change: base64_decode_update dst_length is now also an input
  patch -Np1 -i "$srcdir"/nettle4_base64_decode_update.patch
  # GCC 16: sanitize_dns_hosts() increments this counter but never reads it.
  # Scoped to that function only - the other validator loops do use their i.
  sed -i '/^void sanitize_dns_hosts(/,/^}/ s/int i = 0;/int i __attribute__((unused)) = 0;/' src/config/validator.c
  # x509.c targets the mbedtls 2.x API; mbedtls3 needs the extra RNG arguments
  sed -i 's/mbedtls_x509write_crt_pem(\([^,]*\), \([^,]*\), sizeof(\([^)]*\)))/mbedtls_x509write_crt_pem(\1, \2, sizeof(\3), NULL, NULL)/g' src/webserver/x509.c
  sed -i 's/mbedtls_pk_parse_keyfile(\([^,]*\), \([^,]*\), NULL);/mbedtls_pk_parse_keyfile(\1, \2, NULL, NULL, NULL);/g' src/webserver/x509.c
}

build() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"

  # mbedtls3 lives in a parallel include tree. -isystem keeps FTL's -Werror
  # from turning warnings inside the mbedTLS headers into build failures.
  CFLAGS+=" -isystem /usr/include/mbedtls3"

  # GitHub release tarballs ship no .git directory, so gen_version.cmake's
  # fallback runs git in $srcdir and can pick up the AUR checkout above it
  # (producing e.g. vDev-f2a924d). These overrides are supported upstream.
  export GIT_BRANCH='master'
  export GIT_HASH="${_commit:0:8}"
  export GIT_VERSION="v$pkgver"
  export GIT_DATE="$_commit_date"
  export GIT_TAG="v$pkgver"

  STATIC=false ./build.sh \
    "-DLIBMBEDTLS=/usr/lib/mbedtls3/libmbedtls.so \
     -DLIBMBEDX509=/usr/lib/mbedtls3/libmbedx509.so \
     -DLIBMBEDCRYPTO=/usr/lib/mbedtls3/libmbedcrypto.so"
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
