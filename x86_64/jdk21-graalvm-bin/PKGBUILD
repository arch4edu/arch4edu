# Maintainer: Yakov Till <yakov.till@gmail.com>
# Contributor: Lucas Werkmeister <mail@lucaswerkmeister.de>
# Contributor: <asamk(at)gmx.de>

pkgver=21.0.2
_java=${pkgver%%.*}
pkgname="jdk${_java}-graalvm-bin"
pkgrel=2
pkgdesc="Universal virtual machine for running applications written in a variety of languages (JVM-based, LLVM-based, or other), Java ${_java} version"
arch=('x86_64'
      'aarch64')
url='https://www.graalvm.org/'
license=('GPL-2.0-only WITH Classpath-exception-2.0')
depends=('java-runtime-common'
         'java-environment-common'
         'alsa-lib'
         'freetype2'
         'libx11'
         'libxext'
         'libxi'
         'libxrender'
         'libxtst')
makedepends=()
provides=("java-runtime=${_java}"
          "java-environment=${_java}")
replaces=("native-image-jdk${_java}-bin")
options=('staticlibs' '!debug')
install="$pkgname.install"
source=('graalvm-rebuild-libpolyglot.hook')
sha256sums=('eae72b5a2a2826eed7e4be5710d33f82934622a390ab6a9f009ed7753359e02e')
sha256sums_x86_64=('b048069aaa3a99b84f5b957b162cc181a32a4330cbc35402766363c5be76ae48')
sha256sums_aarch64=('a34be691ce68f0acf4655c7c6c63a9a49ed276a11859d7224fd94fc2f657cd7a')
source_x86_64=("https://github.com/graalvm/graalvm-ce-builds/releases/download/jdk-${pkgver}/graalvm-community-jdk-${pkgver}_linux-x64_bin.tar.gz")
source_aarch64=("https://github.com/graalvm/graalvm-ce-builds/releases/download/jdk-${pkgver}/graalvm-community-jdk-${pkgver}_linux-aarch64_bin.tar.gz")

latestver() {
    gh api --paginate repos/graalvm/graalvm-ce-builds/releases --jq '.[] | select(.draft == false and .prerelease == false) | .tag_name' |
        sed -nE "s/^jdk-(${_java//./\\.}\\.[0-9]+\\.[0-9]+)$/\\1/p" |
        sort -V |
        tail -1
}

package() {
    cd graalvm-community-openjdk-${pkgver}+*
    mkdir -p "$pkgdir/usr/lib/jvm/java-${_java}-graalvm/"
    cp -a -t "$pkgdir/usr/lib/jvm/java-${_java}-graalvm/" *
    install -DTm644 LICENSE_NATIVEIMAGE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    sed "s/JAVA/${_java}/g" < "../graalvm-rebuild-libpolyglot.hook" > "graalvm-jdk${_java}-rebuild-libpolyglot.hook"
    install -DTm644 "graalvm-jdk${_java}-rebuild-libpolyglot.hook" "$pkgdir/usr/share/libalpm/hooks/graalvm-jdk${_java}-rebuild-libpolyglot.hook"
}
