# $Id$
# Maintainer: Florian Maunier <fmaunier@gmail.com>
# Contributor: Michael Straube <straubem@gmx.de>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Piotr Balcerowski <piotr@balcerowski.org>

pkgname=libcurl-openssl-1.0
pkgver=7.75.0
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
sha512sums=('ebef01be48e05f46f7d0605966d4c66391d5a51f6d102265647522f8f5df61b5440c930bd1b043d56968769869275123122826a9ec7fb3148c72a28ee32ce696'
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
