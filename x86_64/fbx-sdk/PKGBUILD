#!/bin/bash
# Maintainer : bartus <arch-user-repoᘓbartus.33mail.com>
#Contributor : Andrzej Giniewicz <gginiu@gmail.com>

pkgname='fbx-sdk'
pkgver=2020.1.1
pkgrel=1
pkgdesc='Platform and API toolkit to transfer existing content into the FBX format.'
arch=('i686' 'x86_64')
url='http://www.autodesk.com/products/fbx/overview'
depends=(gcc-libs)
makedepends=(patchelf)
license=('custom')
install='fbx-sdk.install'
source=("https://damassets.autodesk.net/content/dam/autodesk/www/adn/fbx/${pkgver//./-}/fbx${pkgver//./}_fbxsdk_linux.tar.gz")
sha256sums=('681065ce68f8acc07f30216ebc24e69814d852733efa9926c1b816e1309144c8')

build() {
  mkdir -p "${srcdir}/fbx-sdk"
  chmod +x "${srcdir}/fbx${pkgver//./}_fbxsdk_linux"
  printf "yes\nn\n" | "${srcdir}/fbx${pkgver//./}_fbxsdk_linux" "${srcdir}/fbx-sdk"
}

package() {
  cd "$srcdir/fbx-sdk"

  [ "$CARCH" = "x86_64" ] && fbxarch="x64" || fbxarch="x86"

  install -D "lib/gcc/$fbxarch/release/libfbxsdk.so" "$pkgdir/usr/lib/libfbxsdk.so"

  cp -r include "$pkgdir/usr"

  install -d "$pkgdir/usr/share/doc/$pkgname"
  cp -r samples "$pkgdir/usr/share/doc/$pkgname"
  install -D "FBX_SDK_Online_Documentation.html" "$pkgdir/usr/share/doc/$pkgname/FBX_SDK_Online_Documentation.html"
  install -D "License.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # fix 600 mode
  find "$pkgdir"/usr/{include,share} -type f -exec chmod 644 {} \+
  find "$pkgdir"/usr/{include,share} -type d -exec chmod 755 {} \+

  # strip rpath
  patchelf --remove-rpath "$pkgdir"/usr/lib/libfbxsdk.so
}

