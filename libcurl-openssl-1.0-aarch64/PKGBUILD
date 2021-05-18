# $Id$
# Maintainer: Florian Maunier <fmaunier@gmail.com>
# Contributor: Michael Straube <straubem@gmx.de>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Piotr Balcerowski <piotr@balcerowski.org>

pkgname=libcurl-openssl-1.0
pkgver=7.76.1
pkgrel=1
pkgdesc="An URL retrieval library (without versioned symbols, built against openssl-1.0)"
arch=('aarch64' 'x86_64')
url="https://curl.haxx.se"
license=('MIT')
depends=('curl' 'glibc' 'krb5' 'libssh2' 'openssl-1.0' 'libpsl' 'zlib'
         'libssh2.so')
provides=('libcurl-openssl-1.0.so')
options=('strip')
source=("https://curl.haxx.se/download/curl-${pkgver}.tar.gz"{,.asc})
sha512sums=('43edacadbb823eb43008dd7d3b3851097cc40bc06ed6c701d7af2605a461ec556a9a15d1d71a8703cb2e0180aa3183995a67a072f4043ecc3a3972f25619722b'
            'SKIP')
validpgpkeys=('27EDEAF22F3ABCEB50DB9A125CC908FDB71E12C2') # Daniel Stenberg

build() {
  cd curl-${pkgver}

  export PKG_CONFIG_PATH=/usr/lib/openssl-1.0/pkgconfig

  ./configure \
    --prefix='/usr' \
    --disable-ldap \
    --disable-ldaps \
    --disable-manual \
    --disable-versioned-symbols \
    --enable-ipv6 \
    --enable-threaded-resolver \
    --with-gssapi \
    --with-libssh2 \
    --with-random='/dev/urandom' \
    --with-ca-bundle='/etc/ssl/certs/ca-certificates.crt'

  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make -C lib
}

package() {
  cd curl-${pkgver}

  make -C lib DESTDIR="${pkgdir}" install

  mv "${pkgdir}"/usr/lib/libcurl{,-openssl-1.0}.so.4.7.0
  rm "${pkgdir}"/usr/lib/libcurl.{a,so}*
  for version in 3 4 4.0.0 4.1.0 4.2.0 4.3.0 4.4.0 4.5.0 4.6.0; do
    ln -s libcurl-openssl-1.0.so.4.7.0 "${pkgdir}"/usr/lib/libcurl-openssl-1.0.so.${version}
  done

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s curl "${pkgdir}"/usr/share/licenses/${pkgname}
}

# vim: ts=2 sw=2 et:
