# Maintainer: Amin Vakil <info AT aminvakil DOT com>
# Contributor: xgdgsc <xgdgsc @t gmail dot com>
# Contributor: mynacol <dc07d át mynacol dót xyz>

pkgname=android-sdk-build-tools
#_ver=$(cat "${srcdir}/$_android/source.properties" |grep ^Pkg.Revision=|sed 's/Pkg.Revision=\([0-9.]*\).*/\1/')
_major=35
_minor=0
_micro=1
_ver=35.0.1
_displayversion=35
pkgver=r35.0.1
pkgrel=1
_sdk=android-sdk
_android=android-15

pkgdesc='Build-Tools for Google Android SDK (aapt, aidl, dexdump, dx, llvm-rs-cc)'
arch=('x86_64')
url="https://developer.android.com/studio/releases/build-tools"
license=('custom')
depends=('gcc-libs' 'zlib' 'bash')
optdepends=('lib32-gcc-libs' 'lib32-zlib' 'java-runtime')

source=("https://dl.google.com/android/repository/build-tools_r${_ver}_linux.zip"
        "package.xml")
sha512sums=('284a8a6ec4d99343aaab35c97dba82f8598924bfe95e143ea58eb58fec302cc77b868505531d2dbc73bc816acb5853d8de7f97d7dab9aecde53e8b280bd13be5'
            '501211771b02940010420a4003b8396d3d6599fb339c2f64959335ab1c3cf615811cc62acaa093c9f4e14bbc019a9e493835573a5136383617d8b5184509d3f8')
options=('!strip')

package() {
  cd "$pkgdir"

  install -d usr/share/licenses/$pkgname/
  ln -s /opt/$_sdk/build-tools/$_ver/NOTICE.txt usr/share/licenses/$pkgname/NOTICE.txt
  sed -i "s/@major@/$_major/g;s/@minor@/$_minor/g;s/@micro@/$_micro/g;s/@displayv@/$_displayversion/g;s/@pathv@/$_ver/g" "$srcdir/package.xml"
  install -Dm644 "${srcdir}/package.xml" opt/$_sdk/build-tools/$_ver/package.xml
  ln -s /opt/$_sdk/build-tools/$_ver/package.xml usr/share/licenses/$pkgname/package.xml

  target="opt/$_sdk/build-tools/$_ver"
  mkdir -p "$target"
  cp -r "$srcdir/$_android/"* "$target"
  chmod +Xr -R "$target"

  # Add symlinks to binaries to usr/bin/
  mkdir -p usr/bin/
  # lld is also provided by extra/lld, not creating symlink
  binaries=$(find "${target}" -maxdepth 1 -type f -executable -not -iname lld -printf "%f\n")
  for f in ${binaries[@]}
  do
    ln -s "/$target/$f" "usr/bin/$f"
  done
}
