# Maintainer: BigmenPixel <bigmen dot pixel at tuta dot io>
# Contributor: rustemb <rustemb at systemli dot org>

pkgname=shadowsocks-rust
pkgver=1.15.3
pkgrel=4
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

sha512sums=('95ba0fd4f96166ccc3462dc67fa0dacf18559a849dc4cae60a0b4136e2a6a1e354ca28b359672b6b31bb13811eabf69cd9cdd46c4f5f9eb26b27b445dd1bbc3e'
            '90ee8735104795b5c50bc855ad11ee9c741fa1695409d72de7c69b89b0aa80c9596459edbb3a2c1d49e9414e3d06bc55328126c0062f1e28cac141ea202e455d'
            'ef5a348dfbbfd0bad733da217824dd55851aff3490c63685e9f1bc2b393998fea1bdad864c16a98b8af07264851bb0a11326959529a669008c5e62e94b26b209')

build() {
    [[ "$CARCH" == "riscv64" ]] && CARCH="riscv64gc"
    cd "${srcdir}/${pkgname}-${pkgver}"
    export CARGO_TARGET_DIR=target
    export RUSTUP_TOOLCHAIN=stable
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
