# Maintainer: BigmenPixel <bigmen dot pixel at tuta dot io>
# Contributor: rustemb <rustemb at systemli dot org>

pkgname=shadowsocks-rust
pkgver=1.15.1
pkgrel=1
pkgdesc='A Rust port of shadowsocks https://shadowsocks.org/'
arch=(x86_64)
url='https://github.com/shadowsocks/shadowsocks-rust'
license=('MIT')
makedepends=('cargo')
options=('!lto')
source=(
    "${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
    'shadowsocks-rust@.service'
    'shadowsocks-rust-server@.service')

sha512sums=('e3ae3d728dacd40325d5802ed9b730b759b8007206e9e324df899c6837d4a0d3b95acbdda45242f4ad03e62d889b1d194e270951c46ba2be4ebefc54a55f10e7'
            '3a79d6958e61e891d208cea17b02ed5fe0318bbecc8d1bda7b8297e6ffdad186a86cf0fc55cb2904ed67bd460856f7136b6550ab493de31435df97285279d47d'
            '23a33b6e43ac5e91866c0aab8b0166790559ebdb49b3ea91393a977d2636a0c75f99544f559e0a248be1eb54e6bf8ad1cda8887a85d773a9214de16c4f223f1f')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    export CARGO_TARGET_DIR=target
    cargo fetch --locked --target "${CARCH}-unknown-linux-gnu"
    cargo build --frozen --release --features local-redir,local-tun,local-dns,local-http-native-tls
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 "target/release/sslocal" "${pkgdir}/usr/bin/sslocal"
    install -Dm755 "target/release/ssserver" "${pkgdir}/usr/bin/ssserver"
    install -Dm755 "target/release/ssurl" "${pkgdir}/usr/bin/ssurl"
    install -Dm755 "target/release/ssmanager" "${pkgdir}/usr/bin/ssmanager"
    install -Dm755 "target/release/ssservice" "${pkgdir}/usr/bin/ssservice"
    install -Dm644 "${srcdir}/${pkgname}@.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}@.service"
    install -Dm644 "${srcdir}/${pkgname}-server@.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}-server@.service"
    install -Dm644 "examples/config_ext.json" "${pkgdir}/etc/${pkgname}/config_ext_rust.json.example"
    install -Dm644 "examples/config.json" "${pkgdir}/etc/${pkgname}/config_rust.json.example"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
