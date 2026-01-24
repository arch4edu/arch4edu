# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: haagch <christoph.haag@collabora.com>
pkgname=perfetto
pkgver=53.0
pkgrel=1
pkgdesc="Python APIs and bindings for Perfetto"
arch=(x86_64)
url="https://github.com/google/${pkgname}"
license=(Apache-2.0)
depends=(gcc-libs)
makedepends=(git python clang)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('2e8b3c2b5db7336732c288793f9d1be72df3f69152b3d13a62e130fe5d29640c8abcf6e93604a67af38d65d6bee5a40da364d2166ea8f3984e9d390aa422fe61')

build() {
  cd ${pkgname}-${pkgver}
  tools/install-build-deps
  tools/gn gen --args='is_debug=false' out/linux
  tools/ninja -C out/linux tracebox traced traced_probes perfetto
  tools/gen_amalgamated --output sdk/perfetto
}

package() {
  cd ${pkgname}-${pkgver}
  #DESTDIR="$pkgdir/" ninja -C out/linux install
  #install -d -m755 "$pkgdir"/usr/lib/
  install -D -m644 out/linux/libperfetto.so "$pkgdir"/usr/lib/libperfetto.so
  for i in perfetto tracebox traced; do
    install -D -m755 "out/linux/$i" "$pkgdir/usr/bin/$i"
  done

  install -d -D -m755 test/configs "$pkgdir"/usr/share/perfetto/configs
  install -D -m755 test/configs/* "$pkgdir"/usr/share/perfetto/configs

  install -d -D -m755 sdk "$pkgdir"/usr/share/perfetto/sdk
  install -D -m755 sdk/perfetto.* "$pkgdir"/usr/share/perfetto/sdk
}
