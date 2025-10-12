# Maintainer: <hurricanepootis@protonmail.com>
# Contributor: bartus <arch-user-repoᘓbartus.33mail.com>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>
# Contributor: Gr3q <floyd0122@gmail.com>
# Contributor: Rainbowu <wurongbo2012@hotmail.com>
pkgname=('fbx-sdk' 'fbx-sdk-docs')
pkgbase='fbx-sdk'
pkgver=2020.3.7
pkgrel=2
pkgdesc='Platform and API toolkit to transfer existing content into the FBX format.'
arch=('x86_64')
url='http://www.autodesk.com/products/fbx/overview'
depends=(gcc-libs libxml2-legacy zlib glibc)
makedepends=(rsync)
license=('LicenseRef-Autodesk-FBX-SDK-2020-License')
install='fbx-sdk.install'
source=("https://damassets.autodesk.net/content/dam/autodesk/www/files/fbx${pkgver//.}_fbxsdk_gcc_linux.tar.gz")
sha256sums=('191c6b0a549f1e70154a04705ddbf52232d049a6e5ae17801a2bc2bf60b84e0b')

build() {
  mkdir -p "${srcdir}/fbx-sdk"
  chmod 755 "${srcdir}/fbx${pkgver//./}_fbxsdk_linux"
  printf "yes\nn\n" | "${srcdir}/fbx${pkgver//./}_fbxsdk_linux" "${srcdir}/fbx-sdk"

  # fix typo in sdk file, replace mLefttChild with mLeftChild
  sed -i 's/mLefttChild/mLeftChild/g' "${srcdir}/fbx-sdk/include/fbxsdk/core/base/fbxredblacktree.h"
}

package_fbx-sdk() {
  cd "$srcdir/fbx-sdk"
  optdepends=('fbx-sdk-docs: Documentation')

  install -Dm644 "lib/release/libfbxsdk.so" "$pkgdir/usr/lib/libfbxsdk.so"

  rsync -a -r include "$pkgdir/usr"
  chmod 755 "$pkgdir/usr/include"

  install -D "License.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # strip rpath
  #patchelf --remove-rpath "$pkgdir"/usr/lib/libfbxsdk.so
}

package_fbx-sdk-docs() {
  cd "$srcdir/fbx-sdk"
  depends=()
  install -dm755 "$pkgdir/usr/share/doc/${pkgname::7}"
  install -Dm644 License.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  rsync -a -r samples "$pkgdir/usr/share/doc/${pkgname::7}"
  install -D "FBX_SDK_Online_Documentation.html" \
  "$pkgdir/usr/share/doc/${pkgname::7}/FBX_SDK_Online_Documentation.html"

  cd "$pkgdir/usr/share/doc/${pkgname::7}"
  find -type f -exec chmod 644 {} \;
  find -type d -exec chmod 755 {} \;
}
