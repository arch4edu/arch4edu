# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: haagch <christoph.haag@collabora.com>
pkgname=perfetto
pkgver=54.0
pkgrel=1
pkgdesc="Python APIs and bindings for Perfetto"
arch=(x86_64)
url="https://github.com/google/${pkgname}"
license=(Apache-2.0)
depends=(gcc-libs python-protobuf)
makedepends=(git python-setuptools clang)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('340a6fa56962e18a9039977914a3e448c83566a51fd970bffabf32b28c03c3a2d5c29104ce23a0b2a84f684678eb4471bf8beddbf323056bc64e3c1d7a729a5f')

build() {
  cd ${pkgname}-${pkgver}
  tools/install-build-deps
  tools/gn gen --args='is_debug=false' out/linux
  tools/ninja -C out/linux tracebox traced traced_probes perfetto
  tools/gen_amalgamated --output sdk/perfetto
  
  cd python
  python setup.py build
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

  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  cd python
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
}
